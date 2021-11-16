---
Status: draft
Lang: en
Title: Beat Lucene in Less Than 600 Lines of Code
Date: 2021-11-05T14:49:00.957Z
Author: Huahai
Category: experience
Tags: Clojure,Datalevin
---
OK, I will admit that this title is rather hyperbole, a click-bait. However, it is also not a lie.

Here is the story. I am adding full-text search capability to [Datalevin](https://github.com/juji-io/datalevin), a Datalog database that we open sourced last year. For this task, I have decided to write a search engine from scratch instead of using an existing search library. [Here](https://github.com/juji-io/datalevin/blob/search/doc/search.md#rationale) are some rationales for this decision. Today I finished the main work of the search engine, and ran some [benchmark](https://github.com/juji-io/datalevin/tree/search/search-bench) comparison with [Apache Lucene](https://lucene.apache.org/), the venerable Java search library, and found that the Datalevin search engine is 75% faster on average than Lucene, while 3 times faster at the median. Since Lucene is such a dominant force in the full text search, I think it might be worth to write about it.

Yes, it is true. The search engine is [less than 600 lines of Clojure code](https://github.com/juji-io/datalevin/blob/search/src/datalevin/search.clj).

## Lucene is Hard to Beat

Lucene has over 20 years of history, with perhaps hundreds of man-year of work behind her development. Any search engines coming out with better numbers than Lucene is suspicious of lying, incompetence in benchmarking, or both. I will not name names, but a Google search should show some examples of those. Obviously, I would not want to add Datalevin to such a hall of shame. Please do report any errors in my [benchmark](https://github.com/juji-io/datalevin/tree/search/search-bench).

## Better Search Algorithm

To beat Lucene, it is obviously not enough to optimize code, as Lucene is highly optimized to the last fine details. For example, Lucene has multiple versions of `PriorityQueue` implementations, each customized to a different use case. It is insane.

So, to beat Lucene, better algorithm is pretty much a requirement. Luckily, I did come up with a better search algorithm, which I call *T-Wand*.

By "better", I mean two senses.

### Better Relevance

How many time have you frustrated that the search engine gave you results that you know are worse than what you should be getting? 

> I know there are some documents containing all these search words, why are they not here?  

"Here" means the first page, or being in the "top-K" results in research parlance. Full text search engines, like Lucene, are often optimized to return a limited number (K) of good results as quickly as possible. However, what is a "good" result? This is where the ideas get muddier. It is no longer a purely technical problem, but more of a user experience problem. In research parlance, this is called "relevance".

As someone who has a Ph.D. in Human-computer Interaction (;-)), I feel like I am entitled to define what is "good" in search. I hereby declare that:

> A good top-K algorithm should rank a document containing more user query terms higher than a document containing less number of user query terms. 

This makes perfect sense. Right?

Right. Unfortunately, most search engines, including Lucene, do not do that. 

Most search engines use something called a vector space model, where both user queries and documents are reduced to vectors (i.e. a fixed number of numbers). That is to say, the search engines are not looking at the meanings of the queries or the documents. Instead, they turned them both into some numbers. The search problem, is reduced to a problem of finding the similarity between the numbers representing the query and the numbers representing the documents.

An often used similarity measure, is to treat these numbers as coordinates in some kind of space. Now both a query and a document become vectors (or points) in this space. And if you remember any of the high school math, you will know that one can calculate the angle between a query vector and a document vector. This angle is the similarity search engines use to rank the documents based on the query. The smaller is the angle, the higher ranking is a document.

This is an elegant model. However, as you can see, this vector space model does not explicitly require a higher ranking document to contain more query terms than a lower ranking one. The results often come out violating the above requirement, hence user frustration inducing.

*T-Wand* sets to change that.

### Better Search Speed

*T* of *T-Wand* stands for *Tiered*. As you might have guessed, our search algorithm divides the document collections into tiers. The first tier are those documents containing all `n` user query terms, the second tier are those containing `n-1` user query terms, so on and so forth.

With this division, we no longer need to consider the whole document collection as the potential result candidates. Instead, only those in the current tier are. With much less work to do, the search speed is going to be better.

## *T-Wand* Algorithm

Did I say Lucene is very fast? Lucene is very fast, because it uses one of the state of art search algorithms, *Wand* [1]. Here's how *Wand* works. 

It cheats.

Well, any good algorithm looks like cheating. *Wand* is no exception. Basically, it skips a large portion of document collection, and it skips them *safely*, meaning the results would be the same if one exhaustively does the full computation. It was able to *safely* skip documents by using two tricks. 

The first trick is the most ingenious. I still do not know how my former colleagues at IBM Research came up with it. My hat's off to them. Let me steal a picture from a followup article by others [2] to illustrate this.

As can be seen, the 4 rows are the document ids of 4 query terms, and four iterators are walking the document ids. At each step of the iteration, *Wand* arranges the rows such that the current document ids of the rows are sorted from lower to higher. 

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

\[1] Broder, Carmel, Herscovici, Soffer and Zien, Efficient Query Evaluation using a Two-Level Retrieval Process, CIKM'2003.

\[2] Ding and Suel. Faster top-k document retrieval using block-max indexes." SIGIR'2011.