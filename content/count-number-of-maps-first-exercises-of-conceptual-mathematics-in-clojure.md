---
Title: "Count Number of Maps: First Exercises of Conceptual Mathematics in Clojure"
Date: 2012-05-16 20:33
Author: Huahai
Category: notebook
Tags: Math, CategoryTheory, Programming, Clojure 
Slug: count-number-of-maps-first-exercises-of-conceptual-mathematics-in-clojure
Alias: /blog/2012/05/count-number-maps-first-exercises-conceptual-mathematics-clojure
Lang: en
---

As [previously mentioned](http://yyhh.org/blog/2012/04/start-learning-category-theory), I am learning category theory, beginning with [Lawvere](http://en.wikipedia.org/wiki/William_Lawvere)'s [Conceptual Mathematics](http://www.amazon.com/Conceptual-Mathematics-First-Introduction-Categories/dp/052171916X) book. This is a very elementry book that assumes almost nothing as a background. However, it is still a math book, which requires doing some exercises. Since the book provides no answer to exercises, I decide to make my own and post them here as I did them. Hopefully someone will find them useful.

Since a large part of category theory is constructive, I will try to implement the concepts computationally in order to understand them better. Cateogry theory has been implemented as types in some strong typed languages such as [ML](http://www.cs.man.ac.uk/~david/categories/) and Haskell. I think it would be fun to see how it would look in a dynamic typed language such as Clojure. Even if I could not go very far, at minimum, I will have a mechanical means to check my solutions to the exercises.

The first article of the book deals with the category of sets, and the main topic is about maps between sets. The second article talks about isomorphisms and related concepts. Some exercises (on page 20 and 47) are of the "how many maps are there" variety. Here are some Clojure code I used to calculate the results.

<font face="monospace"><br /><span><font color="#912f11">(</font></span><span><font color="#800090">ns</font></span> CM.core<br />   <font color="#cd3700">(</font><span><font color="#1f3f81"><b>:use</b></font></span> clojure.math.combinatorics<font color="#cd3700">)</font><span><font color="#912f11">)</font></span> <p><span><font color="#912f11">(</font></span><span><font color="#800090">defn</font></span> all-maps<br />   <span><font color="#077807">"Return a lazy sequence of all the possible maps from a domain to </font></span><br /><span><font color="#077807">  a codomain"</font></span><br />   <span><font color="#912f11">[</font></span>domain codomain<span><font color="#912f11">]</font></span><br />   <font color="#cd3700">(</font><span><font color="#1f3f81"><b>map</b></font></span> <span><font color="#912f11">#(</font></span><span><font color="#007080">conj</font></span> <span><font color="#912f11">{</font></span><span><font color="#1f3f81"><b>:domain</b></font></span> domain <span><font color="#1f3f81"><b>:codomain</b></font></span> codomain<span><font color="#912f11">}</font></span> <span><font color="#912f11">[</font></span><span><font color="#1f3f81"><b>:rule</b></font></span> <span><font color="#912f11">(</font></span><span><font color="#007080">zipmap</font></span> %<span><font color="#077807">1</font></span> %<span><font color="#077807">2</font></span><span><font color="#912f11">)])</font></span><br />        <font color="#ee9a00">(</font><span><font color="#007080">repeat</font></span> domain<font color="#ee9a00">)</font><br />        <font color="#ee9a00">(</font><span><font color="#007080">apply</font></span> <span><font color="#007080">cartesian-product</font></span> <font color="#cdcd00">(</font><span><font color="#007080">repeat</font></span> <font color="#698b22">(</font><span><font color="#007080">count</font></span> domain<font color="#698b22">)</font> codomain<font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><span><font color="#912f11">)</font></span></p> <p><span><font color="#912f11">(</font></span><span><font color="#800090">defn</font></span> same-mapping-rule?<br />   <span><font color="#077807">"Return true if two mapping rules give the same results for a domain"</font></span><br />   <span><font color="#912f11">[</font></span>domain r1 r2<span><font color="#912f11">]</font></span><br />   <font color="#cd3700">(</font><span><font color="#007080">every?</font></span> <span><font color="#007080">identity</font></span> <font color="#ee9a00">(</font><span><font color="#1f3f81"><b>map</b></font></span> <span><font color="#007080">=</font></span> <font color="#cdcd00">(</font><span><font color="#1f3f81"><b>map</b></font></span> r1 domain<font color="#cdcd00">)</font> <font color="#cdcd00">(</font><span><font color="#1f3f81"><b>map</b></font></span> r2 domain<font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><span><font color="#912f11">)</font></span></p> <p><span><font color="#912f11">(</font></span><span><font color="#800090">defn</font></span> same-map?<br />   <span><font color="#077807">"Return true if two maps are the same"</font></span><br />   <span><font color="#912f11">[</font></span>f g<span><font color="#912f11">]</font></span><br />   <font color="#cd3700">(</font><span><font color="#800090">and</font></span> <font color="#ee9a00">(</font><span><font color="#007080">=</font></span> <font color="#cdcd00">(</font><span><font color="#1f3f81"><b>:domain</b></font></span> f<font color="#cdcd00">)</font> <font color="#cdcd00">(</font><span><font color="#1f3f81"><b>:domain</b></font></span> g<font color="#cdcd00">)</font><font color="#ee9a00">)</font><br />        <font color="#ee9a00">(</font><span><font color="#007080">=</font></span> <font color="#cdcd00">(</font><span><font color="#1f3f81"><b>:codomain</b></font></span> f<font color="#cdcd00">)</font> <font color="#cdcd00">(</font><span><font color="#1f3f81"><b>:codomain</b></font></span> g<font color="#cdcd00">)</font><font color="#ee9a00">)</font><br />        <font color="#ee9a00">(</font>same-mapping-rule? <font color="#cdcd00">(</font><span><font color="#1f3f81"><b>:domain</b></font></span> f<font color="#cdcd00">)</font> <font color="#cdcd00">(</font><span><font color="#1f3f81"><b>:rule</b></font></span> f<font color="#cdcd00">)</font> <font color="#cdcd00">(</font><span><font color="#1f3f81"><b>:rule</b></font></span> g<font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><span><font color="#912f11">)</font></span></p> <p><span><font color="#912f11">(</font></span><span><font color="#800090">defn</font></span> compose-map<br />   <span><font color="#077807">"Return a composed map, also ensure domains and codomains match"</font></span><br />   <span><font color="#912f11">[</font></span>f g<span><font color="#912f11">]</font></span><br />   <font color="#cd3700">(</font><span><font color="#912f11">if</font></span> <font color="#ee9a00">(</font><span><font color="#007080">=</font></span> <font color="#cdcd00">(</font><span><font color="#1f3f81"><b>:codomain</b></font></span> g<font color="#cdcd00">)</font> <font color="#cdcd00">(</font><span><font color="#1f3f81"><b>:domain</b></font></span> f<font color="#cdcd00">)</font><font color="#ee9a00">)</font><br />     <span><font color="#912f11">{</font></span><span><font color="#1f3f81"><b>:domain</b></font></span> <span><font color="#912f11">(</font></span><span><font color="#1f3f81"><b>:domain</b></font></span> g<span><font color="#912f11">)</font></span>, <span><font color="#1f3f81"><b>:codomain</b></font></span> <span><font color="#912f11">(</font></span><span><font color="#1f3f81"><b>:codomain</b></font></span> f<span><font color="#912f11">)</font></span>, <br />      <span><font color="#1f3f81"><b>:rule</b></font></span> <span><font color="#912f11">(</font></span><span><font color="#007080">comp</font></span> <font color="#cd3700">(</font><span><font color="#1f3f81"><b>:rule</b></font></span> f<font color="#cd3700">)</font> <font color="#cd3700">(</font><span><font color="#1f3f81"><b>:rule</b></font></span> g<font color="#cd3700">)</font><span><font color="#912f11">)}</font></span><br />     <font color="#ee9a00">(</font><span><font color="#1f3f81"><b>throw</b></font></span> <font color="#cdcd00">(</font>Exception. <span><font color="#077807">"Cannot compose, domain does not match codomain"</font></span><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><span><font color="#912f11">)</font></span></p> <p><span><font color="#912f11">(</font></span><span><font color="#800090">defn</font></span> composed? <br />   <span><font color="#077807">"Return true if map f and map g compose to map c"</font></span><br />   <span><font color="#912f11">[</font></span>f g c<span><font color="#912f11">]</font></span><br />   <font color="#cd3700">(</font>same-map? c <font color="#ee9a00">(</font>compose-map f g<font color="#ee9a00">)</font><font color="#cd3700">)</font><span><font color="#912f11">)</font></span><br />   <br /><span><font color="#912f11">(</font></span><span><font color="#800090">defn</font></span> idempotent? <br />   <span><font color="#077807">"Return true if the given map return the same results as when it is </font></span><br /><span><font color="#077807">  applied twice"</font></span><br />   <span><font color="#912f11">[</font></span>f<span><font color="#912f11">]</font></span><br />   <font color="#cd3700">(</font>composed? f f f<font color="#cd3700">)</font><span><font color="#912f11">)</font></span></p> <p><span><font color="#912f11">(</font></span><span><font color="#800090">defn</font></span> solutions<br />   <span><font color="#077807">"Return a lazy sequence of maps that match the given predicates and go</font></span><br /><span><font color="#077807">  from the given domain to given codomain"</font></span><br />   <span><font color="#912f11">[</font></span>pred domain codomain<span><font color="#912f11">]</font></span><br />   <font color="#cd3700">(</font><span><font color="#1f3f81"><b>filter</b></font></span> pred <font color="#ee9a00">(</font>all-maps domain codomain<font color="#ee9a00">)</font><font color="#cd3700">)</font><span><font color="#912f11">)</font></span></p> <p><span><font color="#912f11">(</font></span><span><font color="#800090">defn</font></span> idempotent-maps<br />   <span><font color="#077807">"Return a lazy sequence of idempotent maps between a domain and itself </font></span><br /><span><font color="#077807">  as the codomain"</font></span><br />   <span><font color="#912f11">[</font></span>domain<span><font color="#912f11">]</font></span><br />   <font color="#cd3700">(</font>solutions idempotent? domain domain<font color="#cd3700">)</font><span><font color="#912f11">)</font></span></p> <p><span><font color="#912f11">(</font></span><span><font color="#800090">defn</font></span> choice<br />   <span><font color="#077807">"Return a lazy sequence of maps that are applied before the given map to</font></span><br /><span><font color="#077807">  return the same results as the given composed map, i.e. solution of </font></span><br /><span><font color="#077807">  choice problem"</font></span><br />   <span><font color="#912f11">[</font></span>f c<span><font color="#912f11">]</font></span><br />   <font color="#cd3700">(</font>solutions <span><font color="#912f11">#(</font></span>composed? f <span><font color="#912f11">%</font></span> c<span><font color="#912f11">)</font></span> <font color="#ee9a00">(</font><span><font color="#1f3f81"><b>:domain</b></font></span> c<font color="#ee9a00">)</font> <font color="#ee9a00">(</font><span><font color="#1f3f81"><b>:domain</b></font></span> f<font color="#ee9a00">)</font><font color="#cd3700">)</font><span><font color="#912f11">)</font></span></p> <p><span><font color="#912f11">(</font></span><span><font color="#800090">defn</font></span> determination<br />   <span><font color="#077807">"Return a lazy sequence of maps that are applied after the given map to</font></span><br /><span><font color="#077807">  return the same results as the given composed map, i.e. solution of </font></span><br /><span><font color="#077807">  determination problem"</font></span><br />   <span><font color="#912f11">[</font></span>g c<span><font color="#912f11">]</font></span><br />   <font color="#cd3700">(</font>solutions <span><font color="#912f11">#(</font></span>composed? <span><font color="#912f11">%</font></span> g c<span><font color="#912f11">)</font></span> <font color="#ee9a00">(</font><span><font color="#1f3f81"><b>:codomain</b></font></span> g<font color="#ee9a00">)</font> <font color="#ee9a00">(</font><span><font color="#1f3f81"><b>:codomain</b></font></span> c<font color="#ee9a00">)</font><font color="#cd3700">)</font><span><font color="#912f11">)</font></span></p> <p><span><font color="#912f11">(</font></span><span><font color="#800090">defn</font></span> section<br />   <span><font color="#077807">"Return a lazy sequence of maps that are sections of the given map"</font></span><br />   <span><font color="#912f11">[</font></span>f<span><font color="#912f11">]</font></span><br />   <font color="#cd3700">(</font>choice f <span><font color="#912f11">{</font></span><span><font color="#1f3f81"><b>:domain</b></font></span> <span><font color="#912f11">(</font></span><span><font color="#1f3f81"><b>:codomain</b></font></span> f<span><font color="#912f11">)</font></span> <span><font color="#1f3f81"><b>:codomain</b></font></span> <span><font color="#912f11">(</font></span><span><font color="#1f3f81"><b>:codomain</b></font></span> f<span><font color="#912f11">)</font></span> <span><font color="#1f3f81"><b>:rule</b></font></span> <span><font color="#007080">identity</font></span><span><font color="#912f11">}</font></span><font color="#cd3700">)</font><span><font color="#912f11">)</font></span></p> <p><span><font color="#912f11">(</font></span><span><font color="#800090">defn</font></span> retraction<br />   <span><font color="#077807">"Return a lazy sequence of maps that are retractions of the given map"</font></span><br />   <span><font color="#912f11">[</font></span>f<span><font color="#912f11">]</font></span><br />   <font color="#cd3700">(</font>determination f <span><font color="#912f11">{</font></span><span><font color="#1f3f81"><b>:domain</b></font></span> <span><font color="#912f11">(</font></span><span><font color="#1f3f81"><b>:domain</b></font></span> f<span><font color="#912f11">)</font></span> <span><font color="#1f3f81"><b>:codomain</b></font></span> <span><font color="#912f11">(</font></span><span><font color="#1f3f81"><b>:domain</b></font></span> f<span><font color="#912f11">)</font></span> <span><font color="#1f3f81"><b>:rule</b></font></span> <span><font color="#007080">identity</font></span><span><font color="#912f11">}</font></span><font color="#cd3700">)</font><span><font color="#912f11">)</font></span></p> <p><span><font color="#912f11">(</font></span><span><font color="#800090">defn</font></span> composed-solution-pairs <br />   <span><font color="#077807">"Return a lazy sequence of pairs of maps that compose to a given map, with</font></span><br /><span><font color="#077807">  the given shared domain in between"</font></span><br />   <span><font color="#912f11">[</font></span>domain c<span><font color="#912f11">]</font></span><br />   <font color="#cd3700">(</font><span><font color="#1f3f81"><b>filter</b></font></span> <br />     <span><font color="#912f11">#(</font></span>composed? <span><font color="#912f11">(</font></span><span><font color="#007080">first</font></span> %<span><font color="#912f11">)</font></span> <span><font color="#912f11">(</font></span><span><font color="#007080">last</font></span> %<span><font color="#912f11">)</font></span> c<span><font color="#912f11">)</font></span><br />     <font color="#ee9a00">(</font><span><font color="#1f3f81"><b>for</b></font></span> <span><font color="#912f11">[</font></span>g <span><font color="#912f11">(</font></span>all-maps <font color="#cd3700">(</font><span><font color="#1f3f81"><b>:domain</b></font></span> c<font color="#cd3700">)</font> domain<span><font color="#912f11">)</font></span><br />           f <span><font color="#912f11">(</font></span>all-maps domain <font color="#cd3700">(</font><span><font color="#1f3f81"><b>:codomain</b></font></span> c<font color="#cd3700">)</font><span><font color="#912f11">)]</font></span><br />       <span><font color="#912f11">[</font></span>f g<span><font color="#912f11">]</font></span><font color="#ee9a00">)</font><font color="#cd3700">)</font><span><font color="#912f11">)</font></span><br />       <br /><span><font color="#912f11">(</font></span><span><font color="#800090">defn</font></span> retraction-section-pairs<br />   <span><font color="#077807">"Return a lazy sequence of pairs of maps r and s, where r goes from domain</font></span><br /><span><font color="#077807">  X to domain A,  s goes from A to X, and r of s is the same as the identity </font></span><br /><span><font color="#077807">  map on A."</font></span><br />   <span><font color="#912f11">[</font></span>A X<span><font color="#912f11">]</font></span><br />   <font color="#cd3700">(</font>composed-solution-pairs X <span><font color="#912f11">{</font></span><span><font color="#1f3f81"><b>:domain</b></font></span> A <span><font color="#1f3f81"><b>:codomain</b></font></span> A <span><font color="#1f3f81"><b>:rule</b></font></span> <span><font color="#007080">identity</font></span><span><font color="#912f11">}</font></span><font color="#cd3700">)</font><span><font color="#912f11">)</font></span></p> <p><span><font color="#912f11">(</font></span><span><font color="#912f11">def</font></span> A <span><font color="#912f11">#{</font></span><span><font color="#077807">"John"</font></span> <span><font color="#077807">"Mary"</font></span> <span><font color="#077807">"Sam"</font></span><span><font color="#912f11">})</font></span><br /><span><font color="#912f11">(</font></span><span><font color="#912f11">def</font></span> B <span><font color="#912f11">#{</font></span><span><font color="#077807">"eggs"</font></span> <span><font color="#077807">"coffee"</font></span><span><font color="#912f11">})</font></span><br /><span><font color="#912f11">(</font></span><span><font color="#912f11">def</font></span> U <span><font color="#912f11">#{</font></span><span><font color="#1f3f81"><b>:b</b></font></span> <span><font color="#1f3f81"><b>:p</b></font></span> <span><font color="#1f3f81"><b>:q</b></font></span> <span><font color="#1f3f81"><b>:r</b></font></span> <span><font color="#1f3f81"><b>:s</b></font></span><span><font color="#912f11">})</font></span><br /><span><font color="#912f11">(</font></span><span><font color="#912f11">def</font></span> D <span><font color="#912f11">#{</font></span><span><font color="#077807">0</font></span> <span><font color="#077807">1</font></span><span><font color="#912f11">})</font></span></p> <p><span><font color="#912f11">(</font></span><span><font color="#912f11">def</font></span> one-a <span><font color="#912f11">{</font></span><span><font color="#1f3f81"><b>:domain</b></font></span> A <span><font color="#1f3f81"><b>:codomain</b></font></span> A <span><font color="#1f3f81"><b>:rule</b></font></span> <span><font color="#007080">identity</font></span><span><font color="#912f11">})</font></span><br /><span><font color="#912f11">(</font></span><span><font color="#912f11">def</font></span> one-b <span><font color="#912f11">{</font></span><span><font color="#1f3f81"><b>:domain</b></font></span> B <span><font color="#1f3f81"><b>:codomain</b></font></span> B <span><font color="#1f3f81"><b>:rule</b></font></span> <span><font color="#007080">identity</font></span><span><font color="#912f11">})</font></span><br /><span><font color="#912f11">(</font></span><span><font color="#912f11">def</font></span> one-d <span><font color="#912f11">{</font></span><span><font color="#1f3f81"><b>:domain</b></font></span> D <span><font color="#1f3f81"><b>:codomain</b></font></span> D <span><font color="#1f3f81"><b>:rule</b></font></span> <span><font color="#007080">identity</font></span><span><font color="#912f11">})</font></span></p> <p><span><font color="#912f11">(</font></span><span><font color="#912f11">def</font></span> g <span><font color="#912f11">{</font></span><span><font color="#1f3f81"><b>:domain</b></font></span> U <span><font color="#1f3f81"><b>:codomain</b></font></span> D <span><font color="#1f3f81"><b>:rule</b></font></span> <span><font color="#912f11">{</font></span><span><font color="#1f3f81"><b>:b</b></font></span> <span><font color="#077807">0</font></span> <span><font color="#1f3f81"><b>:p</b></font></span> <span><font color="#077807">0</font></span> <span><font color="#1f3f81"><b>:q</b></font></span> <span><font color="#077807">0</font></span> <span><font color="#1f3f81"><b>:r</b></font></span> <span><font color="#077807">1</font></span> <span><font color="#1f3f81"><b>:s</b></font></span> <span><font color="#077807">1</font></span><span><font color="#912f11">}})</font></span><br /><span><font color="#912f11">(</font></span><span><font color="#912f11">def</font></span> f <span><font color="#912f11">{</font></span><span><font color="#1f3f81"><b>:domain</b></font></span> D <span><font color="#1f3f81"><b>:codomain</b></font></span> U <span><font color="#1f3f81"><b>:rule</b></font></span> <span><font color="#912f11">{</font></span><span><font color="#077807">0</font></span> <span><font color="#1f3f81"><b>:b</b></font></span> <span><font color="#077807">1</font></span> <span><font color="#1f3f81"><b>:r</b></font></span><span><font color="#912f11">}})</font></span><br /><span><font color="#912f11">(</font></span><span><font color="#912f11">def</font></span> u <span><font color="#912f11">{</font></span><span><font color="#1f3f81"><b>:domain</b></font></span> D <span><font color="#1f3f81"><b>:codomain</b></font></span> U <span><font color="#1f3f81"><b>:rule</b></font></span> <span><font color="#912f11">{</font></span><span><font color="#077807">0</font></span> <span><font color="#1f3f81"><b>:b</b></font></span> <span><font color="#077807">1</font></span> <span><font color="#1f3f81"><b>:b</b></font></span><span><font color="#912f11">}})</font></span><br /></p></font>

In this code, maps in category theory are simply implemented as Clojure's map data structure. So a map in category theory will have three keys in the implementation, a :domain, a :codomain, and a :rule. The first two are sets, and the last one is a function, which defines the actual mapping rule from domain to codomain.

***Article 1, Exercise 2.*** How many different maps $f$ are there with domain $A$ and codomain $B$?

Domain $A$ has 3 elements "John", "Mary" and "Sam", codomain $B$ has 2 elements "eggs" and "coffee". To find the answer, evaluate this in REPL:

CM.core=&gt; (count (all-maps A B))

8

For our domain of 3 elements and codomain of 2 elements, the number of maps is 8, or $2^3$. If we try some other domains (Exercise 3, 4, 5), we will soon discover that the answer is always $$n^m$$ where $n$ and $m$ is the size of codomain and domain, respectively. The reason is simple: each and every element of the domain can pick any one of the elment of codomain as the target. So the first element in the domain has $n$ choices of target, the second can pick $n$ choices as well, and so on, doing this $m$ times, and multipling them all up gives the answer.

***Article 1, Exercise 6.*** How many different maps $A \stackrel{f}{\longrightarrow} A$ satisfy $f \circ f = f$?

Basically, this is asking how many maps are there that composes with itself to get the same results as itself. Such maps are called idempotent maps. The code to find the answer:

CM.core=&gt; (count (idempotent-maps A))

10

Let's try Exercise 7, the number of idempotent maps for $B$:

CM.core=&gt; (count (idempotent-maps B))

3

How about a domain with 4, 5 or 6 elments?

CM.core=&gt; (count (idempotent-maps \#{1 2 3 4}))

41

CM.core=&gt; (count (idempotent-maps \#{1 2 3 4 5}))

196

CM.core=&gt; (count (idempotent-maps \#{1 2 3 4 5 6}))

1057

Hmm, 3, 10, 41, 196, 1057, ... what is the regularity here? It is not obvious. Let's examine the details of the first two maps and look at their rules:

CM.core=&gt; (map :rule (idempotent-maps B))

({"eggs" "coffee", "coffee" "coffee"} {"eggs" "eggs", "coffee" "coffee"} {"eggs" "eggs", "coffee" "eggs"})

CM.core=&gt; (map :rule (idempotent-maps A))

({"Sam" "John", "Mary" "John", "John" "John"} {"Sam" "Sam", "Mary" "John", "John" "John"} {"Sam" "John", "Mary" "Mary", "John" "John"} {"Sam" "Mary", "Mary" "Mary", "John" "John"} {"Sam" "Sam", "Mary" "Mary", "John" "John"} {"Sam" "Sam", "Mary" "Sam", "John" "John"} {"Sam" "Mary", "Mary" "Mary", "John" "Mary"} {"Sam" "Sam", "Mary" "Mary", "John" "Mary"} {"Sam" "Sam", "Mary" "Mary", "John" "Sam"} {"Sam" "Sam", "Mary" "Sam", "John" "Sam"})

The regularity seems to be this: either an element must map to itself, or it must map to an elment that maps to itself. For example, for domain $B$, if "eggs" maps to itself, "coffee" must either map to "coffee" or to "eggs". Cross mappings are not allowed. So "eggs" maps to "coffee" and "coffee" maps to "eggs" is illegal.

Given this regularity, let's work out a formula for the number of idempotent maps. For a 2 element domain, there are two cases: both elements map to themselves, or both map to one element, so the total is ${2 \choose 2} + {2 \choose 1} = 3$; For a 3 element domain, there are three cases: all map to themselves, two map to themselves and the third maps to one of them, or all three map to one, total is ${3 \choose 3} + {3 \choose 2}{2^1} + {3 \choose 1} = 1+ 3\times2 + 3 = 10$; For 4 element domain, four cases: all map to themselves, three map to themselves and the fouth to one of three, two map to themselves and remaining two map to those two, or all map to one: ${4 \choose 4} + {4 \choose 3}{3^1} + {4 \choose 2}{2^2} + {4 \choose 1} = 1 + 4\times3 + 6\times4 + 4 = 41$; and so on... A general formula for the number of idempotent maps emerges, it is $$\sum\limits_{k=0}^n {n \choose k}k^{n-k}$$ Where $n$ is the size of the domain. Notice that we used the results of the previous exercise in the derivation: the number of maps is $|codomain|^{|domain|}$.

***Article 1, Exercise 8.*** Can you find a pair of maps $A \stackrel{f}{\longrightarrow} B \stackrel{g}{\longrightarrow} A$ for which $g \circ f = 1_A$?

OK, this is asking if we can find a pair of maps that compose to an identity map of domain $A$, with the map $B$ in between. Let's see:

CM.core=&gt; (count (composed-solution-pairs B one-a))

0

No such map pair exists, so it is not possible to go through $B$ back to $A$. What about going through $A$ itself?

CM.core=&gt; (count (composed-solution-pairs A one-a))

6

There are 6 such map pairs. It is the same as going through another 3 element domain:

CM.core=&gt; (count (composed-solution-pairs \#{1 2 3} one-a))

6

So when the domains have the same number of elements, it is possible for the map compositions to go through them back and forth. Let's look at the details of these map pairs:

CM.core=&gt; (composed-solution-pairs \#{1 2 3} one-a)

(\[{:rule {3 "Sam", 2 "Mary", 1 "John"}, :domain \#{1 2 3}, :codomain \#{"John" "Mary" "Sam"}} {:rule {"Sam" 3, "Mary" 2, "John" 1}, :domain \#{"John" "Mary" "Sam"}, :codomain \#{1 2 3}}\] \[{:rule {3 "Mary", 2 "Sam", 1 "John"}, :domain \#{1 2 3}, :codomain \#{"John" "Mary" "Sam"}} {:rule {"Sam" 2, "Mary" 3, "John" 1}, :domain \#{"John" "Mary" "Sam"}, :codomain \#{1 2 3}}\] \[{:rule {3 "Sam", 2 "John", 1 "Mary"}, :domain \#{1 2 3}, :codomain \#{"John" "Mary" "Sam"}} {:rule {"Sam" 3, "Mary" 1, "John" 2}, :domain \#{"John" "Mary" "Sam"}, :codomain \#{1 2 3}}\] \[{:rule {3 "Mary", 2 "John", 1 "Sam"}, :domain \#{1 2 3}, :codomain \#{"John" "Mary" "Sam"}} {:rule {"Sam" 1, "Mary" 3, "John" 2}, :domain \#{"John" "Mary" "Sam"}, :codomain \#{1 2 3}}\] \[{:rule {3 "John", 2 "Sam", 1 "Mary"}, :domain \#{1 2 3}, :codomain \#{"John" "Mary" "Sam"}} {:rule {"Sam" 2, "Mary" 1, "John" 3}, :domain \#{"John" "Mary" "Sam"}, :codomain \#{1 2 3}}\] \[{:rule {3 "John", 2 "Mary", 1 "Sam"}, :domain \#{1 2 3}, :codomain \#{"John" "Mary" "Sam"}} {:rule {"Sam" 1, "Mary" 2, "John" 3}, :domain \#{"John" "Mary" "Sam"}, :codomain \#{1 2 3}}\])

Obviously, for each pair, the two map rules are simply the reverse of the another, i.e. flipping the arrows around. If a map has an inverse, it is unique. These maps are called isomorphic, bijective, or one-to-one and onto.

In fact, when the map in the middle has larger size than $A$, there may also be map pairs that compose to the identity of $A$.

CM.core=&gt; (count (composed-solution-pairs \#{1 2 3 4} one-a))

72

In such pairs, each map is called *retraction* and *section* to each other. Let's calculate the number of retractions and sections.

***Article 2, Exercise 5 (1)*** Given map $g$ (see code for its definition), how many maps $f$ are there with $g \circ f = 1_{\{0, 1\}}$?

This is asking the number of sections of the map $g$, which has a 5 element domain $U$, and a 2 element codomain $D$. Three of the elments of $U$, b, p, q, map to 0 in $D$; two elements of $U$, r and s, map to 1 in $D$. The answer can be found by:

CM.core=&gt; (count (section g))

6

Basically, each section $f$ must choose two elements in $U$ to map 0 and 1 to, such that $g$ can map the results back to form an identity map on {0, 1}. For element 0, $f$ can choose one of b, p or q to map to; for element 1, $f$ can choose one of r and s. Therefore, the number of possible $f$ is $2 \times 3 = 6$.

Obviously, not all maps have sections.

CM.core=&gt; (count (section f))

0

To have sections, the map must have a domain size larger than or equal to the codomain size. In addition, each elment of the codomain must be mapped to. Such map property is called surjective or onto. The general formula for the number of sections for map $g$ is therefore $$\prod_{i=1}^{n}m_i$$ where $n$ is the size of the codomain of $g$, and $m_i$ is the number of elements in the domain of $g$ that map to the $i$th element of the codomain.

***Article 2, Exercise 5 (2)*** Choose a particular such $f$ (see code for its definition), how many maps $g$ satisfy $g \circ f = 1_{\{0, 1\}}$?

Given a chosen $f$, this question is asking its number of retractions. The answer is:

CM.core=&gt; (count (retraction f))

8

For given $f$, 0 and 1 each maps to its own element in $U$, its retraction only need to flip the arrows to point back to 0 and 1, the remaining three element in $U$ can freely choose any of 0 and 1 to map to, so the number of retractions is the same as the total number of maps from a 3 element domain to a 2 element codomain, $2^3$. The general formula is $$n^{m-n}$$ where $n$ is the size of domain of $f$, and $m$ is its codomain size. To have retraction, a map must have a domain smaller or equal to the size of its codomain. In addition, it must be a one-to-one mapping, also called injective mapping.

***Number of section-retraction pairs*** On page 117 of the book, the above formula for the number of retractions and sections of a given map are given, but it also says that the formula for the number of pairs of section/retraction in term of $m$ and $n$ is rather complicated. As it turns out, it is simple to derive a formula that is not complicated at all. First, each element of the smaller domain (size $n$) must map injectively to the lager domain (size $m$), the number of possibilities is just the number of permutation of choosing $n$ out of $m$. Then the remaining $m-n$ in the larger domain can freely choose any of the $n$ to map back to. Finally, we time up the two terms to arrive at $$\frac{m!}{(m-n)!}n^{m-n}$$ where $n$ is the size of domain $A$, m is the size of the domain $X$, $n \le m$, and $A \stackrel{s}{\longrightarrow} X \stackrel{r}{\longrightarrow} A$ satisfy $r \circ s = 1_A$.

The formula seem to be correct as verified by the code:

CM.core=&gt; (count (retraction-section-pairs \#{1 2} \#{:a}))

0

CM.core=&gt;(count (retraction-section-pairs \#{1} \#{:a}))

1

CM.core=&gt; (count (retraction-section-pairs \#{1 2} \#{:a :b}))

2

CM.core=&gt; (count (retraction-section-pairs \#{1 2} \#{:a :b}))

2

CM.core=&gt; (count (retraction-section-pairs \#{1 2} \#{:a :b :c}))

12

CM.core=&gt; (count (retraction-section-pairs \#{1 2} \#{:a :b :c :d :e}))

160

CM.core=&gt; (count (retraction-section-pairs \#{1 2 3} \#{:a :b :c}))

6

CM.core=&gt; (count (retraction-section-pairs \#{1 2 3} \#{:a :b :c :d}))

72

CM.core=&gt; (count (retraction-section-pairs \#{1 2 3 4} \#{:a :b :c :d}))

24

CM.core=&gt; (count (retraction-section-pairs \#{1 2 3 4} \#{:a :b :c :d :e}))

480

CM.core=&gt; (count (retraction-section-pairs \#{1 2 3 4 5} \#{:a :b :c :d :e}))

120

CM.core=&gt; (count (retraction-section-pairs \#{1 2 3 4} \#{:a :b :c :d :e :f}))

5760

CM.core=&gt; (count (retraction-section-pairs \#{1 2 3 4 5} \#{:a :b :c :d :e :f}))

3600

Don't try the last two function calls, as they will run a long long time.
