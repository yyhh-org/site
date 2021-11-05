---
Status: draft
Lang: en
Title: Beat Lucene in 600 lines of code
Date: 2021-11-05T14:49:00.957Z
Author: Huahai
Category: experience
Tags: Clojure,Datalevin
---
At this point, we achieved about 65%
overall speed of Lucene, measured 840 queries per seconds in my benchmark vs.
Lucene's 1300. Our median query speed is actually faster than Lucene, but
the long tail query time is way slower. That is because Lucene cheats. I am
joking. Well, all good algorithms look like cheating, if cheating means avoid
doing unnecessary work. Our algorithm described above certainly does. In this case, Lucene uses an early termination method called WAND, so it's long tail is very short.

[1] Efficient Query Evaluation using a Two-Level Retrieval * Process" by Broder, Carmel, Herscovici, Soffer and Zien