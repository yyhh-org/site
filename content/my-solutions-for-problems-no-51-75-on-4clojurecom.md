---
Title: My solutions for problems No. 51-75 on 4clojure.com
Date: 2011-05-25 01:59
Author: Huahai
Category: notebook
Tags: Programming, Clojure
Slug: my-solutions-for-problems-no-51-75-on-4clojurecom
Alias: /blog/2011/05/my-solutions-problems-no-51-75-4clojure-com
Series: 4clojure-solutions
Lang: en
---

This post continues the [previous one](https://yyhh.org/blog/2011/05/my-solutions-first-50-problems-4clojure-com), on my solutions for small clojure programming problems on [4clojure.com](https://www.4clojure.com). Doing these problems seems to be addictive as I could not seem to stop myself. The site recently added a golf league feature, so one can see how short one's own solution compared with others. If a lot of people got a much shorter solution than yours, you know you are not thinking in the right way. This little competition makes the site even more attractive. Anyhow, the code is here:

<font face="monospace">  
<font color="#786000">; 53: Given a vector of integers, find the longest consecutive sub-sequence of</font>  
<font color="#786000">; increasing numbers.  If two sub-sequences have the same length, use the one </font>  
<font color="#786000">; that occurs first. An increasing sub-sequence must have a length of 2 or </font>  
<font color="#786000">; greater to qualify.</font>  
<font color="#786000">; (= (\_\_ \[1 0 1 2 3 0 4 5\]) \[0 1 2 3\])</font>  
<font color="#786000">; (= (\_\_ \[7 6 5 4\]) \[\])</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>coll<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#800090">-&gt;&gt;</font> <font color="#ee9a00">(</font><font color="#007080">partition</font> <font color="#077807">2</font> <font color="#077807">1</font> coll<font color="#ee9a00">)</font>   
    <font color="#ee9a00">(</font><font color="#007080">partition-by</font> <font color="#912f11">\#(</font><font color="#007080">-</font> <font color="#912f11">(</font><font color="#007080">second</font> %<font color="#912f11">)</font> <font color="#912f11">(</font><font color="#007080">first</font> %<font color="#912f11">))</font><font color="#ee9a00">)</font>   
    <font color="#ee9a00">(</font><font color="#1f3f81">**filter**</font> <font color="#912f11">\#(</font><font color="#007080">=</font> <font color="#077807">1</font> <font color="#912f11">(</font><font color="#007080">-</font> <font color="#cd3700">(</font><font color="#007080">second</font> <font color="#ee9a00">(</font><font color="#007080">first</font> %<font color="#ee9a00">)</font><font color="#cd3700">)</font> <font color="#cd3700">(</font><font color="#007080">ffirst</font> %<font color="#cd3700">)</font><font color="#912f11">))</font><font color="#ee9a00">)</font>   
    <font color="#ee9a00">(</font><font color="#1f3f81">**reduce**</font> <font color="#912f11">\#(</font><font color="#912f11">if</font> <font color="#912f11">(</font><font color="#007080">&lt;</font> <font color="#cd3700">(</font><font color="#007080">count</font> %<font color="#077807">1</font><font color="#cd3700">)</font> <font color="#cd3700">(</font><font color="#007080">count</font> %<font color="#077807">2</font><font color="#cd3700">)</font><font color="#912f11">)</font> <font color="#912f11">%2</font> <font color="#912f11">%1</font><font color="#912f11">)</font> <font color="#912f11">\[\]</font><font color="#ee9a00">)</font>  
    <font color="#007080">flatten</font>  
    <font color="#007080">distinct</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; we first create a list of neighoring pairs, partition them by their pair </font>  
<font color="#786000">; differences, keep those with difference 1, finally return the longest one</font>

<font color="#786000">; 54: Write a function which returns a sequence of lists of x items each. </font>  
<font color="#786000">; Lists of less than x items should not be returned. </font>  
<font color="#786000">; (= (\_\_ 3 (range 8)) '((0 1 2) (3 4 5))) </font>  
<font color="#786000">; forbidden: partition, partition-all</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> partition2 <font color="#912f11">\[</font>n coll<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#1f3f81">**when**</font> <font color="#ee9a00">(</font><font color="#007080">&lt;=</font> n <font color="#cdcd00">(</font><font color="#007080">count</font> coll<font color="#cdcd00">)</font><font color="#ee9a00">)</font>  
    <font color="#ee9a00">(</font><font color="#007080">cons</font> <font color="#cdcd00">(</font><font color="#007080">take</font> n coll<font color="#cdcd00">)</font> <font color="#cdcd00">(</font>partition2 n <font color="#698b22">(</font><font color="#007080">drop</font> n coll<font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; we recursively take n items till not enough items</font>

<font color="#786000">; 55: Write a function that returns a map containing the number of occurences </font>  
<font color="#786000">; of each distinct item in a sequence.</font>  
<font color="#786000">; (= (\_\_ \[1 1 2 3 2 1 1\]) {1 4, 2 2, 3 1})</font>  
<font color="#786000">; forbidden: frequencies</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>coll<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>gp <font color="#912f11">(</font><font color="#007080">group-by</font> <font color="#007080">identity</font> coll<font color="#912f11">)\]</font>   
    <font color="#ee9a00">(</font><font color="#007080">zipmap</font> <font color="#cdcd00">(</font><font color="#007080">keys</font> gp<font color="#cdcd00">)</font> <font color="#cdcd00">(</font><font color="#1f3f81">**map**</font> <font color="#912f11">\#(</font><font color="#007080">count</font> <font color="#912f11">(</font><font color="#007080">second</font> %<font color="#912f11">))</font> gp<font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; note a map entry is just a two item vector, first item is the key, the</font>  
<font color="#786000">; second item is the value</font>

<font color="#786000">; 56: Write a function which removes the duplicates from a sequence. Order of </font>  
<font color="#786000">; the items must be maintained.</font>  
<font color="#786000">; (= (\_\_ \[1 2 1 3 1 2 4\]) \[1 2 3 4\])</font>  
<font color="#786000">; forbidden: distinct</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>coll<font color="#912f11">\]</font>   
  <font color="#cd3700">(</font><font color="#ee9a00">(</font><font color="#912f11">fn</font> step <font color="#912f11">\[\[</font>x <font color="#912f11">&</font> xs<font color="#912f11">\]</font> seen<font color="#912f11">\]</font>   
     <font color="#cdcd00">(</font><font color="#1f3f81">**when**</font> x  
       <font color="#698b22">(</font><font color="#912f11">if</font> <font color="#008b00">(</font>seen x<font color="#008b00">)</font>   
         <font color="#008b00">(</font>step xs seen<font color="#008b00">)</font>  
         <font color="#008b00">(</font><font color="#007080">cons</font> x <font color="#96cdcd">(</font>step xs <font color="#00688b">(</font><font color="#007080">conj</font> seen x<font color="#00688b">)</font><font color="#96cdcd">)</font><font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font>   
   coll <font color="#912f11">\#{}</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; we recursively go through the sequence, use a set to keep track of items </font>  
<font color="#786000">; we've seen, only return those we have not seen before. </font>  
  

<font color="#786000">; 58: Write a function which allows you to create function compositions. The </font>  
<font color="#786000">; parameter list should take a variable number of functions, and create a </font>  
<font color="#786000">; function applies them from right-to-left.</font>  
<font color="#786000">; (= \[3 2 1\] ((\_\_ rest reverse) \[1 2 3 4\]))</font>  
<font color="#786000">; forbidden: comp</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>x <font color="#912f11">&</font> xs<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font><font color="#912f11">&</font> args<font color="#912f11">\]</font>  
    <font color="#ee9a00">(</font><font color="#cdcd00">(</font><font color="#912f11">fn</font> step <font color="#912f11">\[\[</font>f <font color="#912f11">&</font> fs<font color="#912f11">\]</font> a<font color="#912f11">\]</font>  
       <font color="#698b22">(</font><font color="#912f11">if</font> fs  
         <font color="#008b00">(</font>f <font color="#96cdcd">(</font>step fs a<font color="#96cdcd">)</font><font color="#008b00">)</font>  
         <font color="#008b00">(</font><font color="#007080">apply</font> f a<font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font>  
     <font color="#cdcd00">(</font><font color="#007080">cons</font> x xs<font color="#cdcd00">)</font> args<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; step function takes the function list and the arguments, recursively builds</font>  
<font color="#786000">; an ever deeper call stack till at the end of the list, where the right most </font>  
<font color="#786000">; function is called with the given arguments.</font>  
    

<font color="#786000">; 59: Take a set of functions and return a new function that takes a variable </font>  
<font color="#786000">; number of arguments and returns sequence containing the result of applying </font>  
<font color="#786000">; each function left-to-right to the argument list.</font>  
<font color="#786000">; (= \[21 6 1\] ((\_\_ + max min) 2 3 5 1 6 4))</font>  
<font color="#786000">; forbidden: juxt</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>x <font color="#912f11">&</font> xs<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font><font color="#912f11">&</font> args<font color="#912f11">\]</font>  
    <font color="#ee9a00">(</font><font color="#1f3f81">**map**</font> <font color="#912f11">\#(</font><font color="#007080">apply</font> <font color="#912f11">%</font> args<font color="#912f11">)</font> <font color="#cdcd00">(</font><font color="#007080">cons</font> x xs<font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>

<font color="#786000">; 60: Write a function which behaves like reduce, but returns each </font>  
<font color="#786000">; intermediate value of the reduction. Your function must accept either two </font>  
<font color="#786000">; or three arguments, and the return sequence must be lazy.</font>  
<font color="#786000">; (= (take 5 (\_\_ + (range))) \[0 1 3 6 10\])</font>  
<font color="#786000">; (= (\_\_ conj \[1\] \[2 3 4\]) \[\[1\] \[1 2\] \[1 2 3\] \[1 2 3 4\]\])</font>  
<font color="#786000">; forbidden: reductions</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> reductions2  
  <font color="#cd3700">(</font><font color="#912f11">\[</font>f init <font color="#912f11">\[</font>x <font color="#912f11">&</font> xs<font color="#912f11">\]\]</font>   
   <font color="#ee9a00">(</font><font color="#007080">cons</font> init <font color="#cdcd00">(</font><font color="#800090">lazy-seq</font> <font color="#698b22">(</font><font color="#1f3f81">**when**</font> x <font color="#008b00">(</font>reductions2 f <font color="#96cdcd">(</font>f init x<font color="#96cdcd">)</font> xs<font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font>   
  <font color="#cd3700">(</font><font color="#912f11">\[</font>f coll<font color="#912f11">\]</font>   
   <font color="#ee9a00">(</font>reductions2 f <font color="#cdcd00">(</font><font color="#007080">first</font> coll<font color="#cdcd00">)</font> <font color="#cdcd00">(</font><font color="#007080">rest</font> coll<font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>

<font color="#786000">; 61: Write a function which takes a vector of keys and a vector of values </font>  
<font color="#786000">; and constructs a map from them.</font>  
<font color="#786000">; (= (\_\_ \[:a :b :c\] \[1 2 3\]) {:a 1, :b 2, :c 3})</font>  
<font color="#786000">; forbidden: zipmap</font>  
<font color="#912f11">\#(</font><font color="#007080">into</font> <font color="#912f11">{}</font> <font color="#912f11">(</font><font color="#1f3f81">**map**</font> <font color="#007080">vector</font> %<font color="#077807">1</font> %<font color="#077807">2</font><font color="#912f11">))</font>

<font color="#786000">; 62. Given a side-effect free function f and an initial value x </font>  
<font color="#786000">; write a function which returns an infinite lazy sequence of x,</font>  
<font color="#786000">; (f x), (f (f x)), (f (f (f x))), etc.  </font>  
<font color="#786000">; (= (take 5 (\_\_ \#(\* 2 %) 1)) \[1 2 4 8 16\])</font>  
<font color="#786000">; forbidden: iterate</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> iterate2 <font color="#912f11">\[</font>f x<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#007080">cons</font> x <font color="#ee9a00">(</font><font color="#800090">lazy-seq</font> <font color="#cdcd00">(</font>iterate2 f <font color="#698b22">(</font>f x<font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; it turns out that clojure's own implmentation is the same </font>

<font color="#786000">; 63. Given a function f and a sequence s, write a function which returns a </font>  
<font color="#786000">; map. The keys should be the values of f applied to each item in s. The value</font>  
<font color="#786000">; at each key should be a vector of corresponding items in the order they </font>  
<font color="#786000">; appear in s.</font>  
<font color="#786000">; (= (\_\_ \#(&gt; % 5) \#{1 3 6 8}) {false \[1 3\], true \[6 8\]})</font>  
<font color="#786000">; forbidden group-by</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>f s<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#ee9a00">(</font><font color="#912f11">fn</font> step <font color="#912f11">\[</font>ret f <font color="#912f11">\[</font>x <font color="#912f11">&</font> xs<font color="#912f11">\]\]</font>  
     <font color="#cdcd00">(</font><font color="#912f11">if</font> x  
       <font color="#698b22">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>k <font color="#912f11">(</font>f x<font color="#912f11">)\]</font>  
         <font color="#008b00">(</font>step <font color="#96cdcd">(</font><font color="#007080">assoc</font> ret k <font color="#00688b">(</font><font color="#007080">conj</font> <font color="#483d8b">(</font><font color="#007080">get</font> ret k <font color="#912f11">\[\]</font><font color="#483d8b">)</font> x<font color="#00688b">)</font><font color="#96cdcd">)</font> f xs<font color="#008b00">)</font><font color="#698b22">)</font>  
       ret<font color="#cdcd00">)</font><font color="#ee9a00">)</font>  
    <font color="#912f11">{}</font> f <font color="#ee9a00">(</font><font color="#007080">seq</font> s<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; the get function takes a default argument for when the key is not found,</font>  
<font color="#786000">; which is used to initialize a vector here. Note the use of seq for s, as</font>  
<font color="#786000">; the collection may be a set, where the \[x & xs\] destructering doesn't work.</font>  
<font color="#786000">; Intead of recursively going over a sequence, we can also use reduce:</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>f s<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#1f3f81">**reduce**</font>   
    <font color="#ee9a00">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>ret x<font color="#912f11">\]</font>  
      <font color="#cdcd00">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>k <font color="#912f11">(</font>f x<font color="#912f11">)\]</font>  
        <font color="#698b22">(</font><font color="#007080">assoc</font> ret k <font color="#008b00">(</font><font color="#007080">conj</font> <font color="#96cdcd">(</font><font color="#007080">get</font> ret k <font color="#912f11">\[\]</font><font color="#96cdcd">)</font> x<font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font>  
    <font color="#912f11">{}</font> s<font color="#cd3700">)</font><font color="#912f11">)</font>

<font color="#786000">; 65: Write a function which takes a collection and returns one of :map, :set,</font>  
<font color="#786000">; :list, or :vector - describing the type of collection it was given. </font>  
<font color="#786000">; (= :map (\_\_ {:a 1, :b 2}))</font>  
<font color="#786000">; forbidden: class, type, Class, vector?, sequential?, list?, seq?, map?, set?</font>  
<font color="#786000">; instance? getClass</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>coll<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>x <font color="#912f11">(</font><font color="#007080">rand-int</font> <font color="#077807">100</font><font color="#912f11">)</font> y <font color="#912f11">(</font><font color="#007080">rand-int</font> <font color="#077807">100</font><font color="#912f11">)</font>   
        p <font color="#912f11">\[</font>x y<font color="#912f11">\]</font> c <font color="#912f11">(</font><font color="#007080">conj</font> coll z<font color="#912f11">)\]</font>  
    <font color="#ee9a00">(</font><font color="#1f3f81">**cond**</font>   
      <font color="#cdcd00">(</font><font color="#007080">=</font> y <font color="#698b22">(</font><font color="#007080">get</font> c x<font color="#698b22">)</font><font color="#cdcd00">)</font> <font color="#1f3f81">**:map**</font>  
      <font color="#cdcd00">(</font><font color="#007080">=</font> p <font color="#698b22">(</font><font color="#007080">get</font> c p<font color="#698b22">)</font><font color="#cdcd00">)</font> <font color="#1f3f81">**:set**</font>  
      <font color="#cdcd00">(</font><font color="#007080">=</font> x <font color="#698b22">(</font><font color="#007080">last</font> <font color="#008b00">(</font><font color="#007080">conj</font> c x<font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font> <font color="#1f3f81">**:vector**</font>  
      <font color="#1f3f81">**:else**</font> <font color="#1f3f81">**:list**</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; we conj a random two element vector into the collection, map will treat it </font>  
<font color="#786000">; as a new key value pair, others treat it as a single item; set is a map too,</font>  
<font color="#786000">; so we can get the vector back with itself as the key; vector and list are </font>  
<font color="#786000">; differentiated by the position of the conj.</font>

<font color="#786000">; 67: Write a function which returns the first x number of prime numbers. </font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>x<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#007080">take</font> x  
        <font color="#ee9a00">(</font><font color="#007080">remove</font>   
          <font color="#cdcd00">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>n<font color="#912f11">\]</font>   
            <font color="#698b22">(</font><font color="#007080">some</font> <font color="#912f11">\#(</font><font color="#007080">=</font> <font color="#077807">0</font> <font color="#912f11">(</font><font color="#007080">mod</font> n %<font color="#912f11">))</font> <font color="#008b00">(</font><font color="#007080">range</font> <font color="#077807">2</font> <font color="#96cdcd">(</font><font color="#007080">inc</font> <font color="#00688b">(</font><font color="#007080">int</font> <font color="#483d8b">(</font>Math/sqrt n<font color="#483d8b">)</font><font color="#00688b">)</font><font color="#96cdcd">)</font><font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font>  
          <font color="#cdcd00">(</font><font color="#007080">iterate</font> <font color="#007080">inc</font> <font color="#077807">2</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; we just test each number n, each divided by numbers from 2 up to sqrt(n)</font>

<font color="#786000">; 69: Write a function which takes a function f and a variable number of maps.</font>  
<font color="#786000">; Your function should return a map that consists of the rest of the maps </font>  
<font color="#786000">; conj-ed onto the first. If a key occurs in more than one map, the mapping(s)</font>  
<font color="#786000">; from the latter (left-to-right) should be combined with the mapping in the </font>  
<font color="#786000">; result by calling (f val-in-result val-in-latter)</font>  
<font color="#786000">; (= (\_\_ - {1 10, 2 20} {1 3, 2 10, 3 15}) {1 7, 2 10, 3 15})</font>  
<font color="#786000">; forbidden: merge-with</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>f m <font color="#912f11">&</font> ms<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#1f3f81">**reduce**</font>   
    <font color="#ee9a00">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>ret x<font color="#912f11">\]</font>  
      <font color="#cdcd00">(</font><font color="#1f3f81">**reduce**</font>   
        <font color="#698b22">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>r k<font color="#912f11">\]</font>   
          <font color="#008b00">(</font><font color="#007080">conj</font> r <font color="#96cdcd">(</font><font color="#912f11">if</font> <font color="#00688b">(</font>r k<font color="#00688b">)</font> <font color="#912f11">\[</font>k <font color="#912f11">(</font>f <font color="#cd3700">(</font>r k<font color="#cd3700">)</font> <font color="#cd3700">(</font>x k<font color="#cd3700">)</font><font color="#912f11">)\]</font> <font color="#00688b">(</font><font color="#007080">find</font> x k<font color="#00688b">)</font><font color="#96cdcd">)</font><font color="#008b00">)</font><font color="#698b22">)</font>   
        ret <font color="#698b22">(</font><font color="#007080">keys</font> x<font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font>   
    <font color="#ee9a00">(</font><font color="#007080">cons</font> m ms<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; note a map is a function itself, so (r k) and (x k) works</font>

<font color="#786000">; 70: Write a function which splits a sentence up into a sorted list of words.</font>  
<font color="#786000">; Capitalization should not affect sort order and punctuation should be ignored</font>  
<font color="#786000">; (= (\_\_  "Have a nice day.") \["a" "day" "Have" "nice"\])</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>s<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#007080">sort-by</font> <font color="#912f11">\#(</font>.toLowerCase <font color="#912f11">%</font><font color="#912f11">)</font> <font color="#ee9a00">(</font><font color="#007080">re-seq</font> <font color="#077807">\#"\\w+"</font> s<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>

<font color="#786000">; 73: A tic-tac-toe board is represented by a two dimensional vector. X is </font>  
<font color="#786000">; represented by :x, O is represented by :o, and empty is represented by :e. A </font>  
<font color="#786000">; player wins by placing three Xs or three Os in a horizontal, vertical, or </font>  
<font color="#786000">; diagonal row. Write a function which analyzes a tic-tac-toe board and returns</font>  
<font color="#786000">; :x if X has won, :o if O has won, and nil if neither player has won.</font>  
<font color="#786000">; (= nil (\_\_ \[\[:e :e :e\]</font>  
            <font color="#786000">;\[:e :e :e\]</font>  
            <font color="#786000">;\[:e :e :e\]\]))</font>  
<font color="#786000">;(= :x (\_\_ \[\[:x :e :o\]</font>  
           <font color="#786000">;\[:x :e :e\]</font>  
           <font color="#786000">;\[:x :e :o\]\]))</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>board<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>i <font color="#912f11">\[</font><font color="#077807">0</font> <font color="#077807">1</font> <font color="#077807">2</font><font color="#912f11">\]</font>  
        c <font color="#912f11">(</font><font color="#007080">take</font> <font color="#077807">12</font> <font color="#cd3700">(</font><font color="#007080">cycle</font> i<font color="#cd3700">)</font><font color="#912f11">)</font>  
        p <font color="#912f11">(</font><font color="#007080">flatten</font> <font color="#cd3700">(</font><font color="#1f3f81">**map**</font> <font color="#912f11">\#(</font><font color="#007080">repeat</font> <font color="#077807">3</font> <font color="#912f11">%</font><font color="#912f11">)</font> i<font color="#cd3700">)</font><font color="#912f11">)</font>  
        zip <font color="#912f11">\#(</font><font color="#1f3f81">**map**</font> <font color="#007080">vector</font> <font color="#912f11">%1</font> <font color="#912f11">%2</font><font color="#912f11">)</font>  
        win? <font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>w<font color="#912f11">\]</font>   
               <font color="#cd3700">(</font><font color="#007080">some</font>   
                 <font color="#ee9a00">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>x<font color="#912f11">\]</font> <font color="#cdcd00">(</font><font color="#007080">every?</font> <font color="#912f11">\#(</font><font color="#007080">=</font> w <font color="#912f11">(</font><font color="#007080">get-in</font> board %<font color="#912f11">))</font> x<font color="#cdcd00">)</font><font color="#ee9a00">)</font>   
                 <font color="#ee9a00">(</font><font color="#007080">partition</font>   
                   <font color="#077807">3</font> <font color="#cdcd00">(</font><font color="#007080">into</font> <font color="#698b22">(</font>zip <font color="#008b00">(</font><font color="#007080">into</font> i p<font color="#008b00">)</font> c<font color="#698b22">)</font> <font color="#698b22">(</font>zip c <font color="#008b00">(</font><font color="#007080">into</font> <font color="#96cdcd">(</font><font color="#007080">reverse</font> i<font color="#96cdcd">)</font> p<font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)\]</font>  
    <font color="#ee9a00">(</font><font color="#1f3f81">**cond**</font>   
      <font color="#cdcd00">(</font>win? <font color="#1f3f81">**:x**</font><font color="#cdcd00">)</font> <font color="#1f3f81">**:x**</font>  
      <font color="#cdcd00">(</font>win? <font color="#1f3f81">**:o**</font><font color="#cdcd00">)</font> <font color="#1f3f81">**:o**</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; we basically enumerate all possible winning positions, which fall into</font>  
<font color="#786000">; some regular patterns. I am sure there are better ways, but in the </font>  
<font color="#786000">; interest of time... Note the use of get-in to fetech value in a multiple </font>  
<font color="#786000">; dimensional vector: (get-in board \[x y\])</font>

<font color="#786000">; 74: Given a string of comma separated integers, write a function which </font>  
<font color="#786000">; returns a new comma separated string that only contains the numbers </font>  
<font color="#786000">; which are perfect squares.</font>  
<font color="#786000">; (= (\_\_ "4,5,6,7,8,9") "4,9")</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>s<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#800090">-&gt;&gt;</font> <font color="#ee9a00">(</font><font color="#007080">re-seq</font> <font color="#077807">\#"\\d+"</font> s<font color="#ee9a00">)</font>  
    <font color="#ee9a00">(</font><font color="#1f3f81">**map**</font> <font color="#912f11">\#(</font>Integer/parseInt <font color="#912f11">%</font><font color="#912f11">)</font><font color="#ee9a00">)</font>  
    <font color="#ee9a00">(</font><font color="#1f3f81">**filter**</font> <font color="#cdcd00">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>x<font color="#912f11">\]</font>  
              <font color="#698b22">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>r <font color="#912f11">(</font><font color="#007080">int</font> <font color="#cd3700">(</font>Math/sqrt x<font color="#cd3700">)</font><font color="#912f11">)\]</font>  
                <font color="#008b00">(</font><font color="#007080">=</font> x <font color="#96cdcd">(</font><font color="#007080">\*</font> r r<font color="#96cdcd">)</font><font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font>  
    <font color="#ee9a00">(</font><font color="#007080">interpose</font> <font color="#077807">","</font><font color="#ee9a00">)</font>  
    <font color="#ee9a00">(</font><font color="#007080">apply</font> <font color="#007080">str</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>

<font color="#786000">; 75: Two numbers are coprime if their greatest common divisor equals 1. </font>  
<font color="#786000">; Euler's totient function f(x) is defined as the number of positive integers </font>  
<font color="#786000">; less than x which are coprime to x. The special case f(1) equals 1. Write a </font>  
<font color="#786000">; function which calculates Euler's totient function.</font>  
<font color="#786000">; (= (\_\_ 10) (count '(1 3 7 9)) 4)</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>n<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#800090">-&gt;&gt;</font> <font color="#ee9a00">(</font><font color="#007080">range</font> <font color="#077807">2</font> n<font color="#ee9a00">)</font>  
    <font color="#ee9a00">(</font><font color="#1f3f81">**filter**</font> <font color="#cdcd00">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>x<font color="#912f11">\]</font>  
              <font color="#698b22">(</font><font color="#007080">=</font> <font color="#077807">1</font> <font color="#008b00">(</font><font color="#96cdcd">(</font><font color="#912f11">fn</font> gcd <font color="#912f11">\[</font>a b<font color="#912f11">\]</font>  
                      <font color="#00688b">(</font><font color="#912f11">if</font> <font color="#483d8b">(</font><font color="#007080">=</font> <font color="#077807">0</font> b<font color="#483d8b">)</font> a <font color="#483d8b">(</font>gcd b <font color="#9400d3">(</font><font color="#007080">mod</font> a b<font color="#9400d3">)</font><font color="#483d8b">)</font><font color="#00688b">)</font><font color="#96cdcd">)</font>  
                    x n<font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font>  
    <font color="#007080">count</font>  
    <font color="#007080">inc</font><font color="#cd3700">)</font><font color="#912f11">)</font>

</font>
