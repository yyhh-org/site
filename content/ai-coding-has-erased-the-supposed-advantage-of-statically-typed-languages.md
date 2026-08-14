---
Status: published
Lang: en
Title: AI Coding Has Erased the Supposed Advantage of Statically Typed Languages
Date: 2026-08-13T12:00:00.000Z
Author: Huahai
Category: opinion
Tags: AI,Programming Languages,Static Typing,Software Development,LLM,Clojure
---

For years, advocates of statically typed languages have made the same argument:
types catch mistakes earlier, compilers provide better feedback, IDEs offer
better assistance, and large codebases become safer to maintain.

That argument rests on an assumption that is rapidly becoming outdated: The
person writing the code is human.

AI is not human. It does not prefer Python because Python feels simple. It does
not admire Rust because Rust feels rigorous. It has no taste, no emotional
attachment, and no programming-language identity.

To an AI, languages differ primarily in how much code, and therefore how many
tokens, it must generate to express the same idea.

The more complicated the language, the more tokens it requires. The more tokens
it requires, the more opportunities the model has to make a mistake.

It really is that simple.

## AI Does Not Need a Type System to Catch Errors

Compiler feedback matters when humans write code.

People forget function signatures. They confuse return types, overlook null
values, miss fields, and call methods that do not exist. A type checker acts as
a guardrail, catching these mistakes before the program runs.

It is therefore tempting to apply the same logic to AI:

> Statically typed languages give AI more feedback, so AI produces better code
> in them.

This is mostly cargo-cult reasoning inherited from human programming.

When was the last time you saw a capable coding model remain stuck on an
ordinary compilation error?

A missing parenthesis, an incorrect primitive type, or a nonexistent method is
no longer the central problem in AI-generated software. Such errors
occasionally happen, but the model reads the compiler message and fixes them
almost immediately.

AI's expensive mistakes are not usually compilation errors. They are
misunderstandings.

The model implements the wrong business rule. It overlooks an edge case. It
misinterprets the meaning of the data. It breaks an unstated concurrency
assumption. It produces a system that is perfectly type-correct and logically
wrong. A type checker cannot save you from that.

The claim that AI needs "more compiler feedback" sounds technical, but it often
amounts to repeating an old argument without looking at the reality: AI almost
always one-shot the code, and compiler feedbacks are not involved for the most
part.

## Types Are Cost Too

Types are usually described as protection. They are rarely counted as cost.

For AI-generated code, however, a type declaration is first and foremost
additional information that must be generated, maintained, and kept consistent.

Types are valuable when they encode real domain constraints:

- An order total cannot be negative.
- A cancelled transaction cannot be settled again.
- An unauthenticated user cannot perform an administrative operation.

But much type information does not express constraints like these. It merely
repeats facts that are already obvious from the implementation:

- This argument is a string.
- This function returns a list of users.
- This value might be absent.
- This structure implements this interface.

In the human-programming era, this repetition helped programmers understand
unfamiliar code. It also allowed IDEs and compilers to catch simple mistakes.

But an AI model is already an extraordinarily capable pattern recognizer. It
can often infer these relationships from names, implementations, call sites,
tests, and surrounding context.

Requiring the model to state everything again does not automatically improve
correctness. It increases output length and adds another consistency
obligation.

If a constraint cannot eliminate a meaningful business error but requires
dozens of additional tokens, it may be providing ceremony rather than safety.

## Compilation Is No Longer the Scarce Capability

The most commonly advertised benefit of static typing is that it moves errors
into the compilation stage. In AI-assisted development, compilation errors are
among the cheapest errors possible.

The expensive errors are the ones the compiler cannot see:

- The requirement was misunderstood.
- The tests encode the wrong assumption.
- The data model does not reflect the real business.
- The API appears reasonable but breaks compatibility.
- The concurrent code type-checks but contains a race condition.
- The authorization logic compiles but permits unauthorized access.

A program compiling successfully proves only that it satisfies the small subset
of rules represented by its type system. Nowadays, this does not buy much,
because any frontier AI can almost always meet this narrow requirement in a
single shot.

Since AI-generated code already spends very little time stuck on basic compilation
failures, continuing to present compiler feedback as a decisive advantage is
like advertising a self-driving car on the strength of its gear-change
indicator. It may not be entirely useless, but it is simply no longer an
important issue.

## More Types Means More Tokens

For AI, one of the most meaningful differences between languages is how many
tokens are required to express the same behavior.

In a static typed language, a simple operation may require:

- Explicit type declarations
- Generic parameters
- Interfaces or traits
- Lifetime annotations
- Error-type conversions
- Optional-value wrappers
- Data-transfer objects
- Serialization annotations
- Several layers of adapter code

Those additional structures are not free. Longer code requires more generated
tokens. More symbols must remain consistent across the context. Changes touch
more declarations and more files. Every additional abstraction creates another
place where the model can misunderstand the programmer's intent.

AI does not automatically become more correct merely because the code looks
more rigorous. It simply now has more things to keep consistent.

More tokens mean more opportunities for error. More abstraction layers mean
more room for misunderstanding. More type machinery means more code that does
not directly express the business requirement.

On the other hand, dynamic languages may express the same behavior in a lot less
number of lines of code. For example, Clojure, a dynamic language, is shown to be the
most token efficient in [this
study](https://martinalderson.com/posts/which-programming-languages-are-most-token-efficient/).

## Language Costs Must Be Recalculated for the AI Era

This does not mean types have no value. Types can document interfaces, define
module boundaries, support tooling, and encode genuine domain constraints.

But that cost must now be evaluated honestly. Static typing should not be
treated as inherently superior.

Historically, type systems added code and complexity in exchange for reducing
human cognitive load and catching human mistakes.

Now, an increasing share of code is generated, modified, and interpreted by AI.
AI does not have the same memory limitations, and it rarely remains stuck on
syntax or elementary type errors. Its weaknesses lie elsewhere: ambiguous
requirements, hidden assumptions, sprawling context, and imperfect semantic
understanding.

The old benefit is shrinking while the old cost remains.

And now that tokens are a measurable expense, that cost is more visible than
ever.

AI does not care about language ideology. It is not participating in the
culture war between static and dynamic typing. It is generating tokens.

If two languages can solve the same problem, but one requires more declarations,
more boilerplate, more adapters, and more type gymnastics, that complexity does
not disappear. It becomes a longer context, a higher generation cost, and a
larger surface area for mistakes.

The supposed advantage of statically typed languages was built on a world in
which humans were the primary producers of code. That premise has changed. The
conclusion should change with it.
