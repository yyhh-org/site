---
Status: published
Lang: en
Title: Datalevin 1.0.0 Is Here: One Database for Application State and Agent Memory
Date: 2026-07-20T16:00:00.000Z
Author: Huahai
Category: experience
Tags: Datalevin,Database,Datalog,AI,Agent Memory
---

Today, after six years of development, I am thrilled to announce the
availability of **[Datalevin 1.0.0](https://github.com/datalevin/datalevin)**.

We started Datalevin in 2020 with a deceptively simple question: why should SQL
databases remain the default center of application state?

Six years of research, engineering, benchmarking, production use, and community
feedback later, Datalevin 1.0.0 is our answer. Datalevin is open source under
the [Eclipse Public License
2.0](https://github.com/datalevin/datalevin/blob/master/LICENSE). It is a
durable, high-performance, fact-first database that brings relational queries,
graph traversal, logical reasoning, document access, full-text search, and
vector search into one compact system.

The release completes the roadmap we set for 1.0: automatic path indexing for
documents; write-ahead logging and transaction-log access; read-only replicas
and high availability; a JSON API; broad libraries for Clojure, Java, Python,
and JavaScript; and much more.

It also arrives with two new ways to learn Datalevin. The new
**[Datalevin website](https://datalevin.org)** contains the online guide, with
examples in Clojure, Java, Python, and JavaScript. The complete book,
***[Datalevin: The Definitive Guide to Logical and Intelligent
Databases](https://www.amazon.com/dp/B0H8X1QF2Q/)***, is available in print and
ebook formats. In addition to the full database guide, the book contains five
chapters devoted to persistent memory for intelligent systems.

This is a release, a book, and a website. More importantly, it is the point at
which the original Datalevin idea becomes a complete platform.

## Replace SQL at the Center

Datalevin is not intended to be one more specialized database sitting beside a
SQL system. Its goal is to **replace SQL databases at the center of application
state**.

That does not mean recreating SQL with different syntax. It means replacing the
table as the center of gravity with the **fact**. Datalevin stores small
entity-attribute-value facts, or datoms. The same fact can participate in a
row-like record, a graph edge, a nested document workflow, a search result, or a
logical rule without being copied into a different data model.

Why make such a fundamental change? There are three main arguments.

### 1. SQL Is an Awkward Application Interface

SQL is a string-shaped language embedded inside programs. It has a large,
English-like syntax, many dialects, and poor composition with host-language
code. The enormous ecosystems of ORMs, query builders, migration tools, and
object mapping layers are not signs that SQL is a natural application
interface. They are evidence of how much machinery is needed to make it behave
like one.

Datalevin queries are data. Datalog expresses the facts that must be true, while
shared variables create joins implicitly. Rules package reusable logic, and
recursive rules use the same form as ordinary queries. The programmer describes
relationships instead of spelling out a sequence of join mechanics.

This smaller, more regular surface is easier for people to learn and easier for
programs to construct. It is also a better target for AI-generated queries:
fewer syntactic branches, fewer vendor-specific choices, and less
planner-sensitive ceremony.

### 2. Table-Shaped Storage Makes Complex Query Planning Harder

Rows bundle many individual facts into containers. When data are sparse,
skewed, or correlated, a SQL optimizer has a hard time estimating how many rows
will survive each predicate and join. Those cardinality estimates often depend
on histograms, independence assumptions, and other approximations. A bad
estimate can turn a reasonable query into a huge intermediate result.

A fact-first store begins with explicit, independently indexed data items.
Missing facts are absent rather than represented by positional `NULL` values.
Datalevin can count and sample the same indexed facts that query execution will
use, giving its cost-based optimizer better raw material for planning complex
joins.

This is not only a theoretical advantage. In the Join Order Benchmark,
Datalevin has demonstrated that a triplestore can
[outperform PostgreSQL and SQLite on complex relational
queries](https://yyhh.org/blog/2024/09/competing-for-the-job-with-a-triplestore/).
The same query engine also performs strongly on recursive logic and
[industry-standard graph
workloads](https://yyhh.org/blog/2026/01/triple-store-triple-progress-datalevin-posited-for-the-future/).

### 3. Stacking Extensions Creates an Integration Tax

Modern SQL databases can add JSON, full-text search, vector indexes, graph
features, recursive queries, and procedural extensions. Each capability is
useful. The trouble starts when one application question needs several of them
at once.

Every extension tends to bring its own syntax, operators, index types, cost
model, and operational rules. If the capabilities are split into separate
services, the application must also synchronize copies of data and reconcile
results across network boundaries. Either way, the glue moves into application
code.

Datalevin makes these capabilities composable over one database state in the
same elegant fact based model. A single query can ask for documents that contain
a phrase, are close to a question in embedding space, belong to a particular
entity in a graph, satisfy a nested document predicate, and pass exact
permission and lifecycle rules. The database does the integration work where it
belongs.

## A Memory Substrate for AI Agents

That unified model matters even more for AI agents.

An agent needs more than a transcript and more than a vector database. It needs
durable episodes, structured facts, goals, tasks, permissions, tool results,
source documents, relationships, and a bounded view of what matters now. It
needs to recall by similarity, but it must also know which facts are current,
which source supports them, who is allowed to see them, and what they are
connected to.

Datalevin is designed to be the **memory substrate** underneath that system:

* **Full-text search** recalls information by words, phrases, and boolean search
  expressions.
* **Vector and embedding search** recalls information by semantic similarity.
* **Logical access** uses Datalog queries and rules to enforce exact conditions,
  derive facts, and reason recursively.
* **Graph access** follows relationships among users, episodes, facts, goals,
  tasks, evidence, and documents.
* **Document access** keeps nested EDN, JSON, and Markdown values intact while
  automatically indexing their paths.
* **Relational access** joins structured application state without giving up the
  fact-first model.

These are not six disconnected products. They are six ways to see and retrieve
the same durable fact based state.

That distinction is crucial. Similarity search can find plausible memories, but
similarity alone cannot decide whether a fact is authorized, supported,
superseded, or relevant to the active goal. Datalevin lets vector and full-text
recall produce candidates, then lets logic, graph relationships, document
predicates, and ordinary joins constrain and explain the result.

Datalevin does not try to be an agent runtime. The application still owns model
calls, tool authorization, ingestion policy, consolidation, truth maintenance,
and prompt assembly. Datalevin provides the durable, transactional environment
in which those decisions can be stored, inspected, queried, and resumed. Its
built-in MCP server can also expose this memory directly to MCP-compatible AI
tools.

In other words, a context window is temporary attention. Datalevin is memory.

## One Database, Almost the Same API Everywhere

Datalevin began as a Clojure library, but 1.0 is not limited to Clojure
applications. The Clojure, Java, Python, and JavaScript APIs now cover almost
the same public surface:

| Capability | Clojure | Java | Python | JavaScript |
| --- | --- | --- | --- | --- |
| Embedded and remote connections | Yes | Yes | Yes | Yes |
| Datalog query, pull, and explain | Yes | Yes | Yes | Yes |
| Synchronous and asynchronous transactions | Yes | Yes | Yes | Yes |
| Datoms, index reads, bulk loading, and re-indexing | Yes | Yes | Yes | Yes |
| Key-value APIs and explicit KV transactions | Yes | Yes | Yes | Yes |
| Full-text, vector, embedding, and idoc access | Yes | Yes | Yes | Yes |
| Standalone search and vector indexes | Yes | Yes | Yes | Yes |
| UDF registries and query, transaction, and analyzer UDFs | Yes | Yes | Yes | Yes |
| Backup, snapshots, transaction logs, replicas, and HA administration | Yes | Yes | Yes | Yes |

The remaining differences are small and explicit. JavaScript does not expose
the Datalog transaction callback because callback re-entry through the Node/JVM
bridge can deadlock. Staged mutation of an existing entity object remains a
Clojure-only convenience; Java, Python, and JavaScript use transaction maps or
builders instead. The full, current list lives in the
[language compatibility
matrix](https://github.com/datalevin/datalevin/blob/master/doc/language-compatibility.md).

Whatever language you choose, the important parts do not change: the same
facts, schema, transactions, Datalog queries, and indexes.

## Embedded, Server, or Script: Choose at Deployment Time

The data model should not have to change when the deployment topology changes.
Datalevin therefore supports three primary ways to run:

| Mode | Use it for |
| --- | --- |
| **Embedded** | Link Datalevin into a Clojure, Java, Python, or Node.js process for fast local access, much like SQLite. |
| **Server** | Share databases across processes or machines with remote clients, role-based access control, read-only replicas, and high availability. |
| **Scripting** | Use the Babashka pod for fast-starting automation, command-line tools, data jobs, and operational scripts. |

There is also an MCP server mode for local AI-tool integration. You can begin
with an embedded prototype, move to a shared server as the application grows,
and automate it from scripts without rewriting the data model or query language.

Deployment changes. The facts do not.

## Start Building

Datalevin 1.0.0 is available now:

* Read the new guide at **[datalevin.org](https://datalevin.org)**.
* Get the complete print or ebook edition of ***[Datalevin: The Definitive
  Guide](https://www.amazon.com/dp/B0H8X1QF2Q/)***.
* Explore, use, and contribute to the open-source code on
  **[GitHub](https://github.com/datalevin/datalevin)**.
* Use Datalevin from
  **[Clojure](https://clojars.org/datalevin)**,
  **[Java](https://central.sonatype.com/artifact/org.datalevin/datalevin-java)**,
  **[Python](https://pypi.org/project/datalevin/)**, or
  **[JavaScript](https://www.npmjs.com/package/datalevin-node)**.

Reaching 1.0 took six years because the goal was never merely to ship another
query language or another storage wrapper. The goal was to build one coherent
place for application state: simple enough to embed, serious enough to run as a
server, expressive enough for relational, graph, document, and logical work,
and intelligent enough to become durable memory for the next generation of AI
systems.

Thank you to everyone who tested Datalevin, reported issues, contributed code,
shared benchmarks, trusted it in production, or simply asked hard questions.
You helped turn an ambitious idea into a 1.0 database.

**Datalevin 1.0.0 is here. Let us build applications and agents that remember.**
