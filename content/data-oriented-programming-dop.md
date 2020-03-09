Title: Data-Oriented Programming (DOP)
Date: 2016-12-03 23:33
Author: Huahai
Category: opinion
Tags: Programming, Clojure
Slug: data-oriented-programming-dop
Alias: /blog/2016/12/data-oriented-programming-dop
Lang: en

JSON is arguably the world's most popular human readable data format today.  It has largely replaced XML as the data exchange format on the Internet. One of the key reasons for the proliferation of JSON is its simplicity.  The data structure are very limited: only arrays, enclosed with \[\]; and objects, enclosed with {}. That's it. It cannot be simpler.

Apparently, this dead simple data format is enough to represent the vast landscape of data that JSON becomes the de-facto data format for Web services. Most Web APIs we use today speaks JSON. However, JSON is not native for most programming languages. It becomes a pain to convert to and back from JSON in programming languages.

What if we develop a Data-Oriented Programming (DOP) language, that can speak something similar to JSON natively?

Luckily, this language already exists. It is called Clojure!

In Clojure, \[\] means the same thing as in JSON, {} means essentially the same thing as well: a key value map. The only thing added, which makes it a programming language instead of a purely data format, is a pair of (). What () enables is the abilities to define and call functions. With this additon, we get a fully general purpose programming language.

As you may have suspected, using () to define and call functions is what Lisp do. So you are right, in this sense, Clojure is a Lisp. But with the ability to handle data like in JSON, it is a Data-Oriented Programming language.

So, there you have it, Clojure is the first DOP language, a DOP Lisp.
