---
Status: draft
Lang: en
Title: Writing a fast search engine with 500 lines of code
Date: 2021-11-05T14:49:00.957Z
Author: Huahai
Category: experience
Tags: Clojure,Datalevin
---

The reason to store and access term information in aggregates, instead of
storing them in inverted lists and accessed piece-meal, is because LMDB is very
efficient (more efficient than file systems) at reading/writing large binary
blobs. As long as the data structure to be stored has high (de)serialization
speed, it is more efficient to store/retrieve them in large aggregates than in
more granular forms. This does not apply for more complex data structures with
high construction cost, e.g. hash maps. We consider these general advises in how
to best use the so called single-level storage, such as LMDB. We earned these
lessons in our many iterations of speeding up the search.

At this point, we achieved about 65%
overall speed of Lucene, measured 840 queries per seconds in my benchmark vs.
Lucene's 1300. Our median query speed is actually faster than Lucene, but
the long tail query time is way slower. That is because Lucene cheats. I am
joking. Well, all good algorithms look like cheating, if cheating means avoid
doing unnecessary work. Our algorithm described above certainly does. In this case, Lucene uses an early termination method called WAND, so it's long tail is very short.



[1] Efficient Query Evaluation using a Two-Level Retrieval * Process" by Broder, Carmel, Herscovici, Soffer and Zien