---
Status: published
Lang: en
Title: Triple Store, Triple Progress: Datalevin Posited for the Future
Date: 2026-01-19T16:00:00.000Z
Author: Huahai
Category: experience
Tags: Datalevin,Database,Datalog,Triplestore,Graph,Rules
---

![Interactive Short Query Performance](/images/interactive-short-query-performance.svg)

In my previous post, [Competing for the JOB with a
Triplestore](https://yyhh.org/blog/2024/09/competing-for-the-job-with-a-triplestore/), I showed that a triple
store, such as [Datalevin](https://github.com/juji-io/datalevin), can compete
with the best row stores on complex relational workloads. Since then, I have
rewritten Datalevin's rule engine and improved its storage and query engine.
This post focuses on why these matter for the broader goal of using a triple
store as a single, flexible data substrate.

## One store, many workloads

Our goal is to simplify data storage and access by supporting diverse database
use cases and paradigms, because maximal flexibility is the core strength of a
triple store. Using one data store for different use cases simplifies and
reduces the cost of software development, deployment, and maintenance.

Since 2020, we have been working hard toward this goal of building an easy-to-use
and versatile database. I am happy to report that, today, in addition to
key-value and relational database features, Datalevin also handles graph queries
and deductive logic reasoning tasks, with built-in support for full-text search
and vector similarity search as well. All these are seamlessly integrated in a
compact package that works in both embedded and server modes.

This post is a guided tour of the progress made so far in the storage engine,
the query engine, and the new rule engine.

## Triples as the substrate

Datalevin stores data as triples: entity, attribute, value (EAV): the smallest,
atomic unit of a data item. This uniform representation is the key that lets one
engine handle many shapes of data and many ways of asking questions. A triple
store can behave like a relational system when your data is tabular, like a
graph system when your data is connected, and like a logic system when you
define recursive rules.

The challenge has always been performance. Triple stores have historically been
slower than row/column stores. The rest of this post explains how Datalevin
addresses this challenge.

## Storage

Datalevin uses a fast key-value database library as the storage layer.
Specifically, the exceptional read performance of
[LMDB](https://en.wikipedia.org/wiki/Lightning_Memory-Mapped_Database) is the
foundation of Datalevin's query performance. Datalevin stores triples with
nested indices by leveraging LMDB's DUPSORT capability: the head element of a
triple is stored once as the key, and the tail elements are stored as a sorted
list of values. This reduces storage overhead and alleviates the data redundancy
problem inherent in triple stores.

To further reduce data redundancy, we built our own LMDB fork,
[DLMDB](https://github.com/huahaiy/dlmdb), which adds page-level prefix
compression to the storage. For DUPSORT, prefix compression is applied to both
keys and values, resulting in significant storage savings. We also removed the
lesser-used `VAE` index. For a typical reference-heavy (foreign key) Datalog
database, the footprint reduction can be over 40%.

Through relentless code optimization, we achieved these savings
without incurring excessive read/write overhead. In fact, for the common
Datalevin use case of seeking to a key and reading its list of values in full,
we obtained a 40% speedup in most cases.

The Datalevin query planner relies heavily on online counting and sampling. To
facilitate these operations, we added subtree node count maintenance in DLMDB.
These order statistics turn counting and sampling operations from O(n) to O(log
n), cutting Datalog query planning time in half. This feature was introduced with
minimal write overhead.

## Query engine

Datalevin's query planner performs extensive query rewrite passes to optimize
performance. For example, predicates are pushed down into index scans so
filters execute early rather than after joins; inequality predicates are
rewritten into index range scans, and so on.

The planner simplifies the query graph by treating stars as meta-nodes, then
applies a Selinger-style dynamic programming algorithm with accurate cardinality
estimates. Merge scans collapse star-shaped entity access into a single scan,
avoiding redundant joins for attributes belonging to the same entity group. More
details on these optimizations can be found in the [query engine
documentation](https://github.com/juji-io/datalevin/blob/master/doc/query.md).

Even with relatively accurate cardinality estimation, occasional bad plans are
unavoidable, particularly for tricky joins that link different
entities. To reduce the impact of such cases, the cost-based optimizer now
considers hash joins as an alternative when input size is large. We also
extended the optimizer's coverage to more complex query clauses, such as
`or-join`.

We made the multi-threaded query execution pipeline more robust by handling edge
cases in concurrency and adding backpressure. The pipeline now uses its own
thread pool to avoid contention with worker thread pools.

Other improvements have focused on usability: "creature-comfort" features like
a `:having` clause, allowing math expressions in `:find`, specifying sort
variables by indices in `:order-by`, full boolean search expressions for
full-text, and so on. These features reduce the amount of custom code needed for
post-processing results, and in-database operations are usually more efficient
than equivalent work in application code.

## Rule engine

Datalevin uses rules to bundle a set of query clauses into named, reusable
invocations. As rules can call themselves and other rules, this feature enables
recursive logic computation and graph navigation. We wrote a new rule engine
that leverages the same cost-based optimizer, allowing Datalevin to serve as an
efficient graph database and logic reasoner.

The rule engine uses semi-naive fixpoint evaluation, applies magic-set rewrites
where beneficial, and seeds evaluation from outer query bindings so it starts with
relevant candidates instead of a blank slate.

In addition, non-recursive rule clauses are inlined into the main query to let
the optimizer plan them with index scans and joins. For T-stratified rules,
temporal elimination avoids storing unnecessary intermediate results. Detailed
information is available in the [rule engine
documentation](https://github.com/juji-io/datalevin/blob/master/doc/rules.md).

## Benchmarks

We added two new benchmarks to showcase the progress we have made.

### Logic workloads: Math Genealogy benchmark

The [Math Genealogy
benchmark](https://github.com/juji-io/datalevin/tree/master/benchmarks/math-bench)
focuses entirely on rule resolution. It is a good stress test for recursive
Datalog rules. The dataset contains roughly 256,769 dissertations, 256,767
students, and 276,635 advisor-student relationships. There are four queries in
this benchmark. Datalevin's rule engine is very fast on these queries: Q1 (14.4
ms), Q2 (330.9 ms), Q3 (269.6 ms), and Q4 (recursive academic ancestry, 2.9 ms).

By comparison, Datomic takes over 40 seconds on Q4, and Datascript runs out of
memory. This query is difficult because recursive ancestry computes a transitive
closure: each new level of ancestors can join with every previously found level,
which can quickly create a combinatorial explosion of intermediate tuples. Even if
the average branching factor is modest (say b=3–5 advisors per student),
intermediate results can grow on the order of b^k at depth k. If those tuples
are generated repeatedly across branches, we end up materializing large
intermediate relations just to discard most of them later.

Why is Q4 so fast in Datalevin? It exploits bound starting points. The
semi-naive fixpoint evaluation works off delta relations only, i.e., each
iteration only joins newly produced tuples. When a query binds a head argument,
the engine also seeds recursion (and, when effective, applies magic-set
rewrites) so it only explores the reachable slice of the graph rather than
materializing the full closure.

### Graph workloads: LDBC SNB benchmark

Graph workloads are where triple stores should shine, but performance is where
dedicated graph databases usually try to defend their turf. The [LDBC Social
Network Benchmark (SNB)](https://ldbcouncil.org/benchmarks/snb/) is an
industry-standard benchmark for interactive graph queries. We implemented the
full workload and included a Neo4j implementation for comparison
[here](https://github.com/juji-io/datalevin/tree/master/benchmarks/LDBC-SNB-bench).

On the SF1 dataset (about 3.2M entities and 17.3M edges), Datalevin is 27x to
620x faster on short interactive queries (pictured above), averaging 48x
faster than Neo4j. These short queries are the most commonly encountered
workloads in an operational graph database, so performing well on them has
significant practical implications.

Some of these short queries (IS2 and IS6) involve unbounded graph
traversal, such as finding the root post of a comment. Datalevin handles these
with a recursive rule. Thanks to the efficiency of our rule engine, graph
navigation performance is stellar.

On complex queries, Datalevin is about 12% faster overall, with some
queries (IC6, IC8, IC11) orders of magnitude faster and a few (IC3, IC5, IC9)
slower than Neo4j. I am sure Neo4j is extensively tuned for these queries, as it
is one of the authors of this industry-standard benchmark. It is remarkable that
Datalevin performs so well on these complex graph queries without any specific
tuning.

The important observation here is that the same triple store and query
engine handle both relational-style joins and graph traversals without
needing special cases for either.

## Towards the future

A triple store is a flexible substrate. When paired with a cost-based query
optimizer and a modern rule engine, it can span relational, graph, and logical
reasoning workloads. It can also expand toward richer document workloads
without changing the underlying model.

With the current focus on AI systems, a triple store like Datalevin can serve
several critical purposes.

An AI agent needs a context graph: entities, facts, relations, constraints, and
memories that evolve over time. Keeping that context in one integrated store
reduces the impedance mismatch between relational tables, graph edges, embeddings,
and documents. Datalevin makes retrieval and grounding first-class: full-text
and vector search can pull candidate facts, while Datalog queries and rules can
verify, connect, and constrain them. It can also support tool use, where the "tool
outputs" are simply more facts to join and reason over. For example, in a RAG
pipeline, vector search retrieves candidate snippets, graph relations link
them to entities and events, and rules enforce constraints such as provenance or
recency.

Datalevin can serve as an agent's memory model, where episodic facts,
long-term knowledge, and computed embeddings all live in one place and can be
queried together. In that sense, a unified store is to an AI agent what memory
is to human cognition: the common ground where different kinds of signals meet
to be reasoned over.

Even as AI writes more code, a simple and versatile database remains highly
AI-friendly. A context-limited LLM model benefits from a coherent data model and
a single query language that covers many use cases. Datalog is truly
declarative, meaning there are fewer procedural or implementation details for a
model to trip over. That translates to less boilerplate, fewer dialects to
remember, and fewer quirks in query semantics, making it more likely that the
system handles data correctly. In fact, AI wrote all the Datalevin queries used
in the LDBC SNB benchmark mentioned above. Although it is still a relatively
niche database, the AI composed queries for Datalevin with ease because the
query language is inherently simpler.

## Next steps

The recent rule engine rewrite brings us much closer to the 1.0 release
milestone. With the addition of high availability, a JSON API, and libraries for
other languages, we expect to reach this milestone this year.

After six years of continuous research and development, Datalevin would not be
in its current hardened state without the experimentation and production deployment
efforts of the Clojure community. I truly appreciate everyone who has used Datalevin
and made contributions. The future of simplified data storage and access is
near, for human and AI developers alike.
