---
Title: My solutions for the first 50 problems on 4clojure.com
Date: 2011-05-18 23:13
Author: Huahai
Category: notebook
Tags: Programming, Clojure
Slug: my-solutions-for-the-first-50-problems-on-4clojurecom
Alias: /blog/2011/05/my-solutions-first-50-problems-4clojure-com
Series: 4clojure-solutions
Lang: en
---

For someone without previous Lisp experience, the hardest part of learning [Clojure](https://clojure.org) programming seems to be the functional way of doing things. It is like math, one really needs to do some exercises in order to master it. At this point, [4clojure.com](https://www.4clojure.com) seems to be the best place for getting such exercises. It has a lot of problems for new clojurians to solve. These problems ask one to fill in the blank \_\_ so the given expressions are true. To give a little challenge, some clojure built-in functions are forbidden to use for some problems. New problems are added from time to time on the site, so it surely can keep me entertained for a while.

I just finished the first 50 problems and think it might be helpful to post the solutions here. I tried to be functional and avoided using loops in the code. Some solutions are skipped as they seem trivial even for a functional newbie like myself. My solutions are probably just awful, but it is a fun experience nevertheless. I will post more solutions when I am done with them (Solutions [No.50-75](https://yyhh.org/blog/2011/05/my-solutions-problems-no-51-75-4clojure-com) and [76-100](https://yyhh.org/blog/2011/06/my-solutions-problems-no-76-100-4clojure-com)) Update: there are better solutions for problem 21, 27 and 44, contributed by visitors to the old site. But those comments are lost during system switch over. 

<font face="monospace"><font color="#786000">; 21: Write a function which returns the Nth element from a sequence.</font>  
<font color="#786000">; (= (\_\_ '(4 5 6 7) 2) 6)</font>  
<font color="#786000">; forbidden: nth</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>coll n<font color="#912f11">\]</font>   
  <font color="#cd3700">(</font><font color="#ee9a00">(</font><font color="#007080">apply</font> <font color="#007080">comp</font> <font color="#cdcd00">(</font><font color="#007080">cons</font> <font color="#007080">first</font> <font color="#698b22">(</font><font color="#007080">repeat</font> n <font color="#007080">rest</font><font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font> coll<font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; We first compose n rest functions to get progressively shorter lists </font></font>

<font face="monospace"><font color="#786000">; till the </font><font color="#786000">desired element is the head, then take the head. A less </font></font>

<font face="monospace"><font color="#786000">; </font></font><font face="monospace"><font color="#786000">fancy version just </font><font color="#786000">uses nthnext, but it feels like cheating:</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>coll n<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#007080">first</font> <font color="#ee9a00">(</font><font color="#007080">nthnext</font> coll n<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font></font>

 

<font face="monospace"><font color="#786000">; 22: Write a function which returns the total number of elements in </font></font>

<font face="monospace"><font color="#786000">; a sequence.</font>  
<font color="#786000">; (= (\_\_ '(1 2 3 3 1)) 5)</font>  
<font color="#786000">; forbidden: count</font>  
<font color="#912f11">\#(</font><font color="#1f3f81">**reduce**</font> <font color="#007080">+</font> <font color="#912f11">(</font><font color="#1f3f81">**map**</font> <font color="#cd3700">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>x<font color="#912f11">\]</font> <font color="#077807">1</font><font color="#cd3700">)</font> %<font color="#912f11">))</font>  
<font color="#786000">; We just turn each element into 1 and then add them up</font>  
<font color="#786000">; Note that (fn \[x\] 1) can be replaced by (constantly 1)</font></font>

 

<font face="monospace"><font color="#786000">; 23: Write a function which reverses a sequence.</font>  
<font color="#786000">; (= (\_\_ \[1 2 3 4 5\]) \[5 4 3 2 1\])</font>  
<font color="#786000">; forbidden: reverse</font>  
<font color="#912f11">\#(</font><font color="#007080">into</font> <font color="#912f11">()</font> <font color="#912f11">%</font><font color="#912f11">)</font>  
<font color="#786000">; We exploit the property of the list, which alway add new element </font>  
<font color="#786000">; in front of the head. Also that the clojure sequences' equality</font>  
<font color="#786000">; evaluation is element based, so \[1 2 3\] equals to '(1 2 3)</font></font>

 

<font face="monospace"><font color="#786000">; 26: Write a function which returns the first X fibonacci numbers.</font>  
<font color="#786000">; (= (\_\_ 6) '(1 1 2 3 5 8))</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>x<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#007080">take</font> x  
    <font color="#ee9a00">(</font><font color="#cdcd00">(</font><font color="#912f11">fn</font> fib <font color="#912f11">\[</font>a b<font color="#912f11">\]</font>  
        <font color="#698b22">(</font><font color="#007080">cons</font> a <font color="#008b00">(</font><font color="#800090">lazy-seq</font> <font color="#96cdcd">(</font>fib b <font color="#00688b">(</font><font color="#007080">+</font> a b<font color="#00688b">)</font><font color="#96cdcd">)</font><font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font>   
      <font color="#077807">1</font> <font color="#077807">1</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>   
<font color="#786000">; we first recursively construct a lazy sequence of infinite number of </font>  
<font color="#786000">; fibonacci numbers</font></font>

 

<font face="monospace"><font color="#786000">; 27: Write a function which returns true if the given sequence is</font></font>

<font face="monospace"><font color="#786000">; a palindrome.</font>  
<font color="#786000">; (true? (\_\_ '(1 1 3 3 1 1))) </font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>coll<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>rc <font color="#912f11">(</font><font color="#007080">reverse</font> coll<font color="#912f11">)</font> n <font color="#912f11">(</font><font color="#007080">count</font> coll<font color="#912f11">)\]</font>  
    <font color="#ee9a00">(</font><font color="#007080">every?</font> <font color="#007080">identity</font>   
      <font color="#cdcd00">(</font><font color="#1f3f81">**map**</font> <font color="#912f11">\#(</font><font color="#007080">=</font> <font color="#912f11">(</font><font color="#007080">nth</font> coll %<font color="#912f11">)</font> <font color="#912f11">(</font><font color="#007080">nth</font> rc %<font color="#912f11">))</font> <font color="#698b22">(</font><font color="#007080">range</font> <font color="#008b00">(</font><font color="#007080">/</font> <font color="#96cdcd">(</font><font color="#007080">dec</font> n<font color="#96cdcd">)</font> <font color="#077807">2</font><font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; we naively compare half of the pairs of elment e(i) and e(n-i-1)</font></font>

 

<font face="monospace"><font color="#786000">; 28: Write a function which flattens a sequence.</font>  
<font color="#786000">; (= (\_\_ '((1 2) 3 \[4 \[5 6\]\])) '(1 2 3 4 5 6)) </font>  
<font color="#786000">; forbidden: flatten</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> flt <font color="#912f11">\[</font>coll<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>l <font color="#912f11">(</font><font color="#007080">first</font> coll<font color="#912f11">)</font> r <font color="#912f11">(</font><font color="#007080">next</font> coll<font color="#912f11">)\]</font>  
    <font color="#ee9a00">(</font><font color="#007080">concat</font>   
      <font color="#cdcd00">(</font><font color="#912f11">if</font> <font color="#698b22">(</font><font color="#007080">sequential?</font> l<font color="#698b22">)</font>  
        <font color="#698b22">(</font>flt l<font color="#698b22">)</font>  
        <font color="#912f11">\[</font>l<font color="#912f11">\]</font><font color="#cdcd00">)</font>  
      <font color="#cdcd00">(</font><font color="#1f3f81">**when**</font> <font color="#698b22">(</font><font color="#007080">sequential?</font> r<font color="#698b22">)</font>  
        <font color="#698b22">(</font>flt r<font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; we basically treat the nested collection as a tree and recursively </font></font>

<font face="monospace"><font color="#786000">; walk the </font><font color="#786000">tree. Clojure's flatten use a tree-seq to walk the tree.</font></font>

 

<font face="monospace"><font color="#786000">; 29: Write a function which takes a string and returns a new </font></font>

<font face="monospace"><font color="#786000">; string containing</font><font color="#786000"> only the capital letters.</font>  
<font color="#786000">; (= (\_\_ "HeLlO, WoRlD!") "HLOWRD")    </font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>coll<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#007080">apply</font> <font color="#007080">str</font> <font color="#ee9a00">(</font><font color="#1f3f81">**filter**</font> <font color="#912f11">\#(</font>Character/isUpperCase <font color="#912f11">%</font><font color="#912f11">)</font> coll<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; note the use of apply here, as str takes a number of args instead</font>  
<font color="#786000">; of a character collection</font></font>

 

<font face="monospace"><font color="#786000">; 30: Write a function which removes consecutive duplicates from a sequence.</font>  
<font color="#786000">;  (= (apply str (\_\_ "Leeeeeerrroyyy")) "Leroy")</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> cmprs <font color="#912f11">\[</font>coll<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#1f3f81">**when-let**</font> <font color="#912f11">\[\[</font>f <font color="#912f11">&</font> r<font color="#912f11">\]</font> <font color="#912f11">(</font><font color="#007080">seq</font> coll<font color="#912f11">)\]</font>   
    <font color="#ee9a00">(</font><font color="#912f11">if</font> <font color="#cdcd00">(</font><font color="#007080">=</font> f <font color="#698b22">(</font><font color="#007080">first</font> r<font color="#698b22">)</font><font color="#cdcd00">)</font>   
      <font color="#cdcd00">(</font>cmprs r<font color="#cdcd00">)</font>   
      <font color="#cdcd00">(</font><font color="#007080">cons</font> f <font color="#698b22">(</font>cmprs r<font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>    
<font color="#786000">; Basically a variant of the filter function. Note the sequence </font></font>

<font face="monospace"><font color="#786000">; is destructed</font><font color="#786000"> into first element f and the rest r. </font>

<font color="#786000">; 31: Write a function which packs consecutive duplicates into sub-lists.</font>  
<font color="#786000">; (= (\_\_ \[1 1 2 1 1 1 3 3\]) '((1 1) (2) (1 1 1) (3 3)))</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>coll<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#ee9a00">(</font><font color="#912f11">fn</font> pack <font color="#912f11">\[</font>res prev coll<font color="#912f11">\]</font>  
    <font color="#cdcd00">(</font><font color="#1f3f81">**if-let**</font> <font color="#912f11">\[\[</font>f <font color="#912f11">&</font> r<font color="#912f11">\]</font> <font color="#912f11">(</font><font color="#007080">seq</font> coll<font color="#912f11">)\]</font>   
      <font color="#698b22">(</font><font color="#912f11">if</font> <font color="#008b00">(</font><font color="#007080">=</font> f <font color="#96cdcd">(</font><font color="#007080">first</font> prev<font color="#96cdcd">)</font><font color="#008b00">)</font>   
        <font color="#008b00">(</font>pack res <font color="#96cdcd">(</font><font color="#007080">conj</font> prev f<font color="#96cdcd">)</font> r<font color="#008b00">)</font>   
        <font color="#008b00">(</font>pack <font color="#96cdcd">(</font><font color="#007080">conj</font> res prev<font color="#96cdcd">)</font> <font color="#912f11">\[</font>f<font color="#912f11">\]</font> r<font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font>   
     <font color="#cdcd00">(</font><font color="#007080">conj</font> res prev<font color="#cdcd00">)</font><font color="#ee9a00">)</font>  
    <font color="#912f11">\[\]</font> <font color="#912f11">\[(</font><font color="#007080">first</font> coll<font color="#912f11">)\]</font> <font color="#ee9a00">(</font><font color="#007080">rest</font> coll<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>    
<font color="#786000">; res is the final list, prev keeps the immediate previous sub-list. </font>  
<font color="#786000">; A much simpler version use partition-by:</font>  
<font color="#912f11">\#(</font><font color="#007080">partition-by</font> <font color="#007080">identity</font> <font color="#912f11">%</font><font color="#912f11">)</font>

<font color="#786000">; 33: Write a function which replicates each element of a sequence </font>

</font>

<font face="monospace"><font color="#786000">; n number of </font><font color="#786000">times.</font>  
<font color="#786000">; (= (\_\_ \[1 2 3\] 2) '(1 1 2 2 3 3)) </font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>coll n<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#007080">apply</font> <font color="#007080">concat</font> <font color="#ee9a00">(</font><font color="#1f3f81">**map**</font> <font color="#912f11">\#(</font><font color="#007080">repeat</font> n <font color="#912f11">%</font><font color="#912f11">)</font> coll<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; or more succintly: </font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>coll n<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#1f3f81">**mapcat**</font> <font color="#912f11">\#(</font><font color="#007080">repeat</font> n <font color="#912f11">%</font><font color="#912f11">)</font> coll<font color="#cd3700">)</font><font color="#912f11">)</font>

<font color="#786000">; 34: Write a function which creates a list of all integers in a </font>

</font>

<font face="monospace"><font color="#786000">; given range. </font>  
<font color="#786000">; (= (\_\_ 1 4) '(1 2 3))</font>  
<font color="#786000">; forbidden: range</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>s e<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#007080">take</font> <font color="#ee9a00">(</font><font color="#007080">-</font> e s<font color="#ee9a00">)</font> <font color="#ee9a00">(</font><font color="#007080">iterate</font> <font color="#007080">inc</font> s<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>

<font color="#786000">; 38: Write a function which takes a variable number of parameters </font>

</font>

<font face="monospace"><font color="#786000">; and returns </font><font color="#786000">the maximum value.</font>  
<font color="#786000">; forbidden: max, max-key</font>  
<font color="#786000">; (= (\_\_ 1 8 3 4) 8)</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>x <font color="#912f11">&</font> xs<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#1f3f81">**reduce**</font> <font color="#912f11">\#(</font><font color="#912f11">if</font> <font color="#912f11">(</font><font color="#007080">&lt;</font> %<font color="#077807">1</font> %<font color="#077807">2</font><font color="#912f11">)</font> <font color="#912f11">%2</font> <font color="#912f11">%1</font><font color="#912f11">)</font> x xs<font color="#cd3700">)</font><font color="#912f11">)</font>

<font color="#786000">; 39: Write a function which takes two sequences and returns the first</font>

</font>

<font face="monospace"><font color="#786000">; item </font><font color="#786000">from each, then the second item from each, then the third, etc.</font>  
<font color="#786000">; (= (\_\_ \[1 2\] \[3 4 5 6\]) '(1 3 2 4))</font>  
<font color="#786000">; forbidden: interleave</font>  
<font color="#912f11">\#(</font><font color="#1f3f81">**mapcat**</font> <font color="#007080">vector</font> <font color="#912f11">%1</font> <font color="#912f11">%2</font><font color="#912f11">)</font> 

<font color="#786000">; 40: Write a function which separates the items of a sequence by </font>

</font>

<font face="monospace"><font color="#786000">; an arbitrary </font><font color="#786000">value.</font>  
<font color="#786000">; (= (\_\_ 0 \[1 2 3\]) \[1 0 2 0 3\])</font>  
<font color="#786000">; forbidden: interpose</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>sep coll<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#007080">drop-last</font> <font color="#ee9a00">(</font><font color="#1f3f81">**mapcat**</font> <font color="#007080">vector</font> coll <font color="#cdcd00">(</font><font color="#007080">repeat</font> sep<font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>

<font color="#786000">; 41: Write a function which drops every Nth item from a sequence.</font>  
<font color="#786000">; (= (\_\_ \[1 2 3 4 5 6 7 8\] 3) \[1 2 4 5 7 8\])  </font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>coll n<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#007080">flatten</font>   
    <font color="#ee9a00">(</font><font color="#007080">concat</font>   
      <font color="#cdcd00">(</font><font color="#1f3f81">**map**</font> <font color="#912f11">\#(</font><font color="#007080">drop-last</font> <font color="#912f11">%</font><font color="#912f11">)</font> <font color="#698b22">(</font><font color="#007080">partition</font> n coll<font color="#698b22">)</font><font color="#cdcd00">)</font>   
      <font color="#cdcd00">(</font><font color="#007080">take-last</font> <font color="#698b22">(</font><font color="#007080">rem</font> <font color="#008b00">(</font><font color="#007080">count</font> coll<font color="#008b00">)</font> n<font color="#698b22">)</font> coll<font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; We partition the sequence, drop last one from each, then stitch them</font>

</font>

<font face="monospace"><font color="#786000">; back</font><font color="#786000"> take care the remaining elements too</font>

<font color="#786000">; 42: Write a function which calculates factorials.</font>  
<font color="#786000">; (= (\_\_ 5) 120)</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>n<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#007080">apply</font> <font color="#007080">\*</font> <font color="#ee9a00">(</font><font color="#007080">range</font> <font color="#077807">1</font> <font color="#cdcd00">(</font><font color="#007080">inc</font> n<font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; clojure arithmetic functions can take a variable number of arguments</font>

<font color="#786000">; 43: Write a function which reverses the interleave process into n </font>

</font>

<font face="monospace"><font color="#786000">; number of </font><font color="#786000">subsequences.</font>  
<font color="#786000">; (= (\_\_ \[1 2 3 4 5 6\] 2) '((1 3 5) (2 4 6)))</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>coll n<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#007080">apply</font> <font color="#1f3f81">**map**</font> <font color="#007080">list</font> <font color="#ee9a00">(</font><font color="#007080">partition</font> n coll<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; exploit map function's ability to take a variable number of </font></font>

<font face="monospace"><font color="#786000">; collections as </font><font color="#786000">arguments</font>

<font color="#786000">; 44: Write a function which can rotate a sequence in either direction.</font>  
<font color="#786000">; (= (\_\_ 2 \[1 2 3 4 5\]) '(3 4 5 1 2))</font>  
<font color="#786000">; (= (\_\_ -2 \[1 2 3 4 5\]) '(4 5 1 2 3))</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>n coll<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>ntime <font color="#912f11">(</font><font color="#912f11">if</font> <font color="#cd3700">(</font><font color="#007080">neg?</font> n<font color="#cd3700">)</font> <font color="#cd3700">(</font><font color="#007080">-</font> n<font color="#cd3700">)</font> n<font color="#912f11">)</font>  
        lshift <font color="#912f11">\#(</font><font color="#007080">concat</font> <font color="#912f11">(</font><font color="#007080">rest</font> %<font color="#912f11">)</font> <font color="#912f11">\[(</font><font color="#007080">first</font> %<font color="#912f11">)\])</font>  
        rshift <font color="#912f11">\#(</font><font color="#007080">cons</font> <font color="#912f11">(</font><font color="#007080">last</font> %<font color="#912f11">)</font> <font color="#912f11">(</font><font color="#007080">drop-last</font> %<font color="#912f11">))\]</font>  
    <font color="#ee9a00">(</font><font color="#cdcd00">(</font><font color="#007080">apply</font> <font color="#007080">comp</font> <font color="#698b22">(</font><font color="#007080">repeat</font> ntime <font color="#008b00">(</font><font color="#912f11">if</font> <font color="#96cdcd">(</font><font color="#007080">neg?</font> n<font color="#96cdcd">)</font> rshift lshift<font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font> coll<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>

<font color="#786000">; 50: Write a function which takes a sequence consisting of items </font>

</font>

<font face="monospace"><font color="#786000">; with different</font><font color="#786000"> types and splits them up into a set of homogeneous </font></font>

<font face="monospace"><font color="#786000">; sub-sequences. The internal</font><font color="#786000"> order of each sub-sequence should be </font></font>

<font face="monospace"><font color="#786000">; maintained, but the sub-sequences </font><font color="#786000">themselves can be returned in </font></font>

<font face="monospace"><font color="#786000">; any order (this is why 'set' is used in the </font><font color="#786000">test cases).</font>  
<font color="#786000">; (= (set (\_\_ \[1 :a 2 :b 3 :c\])) \#{\[1 2 3\] \[:a :b :c\]})</font>  
<font color="#912f11">\#(</font><font color="#007080">vals</font> <font color="#912f11">(</font><font color="#007080">group-by</font> <font color="#007080">type</font> %<font color="#912f11">))</font></font>

 

 
