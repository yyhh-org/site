Title: My solutions for problems No. 76-100 on 4clojure.com
Date: 2011-06-05 05:36
Author: Huahai
Category: notebook
Tags: Programming, Clojure
Slug: my-solutions-for-problems-no-76-100-on-4clojurecom
Alias: /blog/2011/06/my-solutions-problems-no-76-100-4clojure-com
Series: 4clojure-solutions
Lang: en

Finally done with all the 100 problems listed on 4clojure.com so far :-). When new problems appears there, I will probably do them when I have some time to kill, but I will not post my solutions here any more. If I found interesting programming exercises, I may submit to 4clojure as well.

This has been a great learning experience. I become very familiar with the core Clojure functions, especially the great sequence library. The functional way of writing code is so much fun, I wish I have been exposed to it earlier. Now I am hooked and would like to learn more. It's a pity there ain't many functional algorithm books around. The one I found is Chris Okasaki's "Purely Functional Data Structures", but the exposition language is Standard ML. Let's hope it can be easily translated into Clojure...

<font face="monospace">  
<font color="#786000">; 77: Write a function which finds all the anagrams in a vector of words. A </font>  
<font color="#786000">; word x is an anagram of word y if all the letters in x can be rearranged in </font>  
<font color="#786000">; a different order to form y. Your function should return a set of sets, where</font>  
<font color="#786000">; each sub-set is a group of words which are anagrams of each other. Each </font>  
<font color="#786000">; sub-set should have at least two words. Words without any anagrams should not</font>  
<font color="#786000">; be included in the result.</font>  
<font color="#786000">; (= (\_\_ \["meat" "mat" "team" "mate" "eat"\]) \#{\#{"meat" "team" "mate"}})</font>  
<font color="#786000">; (= (\_\_ \["veer" "lake" "item" "kale" "mite" "ever"\]) </font>  
<font color="#786000">;   \#{\#{"veer" "ever"} \#{"lake" "kale"} \#{"mite" "item"}})</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>coll<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#800090">-&gt;&gt;</font> <font color="#ee9a00">(</font><font color="#007080">group-by</font> <font color="#007080">frequencies</font> coll<font color="#ee9a00">)</font>  
    <font color="#ee9a00">(</font><font color="#007080">vals</font><font color="#ee9a00">)</font>  
    <font color="#ee9a00">(</font><font color="#1f3f81">**filter**</font> <font color="#912f11">\#(</font><font color="#007080">&gt;</font> <font color="#912f11">(</font><font color="#007080">count</font> %<font color="#912f11">)</font> <font color="#077807">1</font><font color="#912f11">)</font><font color="#ee9a00">)</font>  
    <font color="#ee9a00">(</font><font color="#1f3f81">**map**</font> <font color="#007080">set</font> <font color="#ee9a00">)</font>  
    <font color="#007080">set</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; anagrams have the same distribution of characters </font>

<font color="#786000">; 79: Write a function which calculates the sum of the minimal path through a </font>  
<font color="#786000">; triangle. The triangle is represented as a vector of vectors. The path should </font>  
<font color="#786000">; start at the top of the triangle and move to an adjacent number on the next </font>  
<font color="#786000">; row until the bottom of the triangle is reached. </font>  
<font color="#786000">; (= (\_\_ \[  \[1\]</font>  
          <font color="#786000">;\[2 4\]</font>  
         <font color="#786000">;\[5 1 4\]</font>  
        <font color="#786000">;\[2 3 4 5\]\])</font>  
   <font color="#786000">;(+ 1 2 1 3)</font>  
   <font color="#786000">;7)</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>triangle<font color="#912f11">\]</font>   
  <font color="#cd3700">(</font><font color="#007080">apply</font> <font color="#007080">min</font> <font color="#ee9a00">(</font><font color="#cdcd00">(</font><font color="#912f11">fn</font> path-sum <font color="#912f11">\[</font>p<font color="#912f11">\]</font>   
                <font color="#698b22">(</font><font color="#007080">concat</font>   
                  <font color="#008b00">(</font><font color="#912f11">if</font> <font color="#96cdcd">(</font><font color="#007080">=</font> <font color="#00688b">(</font><font color="#007080">count</font> triangle<font color="#00688b">)</font> <font color="#00688b">(</font><font color="#007080">count</font> p<font color="#00688b">)</font><font color="#96cdcd">)</font>   
                    <font color="#912f11">\[(</font><font color="#1f3f81">**reduce**</font> <font color="#007080">+</font> <font color="#cd3700">(</font><font color="#1f3f81">**map-indexed**</font> <font color="#912f11">\#(</font><font color="#007080">get-in</font> triangle <font color="#912f11">\[</font>%<font color="#077807">1</font> %<font color="#077807">2</font><font color="#912f11">\])</font> p<font color="#cd3700">)</font><font color="#912f11">)\]</font>   
                    <font color="#96cdcd">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>x <font color="#912f11">(</font><font color="#007080">last</font> p<font color="#912f11">)\]</font>   
                      <font color="#00688b">(</font><font color="#007080">concat</font>   
                        <font color="#483d8b">(</font>path-sum <font color="#9400d3">(</font><font color="#007080">conj</font> p x<font color="#9400d3">)</font><font color="#483d8b">)</font>   
                        <font color="#483d8b">(</font>path-sum <font color="#9400d3">(</font><font color="#007080">conj</font> p <font color="#912f11">(</font><font color="#007080">inc</font> x<font color="#912f11">)</font><font color="#9400d3">)</font><font color="#483d8b">)</font><font color="#00688b">)</font><font color="#96cdcd">)</font><font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font>   
              <font color="#912f11">\[</font><font color="#077807">0</font><font color="#912f11">\]</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; We enumerate all possible paths. The next step in a path can only go to the </font>  
<font color="#786000">; same or the plus one row index as the previous step, so the paths form a</font>  
<font color="#786000">; binary tree. We walk the tree recursively, building a row index vector p for</font>  
<font color="#786000">; each path.</font>

<font color="#786000">; 81: Reimplement set intersection</font>  
<font color="#912f11">\#(</font><font color="#007080">set</font> <font color="#912f11">(</font><font color="#1f3f81">**filter**</font> %<font color="#077807">1</font> %<font color="#077807">2</font><font color="#912f11">))</font>  
<font color="#786000">; sets are functions too, so this works</font>

<font color="#786000">; 82: A word chain consists of a set of words ordered so that each word differs</font>  
<font color="#786000">; by only one letter from the words directly before and after it. The one </font>  
<font color="#786000">; letter difference can be either an insertion, a deletion, or a substitution. </font>  
<font color="#786000">; Here is an example word chain:</font>  
<font color="#786000">; cat -&gt; cot -&gt; coat -&gt; oat -&gt; hat -&gt; hot -&gt; hog -&gt; dog</font>  
<font color="#786000">; Write a function which takes a sequence of words, and returns true if they </font>  
<font color="#786000">; can be arranged into one continous word chain, and false if they cannot.</font>  
<font color="#786000">; (= false (\_\_ \#{"cot" "hot" "bat" "fat"}))</font>  
<font color="#786000">; (= true (\_\_ \#{"spout" "do" "pot" "pout" "spot" "dot"}))</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>word-set<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#800090">letfn</font> <font color="#912f11">\[(</font>edit-dist <font color="#912f11">\[</font>a b<font color="#912f11">\]</font>   
            <font color="#cd3700">(</font><font color="#1f3f81">**cond**</font>   
              <font color="#ee9a00">(</font><font color="#007080">not</font> <font color="#cdcd00">(</font><font color="#800090">or</font> a b<font color="#cdcd00">)</font><font color="#ee9a00">)</font> <font color="#077807">0</font>   
              <font color="#ee9a00">(</font><font color="#007080">not</font> b<font color="#ee9a00">)</font> <font color="#ee9a00">(</font><font color="#007080">count</font> a<font color="#ee9a00">)</font>   
              <font color="#ee9a00">(</font><font color="#007080">not</font> a<font color="#ee9a00">)</font> <font color="#ee9a00">(</font><font color="#007080">count</font> b<font color="#ee9a00">)</font>   
              <font color="#1f3f81">**:else**</font> <font color="#ee9a00">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>ra <font color="#912f11">(</font><font color="#007080">next</font> a<font color="#912f11">)</font> rb <font color="#912f11">(</font><font color="#007080">next</font> b<font color="#912f11">)\]</font>   
                      <font color="#cdcd00">(</font><font color="#912f11">if</font> <font color="#698b22">(</font><font color="#007080">=</font> <font color="#008b00">(</font><font color="#007080">first</font> a<font color="#008b00">)</font> <font color="#008b00">(</font><font color="#007080">first</font> b<font color="#008b00">)</font><font color="#698b22">)</font>   
                        <font color="#698b22">(</font>edit-dist ra rb<font color="#698b22">)</font>   
                        <font color="#698b22">(</font><font color="#007080">+</font> <font color="#077807">1</font> <font color="#008b00">(</font><font color="#007080">min</font>   
                               <font color="#96cdcd">(</font>edit-dist ra rb<font color="#96cdcd">)</font>   
                               <font color="#96cdcd">(</font>edit-dist ra b<font color="#96cdcd">)</font>   
                               <font color="#96cdcd">(</font>edit-dist a rb<font color="#96cdcd">)</font><font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
          <font color="#912f11">(</font>find-paths <font color="#912f11">\[</font>graph start seen<font color="#912f11">\]</font>   
            <font color="#cd3700">(</font><font color="#912f11">if</font> <font color="#ee9a00">(</font>seen start<font color="#ee9a00">)</font>   
              seen  
              <font color="#ee9a00">(</font><font color="#1f3f81">**for**</font> <font color="#912f11">\[</font>n <font color="#912f11">(</font>graph start<font color="#912f11">)\]</font>   
                <font color="#cdcd00">(</font>find-paths graph n <font color="#698b22">(</font><font color="#007080">conj</font> seen start<font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)\]</font>   
    <font color="#ee9a00">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>graph <font color="#912f11">(</font><font color="#007080">into</font> <font color="#912f11">{}</font>   
                      <font color="#cd3700">(</font><font color="#1f3f81">**for**</font> <font color="#912f11">\[</font>s word-set<font color="#912f11">\]</font>   
                        <font color="#912f11">\[</font>s <font color="#912f11">(</font><font color="#1f3f81">**filter**</font> <font color="#912f11">\#(</font><font color="#007080">=</font> <font color="#077807">1</font> <font color="#912f11">(</font>edit-dist s %<font color="#912f11">))</font> word-set<font color="#912f11">)\]</font><font color="#cd3700">)</font><font color="#912f11">)\]</font>  
      <font color="#cdcd00">(</font><font color="#912f11">if</font> <font color="#698b22">(</font><font color="#007080">some</font> <font color="#008b00">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>w<font color="#912f11">\]</font>   
                  <font color="#96cdcd">(</font><font color="#007080">some</font> <font color="#912f11">\#(</font><font color="#007080">=</font> word-set <font color="#912f11">%</font><font color="#912f11">)</font>   
                        <font color="#00688b">(</font><font color="#007080">flatten</font> <font color="#483d8b">(</font>find-paths graph w <font color="#912f11">\#{}</font><font color="#483d8b">)</font><font color="#00688b">)</font><font color="#96cdcd">)</font><font color="#008b00">)</font>   
                word-set<font color="#698b22">)</font>   
        <font color="#077807">true</font> <font color="#077807">false</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; This problem consists of two sub-problems: A. Determine the edit distance </font>  
<font color="#786000">; between two strings. For brevity, we just used the standard recursive </font>  
<font color="#786000">; algorithm instead of dynamic programming. B. For the graph of strings </font>  
<font color="#786000">; connected by edges of edit distance 1, find a simple (no loop) path that </font>  
<font color="#786000">; goes through all strings once and only once. The graph is represented as</font>  
<font color="#786000">; a map of adjacent node lists. We enumerate all simple paths in the graph </font>  
<font color="#786000">; until we found one going through all nodes.</font>

<font color="#786000">; 84: Write a function which generates the transitive closure of a binary </font>  
<font color="#786000">; relation. The relation will be represented as a set of 2 item vectors.</font>  
<font color="#786000">; (let \[divides \#{\[8 4\] \[9 3\] \[4 2\] \[27 9\]}\]</font>  
<font color="#786000">;   (= (\_\_ divides) \#{\[4 2\] \[8 4\] \[8 2\] \[9 3\] \[27 9\] \[27 3\]}))</font>  
<font color="#786000">; (let \[progeny</font>  
<font color="#786000">;       \#{\["father" "son"\] \["uncle" "cousin"\] \["son" "grandson"\]}\]</font>  
<font color="#786000">;         (= (\_\_ progeny)</font>  
<font color="#786000">;              \#{\["father" "son"\] \["father" "grandson"\]</font>  
<font color="#786000">;                     \["uncle" "cousin"\] \["son" "grandson"\]}))</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>relation<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#800090">letfn</font> <font color="#912f11">\[(</font>expand <font color="#912f11">\[</font>r<font color="#912f11">\]</font>   
            <font color="#cd3700">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>m <font color="#912f11">(</font><font color="#007080">into</font> <font color="#912f11">{}</font> r<font color="#912f11">)\]</font>   
              <font color="#ee9a00">(</font><font color="#800090">-&gt;&gt;</font> <font color="#cdcd00">(</font><font color="#007080">concat</font>   
                     r  
                     <font color="#698b22">(</font><font color="#1f3f81">**for**</font> <font color="#912f11">\[\[</font>k v<font color="#912f11">\]</font> m<font color="#912f11">\]</font>   
                       <font color="#008b00">(</font><font color="#1f3f81">**when-let**</font> <font color="#912f11">\[</font>nv <font color="#912f11">(</font>m v<font color="#912f11">)\]</font> <font color="#912f11">\[</font>k nv<font color="#912f11">\]</font><font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font>   
                <font color="#cdcd00">(</font><font color="#1f3f81">**filter**</font> <font color="#007080">identity</font><font color="#cdcd00">)</font>   
                <font color="#007080">set</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
          <font color="#912f11">(</font>first-consecutive <font color="#912f11">\[</font>pred <font color="#912f11">\[</font>f <font color="#912f11">&</font> rs<font color="#912f11">\]\]</font>   
            <font color="#cd3700">(</font><font color="#1f3f81">**when**</font> rs  
              <font color="#ee9a00">(</font><font color="#912f11">if</font> <font color="#cdcd00">(</font>pred f <font color="#698b22">(</font><font color="#007080">first</font> rs<font color="#698b22">)</font><font color="#cdcd00">)</font>  
                f  
                <font color="#cdcd00">(</font><font color="#1f3f81">**recur**</font> pred rs<font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)\]</font>  
    <font color="#ee9a00">(</font>first-consecutive <font color="#007080">=</font> <font color="#cdcd00">(</font><font color="#007080">iterate</font> expand relation<font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; we iteratively expand the set of transitive relation, until the set no </font>  
<font color="#786000">; longer changes</font>

<font color="#786000">; 85: Write a function which generates the power set of a given set. The power </font>  
<font color="#786000">; set of a set x is the set of all subsets of x, including the empty set and x </font>  
<font color="#786000">; itself.</font>  
<font color="#786000">; (= (\_\_ \#{1 :a}) \#{\#{1 :a} \#{:a} \#{} \#{1}})</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>s<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#1f3f81">**reduce**</font>   
    <font color="#ee9a00">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>init e<font color="#912f11">\]</font>   
      <font color="#cdcd00">(</font><font color="#007080">set</font> <font color="#698b22">(</font><font color="#007080">concat</font> init <font color="#008b00">(</font><font color="#1f3f81">**map**</font> <font color="#912f11">\#(</font><font color="#007080">conj</font> <font color="#912f11">%</font> e<font color="#912f11">)</font> init<font color="#008b00">)</font> <font color="#912f11">\[\#{</font>e<font color="#912f11">}\]</font><font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font>  
    <font color="#912f11">\#{\#{}}</font> s<font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; we just add one element at a time</font>

<font color="#786000">; 86: Happy numbers are positive integers that follow a particular formula: take</font>  
<font color="#786000">; each individual digit, square it, and then sum the squares to get a new number</font>  
<font color="#786000">; Repeat with the new number and eventually, you might get to a number whose </font>  
<font color="#786000">; squared sum is 1. This is a happy number. An unhappy number (or sad number) is</font>  
<font color="#786000">; one that loops endlessly. Write a function that determines if a number is </font>  
<font color="#786000">; happy or not.</font>  
<font color="#786000">; (= (\_\_ 7) true)</font>  
<font color="#786000">; (= (\_\_ 986543210) true)</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>x<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#800090">letfn</font> <font color="#912f11">\[(</font>digits <font color="#912f11">\[</font>n<font color="#912f11">\]</font>  
            <font color="#cd3700">(</font><font color="#1f3f81">**for**</font> <font color="#912f11">\[</font>y <font color="#912f11">(</font><font color="#007080">iterate</font> <font color="#cd3700">(</font><font color="#007080">partial</font> <font color="#007080">\*</font> <font color="#077807">10</font><font color="#cd3700">)</font> <font color="#077807">1</font><font color="#912f11">)</font> <font color="#1f3f81">**:while**</font> <font color="#912f11">(</font><font color="#007080">&lt;=</font> y n<font color="#912f11">)\]</font>  
              <font color="#ee9a00">(</font><font color="#007080">rem</font> <font color="#cdcd00">(</font><font color="#007080">int</font> <font color="#698b22">(</font><font color="#007080">/</font> n y<font color="#698b22">)</font><font color="#cdcd00">)</font> <font color="#077807">10</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
          <font color="#912f11">(</font>sqr-sum <font color="#912f11">\[</font>ds<font color="#912f11">\]</font>  
            <font color="#cd3700">(</font><font color="#1f3f81">**reduce**</font> <font color="#007080">+</font> <font color="#ee9a00">(</font><font color="#1f3f81">**map**</font> <font color="#912f11">\#(</font><font color="#007080">\*</font> <font color="#912f11">%</font> <font color="#912f11">%</font><font color="#912f11">)</font> ds<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)\]</font>  
    <font color="#ee9a00">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>r <font color="#912f11">(</font><font color="#007080">some</font> <font color="#912f11">\#{</font><font color="#077807">1</font> <font color="#077807">4</font><font color="#912f11">}</font> <font color="#cd3700">(</font><font color="#007080">iterate</font> <font color="#ee9a00">(</font><font color="#007080">comp</font> sqr-sum digits<font color="#ee9a00">)</font> x<font color="#cd3700">)</font><font color="#912f11">)\]</font>  
      <font color="#cdcd00">(</font><font color="#1f3f81">**cond**</font>  
        <font color="#698b22">(</font><font color="#007080">=</font> <font color="#077807">1</font> r<font color="#698b22">)</font> <font color="#077807">true</font>  
        <font color="#698b22">(</font><font color="#007080">=</font> <font color="#077807">4</font> r<font color="#698b22">)</font> <font color="#077807">false</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; it turns out that 4 is a sad number, as it results into an infinite loop</font>

<font color="#786000">; 88: Write a function which returns the symmetric difference of two sets. The</font>  
<font color="#786000">; symmetric difference is the set of items belonging to one but not both of </font>  
<font color="#786000">; the two sets.</font>  
<font color="#786000">; (= (\_\_ \#{1 2 3 4 5 6} \#{1 3 5 7}) \#{2 4 6 7})</font>  
<font color="#912f11">\#(</font><font color="#007080">set</font> <font color="#912f11">(</font><font color="#007080">remove</font> <font color="#cd3700">(</font><font color="#007080">set</font> <font color="#ee9a00">(</font><font color="#1f3f81">**filter**</font> %<font color="#077807">1</font> %<font color="#077807">2</font><font color="#ee9a00">)</font><font color="#cd3700">)</font> <font color="#cd3700">(</font><font color="#007080">into</font> %<font color="#077807">1</font> %<font color="#077807">2</font><font color="#cd3700">)</font><font color="#912f11">))</font>  
<font color="#786000">; we remove the intersection from the union</font>

<font color="#786000">; 89: Starting with a graph you must write a function that returns true if it </font>  
<font color="#786000">; is possible to make a tour of the graph in which every edge is visited exactly</font>  
<font color="#786000">; once.  The graph is represented by a vector of tuples, where each tuple </font>  
<font color="#786000">; represents a single edge.  The rules are: </font>  
<font color="#786000">; - You can start at any node.  </font>  
<font color="#786000">; - You must visit each edge exactly once.  </font>  
<font color="#786000">; - All edges are undirected.</font>  
<font color="#786000">; (= true (\_\_ \[\[1 2\] \[2 3\] \[3 4\] \[4 1\]\]))</font>  
<font color="#786000">; (= false (\_\_ \[\[1 2\] \[2 3\] \[2 4\] \[2 5\]\]))</font>  
<font color="#786000">; (= false (\_\_ \[\[:a :b\] \[:a :b\] \[:a :c\] \[:c :a\] \[:a :d\] \[:b :d\] \[:c :d\]\]))</font>  
<font color="#786000">; (= true (\_\_ \[\[:a :b\] \[:a :c\] \[:c :b\] \[:a :e\] \[:b :e\] \[:a :d\] \[:b :d\] </font>  
<font color="#786000">;              \[:c :e\] \[:d :e\] \[:c :f\] \[:d :f\]\]))</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>edge-list<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>graph <font color="#912f11">(</font><font color="#007080">apply</font> <font color="#007080">merge-with</font>   
                <font color="#912f11">\#(</font><font color="#007080">into</font> <font color="#912f11">%1</font> <font color="#912f11">%2</font><font color="#912f11">)</font>   
                <font color="#cd3700">(</font><font color="#007080">apply</font> <font color="#007080">concat</font>   
                  <font color="#ee9a00">(</font><font color="#1f3f81">**map-indexed**</font>   
                    <font color="#cdcd00">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>i <font color="#912f11">\[</font>k v<font color="#912f11">\]\]</font>   
                      <font color="#912f11">\[{</font>k <font color="#912f11">\#{{</font><font color="#1f3f81">**:node**</font> v <font color="#1f3f81">**:index**</font> i<font color="#912f11">}}}</font>   
                       <font color="#912f11">{</font>v <font color="#912f11">\#{{</font><font color="#1f3f81">**:node**</font> k <font color="#1f3f81">**:index**</font> i<font color="#912f11">}}}\]</font><font color="#cdcd00">)</font>   
                    edge-list<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)\]</font>  
    <font color="#ee9a00">(</font><font color="#912f11">if</font> <font color="#cdcd00">(</font><font color="#007080">some</font>  
          <font color="#698b22">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>node<font color="#912f11">\]</font>   
            <font color="#008b00">(</font><font color="#007080">some</font>   
              <font color="#007080">identity</font>   
              <font color="#96cdcd">(</font><font color="#007080">flatten</font>   
                <font color="#00688b">(</font><font color="#483d8b">(</font><font color="#912f11">fn</font> visit <font color="#912f11">\[</font>n vs<font color="#912f11">\]</font>   
                   <font color="#9400d3">(</font><font color="#912f11">if</font> <font color="#912f11">(</font><font color="#007080">every?</font> <font color="#912f11">\#(</font>vs <font color="#912f11">(</font><font color="#1f3f81">**:index**</font> %<font color="#912f11">))</font> <font color="#cd3700">(</font>graph n<font color="#cd3700">)</font><font color="#912f11">)</font>   
                     <font color="#912f11">(</font><font color="#912f11">if</font> <font color="#cd3700">(</font><font color="#007080">every?</font> <font color="#007080">identity</font> vs<font color="#cd3700">)</font> <font color="#077807">true</font> <font color="#077807">false</font><font color="#912f11">)</font>   
                     <font color="#912f11">(</font><font color="#1f3f81">**for**</font> <font color="#912f11">\[</font>x <font color="#912f11">(</font>graph n<font color="#912f11">)\]</font>   
                       <font color="#cd3700">(</font><font color="#1f3f81">**when-not**</font> <font color="#ee9a00">(</font>vs <font color="#cdcd00">(</font><font color="#1f3f81">**:index**</font> x<font color="#cdcd00">)</font><font color="#ee9a00">)</font>   
                         <font color="#ee9a00">(</font>visit <font color="#cdcd00">(</font><font color="#1f3f81">**:node**</font> x<font color="#cdcd00">)</font> <font color="#cdcd00">(</font><font color="#007080">assoc</font> vs <font color="#698b22">(</font><font color="#1f3f81">**:index**</font> x<font color="#698b22">)</font> <font color="#077807">true</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font><font color="#9400d3">)</font><font color="#483d8b">)</font>  
                 node <font color="#483d8b">(</font><font color="#007080">vec</font> <font color="#9400d3">(</font><font color="#007080">repeat</font> <font color="#912f11">(</font><font color="#007080">count</font> edge-list<font color="#912f11">)</font> <font color="#077807">false</font><font color="#9400d3">)</font><font color="#483d8b">)</font><font color="#00688b">)</font><font color="#96cdcd">)</font><font color="#008b00">)</font><font color="#698b22">)</font>   
          <font color="#698b22">(</font><font color="#007080">set</font> <font color="#008b00">(</font><font color="#007080">apply</font> <font color="#007080">concat</font> edge-list<font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font>   
      <font color="#077807">true</font> <font color="#077807">false</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; This problem looks similar to problem 82 as both are graph traversals, but</font>  
<font color="#786000">; the graphs are quite different. Here redundent edges exist, so we cannot use</font>  
<font color="#786000">; a set or a map to track edge visits, we instead use a vector of booleans. </font>  
<font color="#786000">; Also, the condition is to traverse all edges instead of all nodes. We again </font>  
<font color="#786000">; use a map of adjacent node lists as the graph, but supplement each adjacent </font>  
<font color="#786000">; node with the index of the corresponding edge. Finally, here a node can be </font>  
<font color="#786000">; visited multiple times, and we terminates a path at a node only when all of </font>  
<font color="#786000">; its edges have already been visited.</font>

<font color="#786000">; 91: Given a graph, determine whether the graph is connected. A connected </font>  
<font color="#786000">; graph is such that a path exists between any two given nodes.  </font>  
<font color="#786000">; -Your function must return true if the graph is connected and false otherwise.</font>  
<font color="#786000">; -You will be given a set of tuples representing the edges of a graph. Each </font>  
<font color="#786000">;  member of a tuple being a vertex/node in the graph.  </font>  
<font color="#786000">; -Each edge is undirected (can be traversed either direction). </font>  
<font color="#786000">;  (= false (\_\_ \#{\[1 2\] \[2 3\] \[3 1\] \[4 5\] \[5 6\] \[6 4\]}))</font>  
<font color="#786000">;  (= true (\_\_ \#{\[1 2\] \[2 3\] \[3 1\]\[4 5\] \[5 6\] \[6 4\] \[3 4\]}))</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>edge-list<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>graph <font color="#912f11">(</font><font color="#007080">apply</font> <font color="#007080">merge-with</font>   
                <font color="#912f11">\#(</font><font color="#007080">into</font> <font color="#912f11">%1</font> <font color="#912f11">%2</font><font color="#912f11">)</font>   
                <font color="#cd3700">(</font><font color="#007080">apply</font> <font color="#007080">concat</font>   
                  <font color="#ee9a00">(</font><font color="#1f3f81">**map**</font> <font color="#cdcd00">(</font><font color="#912f11">fn</font> <font color="#912f11">\[\[</font>k v<font color="#912f11">\]\]</font> <font color="#912f11">\[{</font>k <font color="#912f11">\#{</font>v<font color="#912f11">}}</font> <font color="#912f11">{</font>v <font color="#912f11">\#{</font>k<font color="#912f11">}}\]</font><font color="#cdcd00">)</font> edeg-list<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)\]</font>   
    <font color="#ee9a00">(</font><font color="#912f11">if</font> <font color="#cdcd00">(</font><font color="#007080">some</font> <font color="#912f11">\#(</font><font color="#007080">=</font> <font color="#912f11">(</font><font color="#007080">count</font> %<font color="#912f11">)</font> <font color="#912f11">(</font><font color="#007080">count</font> graph<font color="#912f11">))</font>   
              <font color="#698b22">(</font><font color="#007080">flatten</font>   
                <font color="#008b00">(</font><font color="#96cdcd">(</font><font color="#912f11">fn</font> paths <font color="#912f11">\[</font>node seen<font color="#912f11">\]</font>   
                   <font color="#00688b">(</font><font color="#912f11">if</font> <font color="#483d8b">(</font>seen node<font color="#483d8b">)</font>   
                     seen  
                     <font color="#483d8b">(</font><font color="#1f3f81">**for**</font> <font color="#912f11">\[</font>x <font color="#912f11">(</font>graph node<font color="#912f11">)\]</font>   
                       <font color="#9400d3">(</font>paths x <font color="#912f11">(</font><font color="#007080">conj</font> seen node<font color="#912f11">)</font><font color="#9400d3">)</font><font color="#483d8b">)</font><font color="#00688b">)</font><font color="#96cdcd">)</font>   
                 <font color="#96cdcd">(</font><font color="#007080">ffirst</font> graph<font color="#96cdcd">)</font> <font color="#912f11">\#{}</font><font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font>   
      <font color="#077807">true</font> <font color="#077807">false</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">;  This graph traversal problem is simpler than both 82 and 89. We only  need </font>  
<font color="#786000">;  to start searching from any one of the nodes instead of all nodes. But the </font>  
<font color="#786000">;  pattern of the code is similar.</font>

<font color="#786000">; 92: Write a function to parse a Roman-numeral string and return the number it</font>  
<font color="#786000">; represents. You can assume that the input will be well-formed, in upper-case,</font>  
<font color="#786000">; and follow the subtractive principle. You don't need to handle any numbers </font>  
<font color="#786000">; greater than MMMCMXCIX (3999), the largest number representable with </font>  
<font color="#786000">; ordinary letters.</font>  
<font color="#786000">; (= 827 (\_\_ "DCCCXXVII"))</font>  
<font color="#786000">; (= 48 (\_\_ "XLVIII"))</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>s<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>snum <font color="#912f11">{\[</font><font color="#077807">\\C</font> <font color="#077807">\\M</font><font color="#912f11">\]</font> <font color="#077807">900</font>  <font color="#912f11">\[</font><font color="#077807">\\C</font> <font color="#077807">\\D</font><font color="#912f11">\]</font> <font color="#077807">400</font> <font color="#912f11">\[</font><font color="#077807">\\X</font> <font color="#077807">\\C</font><font color="#912f11">\]</font> <font color="#077807">90</font>   
             <font color="#912f11">\[</font><font color="#077807">\\X</font> <font color="#077807">\\L</font><font color="#912f11">\]</font> <font color="#077807">40</font> <font color="#912f11">\[</font><font color="#077807">\\I</font> <font color="#077807">\\X</font><font color="#912f11">\]</font> <font color="#077807">9</font> <font color="#912f11">\[</font><font color="#077807">\\I</font> <font color="#077807">\\V</font><font color="#912f11">\]</font> <font color="#077807">4</font><font color="#912f11">}</font>  
        nums <font color="#912f11">{</font><font color="#077807">\\I</font> <font color="#077807">1</font> <font color="#077807">\\V</font> <font color="#077807">5</font> <font color="#077807">\\X</font> <font color="#077807">10</font> <font color="#077807">\\L</font> <font color="#077807">50</font> <font color="#077807">\\C</font> <font color="#077807">100</font> <font color="#077807">\\D</font> <font color="#077807">500</font> <font color="#077807">\\M</font> <font color="#077807">1000</font><font color="#912f11">}\]</font>  
    <font color="#ee9a00">(</font><font color="#800090">letfn</font> <font color="#912f11">\[(</font>sum-snum <font color="#912f11">\[\[</font>f <font color="#912f11">&</font> r<font color="#912f11">\]\]</font>  
                      <font color="#cd3700">(</font><font color="#912f11">if</font> f  
                        <font color="#ee9a00">(</font><font color="#007080">+</font> <font color="#cdcd00">(</font><font color="#1f3f81">**if-let**</font> <font color="#912f11">\[</font>n <font color="#912f11">(</font>snum <font color="#912f11">\[</font>f <font color="#912f11">(</font><font color="#007080">first</font> r<font color="#912f11">)\])\]</font>   
                             n <font color="#077807">0</font><font color="#cdcd00">)</font>  
                           <font color="#cdcd00">(</font>sum-snum r<font color="#cdcd00">)</font><font color="#ee9a00">)</font>  
                        <font color="#077807">0</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
            <font color="#912f11">(</font>del-snum <font color="#912f11">\[\[</font>f <font color="#912f11">&</font> r<font color="#912f11">\]\]</font>  
                         <font color="#cd3700">(</font><font color="#1f3f81">**when**</font> f  
                           <font color="#ee9a00">(</font><font color="#912f11">if</font> <font color="#cdcd00">(</font>snum <font color="#912f11">\[</font>f <font color="#912f11">(</font><font color="#007080">first</font> r<font color="#912f11">)\]</font><font color="#cdcd00">)</font>  
                             <font color="#cdcd00">(</font>del-snum <font color="#698b22">(</font><font color="#007080">rest</font> r<font color="#698b22">)</font><font color="#cdcd00">)</font>  
                             <font color="#cdcd00">(</font><font color="#007080">cons</font> f <font color="#698b22">(</font>del-snum r<font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)\]</font>  
      <font color="#cdcd00">(</font><font color="#1f3f81">**reduce**</font> <font color="#007080">+</font> <font color="#698b22">(</font>sum-snum s<font color="#698b22">)</font> <font color="#698b22">(</font><font color="#1f3f81">**map**</font> nums <font color="#008b00">(</font>del-snum s<font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; We first find and sum the special numbers (4, 9, etc), remove them and sum</font>  
<font color="#786000">; the rest.  </font>

<font color="#786000">; 93: Write a function which flattens any nested combination of sequential </font>  
<font color="#786000">; things (lists, vectors, etc.), but maintains the lowest level sequential </font>  
<font color="#786000">; items. The result should be a sequence of sequences with only one level of </font>  
<font color="#786000">; nesting.</font>  
<font color="#786000">; (= (\_\_ '((1 2)((3 4)((((5 6))))))) '((1 2)(3 4)(5 6)))</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> pf <font color="#912f11">\[</font>coll<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>l <font color="#912f11">(</font><font color="#007080">first</font> coll<font color="#912f11">)</font> r <font color="#912f11">(</font><font color="#007080">next</font> coll<font color="#912f11">)\]</font>  
    <font color="#ee9a00">(</font><font color="#007080">concat</font>   
      <font color="#cdcd00">(</font><font color="#912f11">if</font> <font color="#698b22">(</font><font color="#800090">and</font> <font color="#008b00">(</font><font color="#007080">sequential?</font> l<font color="#008b00">)</font> <font color="#008b00">(</font><font color="#007080">not</font> <font color="#96cdcd">(</font><font color="#007080">sequential?</font> <font color="#00688b">(</font><font color="#007080">first</font> l<font color="#00688b">)</font><font color="#96cdcd">)</font><font color="#008b00">)</font><font color="#698b22">)</font>  
        <font color="#912f11">\[</font>l<font color="#912f11">\]</font>  
        <font color="#698b22">(</font>pf l<font color="#698b22">)</font><font color="#cdcd00">)</font>  
      <font color="#cdcd00">(</font><font color="#1f3f81">**when**</font> <font color="#698b22">(</font><font color="#007080">sequential?</font> r<font color="#698b22">)</font>  
        <font color="#698b22">(</font>pf r<font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; this is just a slight modification of the solution to problem 28.</font>

<font color="#786000">; 94: The game of life is a cellular automaton devised by mathematician John </font>  
<font color="#786000">; Conway.  The 'board' consists of both live (\#) and dead ( ) cells. Each cell </font>  
<font color="#786000">; interacts with its eight neighbours (horizontal, vertical, diagonal), and its</font>  
<font color="#786000">; next state is dependent on the following rules: 1) Any live cell with fewer </font>  
<font color="#786000">; than two live neighbours dies, as if caused by under-population.  2) Any live</font>  
<font color="#786000">; cell with two or three live neighbours lives on to the next generation.  3) </font>  
<font color="#786000">; Any live cell with more than three live neighbours dies, as if by overcrowding</font>  
<font color="#786000">; . 4) Any dead cell with exactly three live neighbours becomes a live cell, as</font>  
<font color="#786000">; if by reproduction.  Write a function that accepts a board, and returns a </font>  
<font color="#786000">; board representing the next generation of cells.</font>  
<font color="#786000">;(= (\_\_ \["      " </font>  
        <font color="#786000">;" \#\#   "</font>  
        <font color="#786000">;" \#\#   "</font>  
        <font color="#786000">;"   \#\# "</font>  
        <font color="#786000">;"   \#\# "</font>  
        <font color="#786000">;"      "\])</font>  
   <font color="#786000">;\["      " </font>  
    <font color="#786000">;" \#\#   "</font>  
    <font color="#786000">;" \#    "</font>  
    <font color="#786000">;"    \# "</font>  
    <font color="#786000">;"   \#\# "</font>  
    <font color="#786000">;"      "\])</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>board<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>offsets <font color="#912f11">\[\[</font><font color="#077807">-1</font> <font color="#077807">-1</font><font color="#912f11">\]</font> <font color="#912f11">\[</font><font color="#077807">-1</font> <font color="#077807">0</font><font color="#912f11">\]</font> <font color="#912f11">\[</font><font color="#077807">-1</font> <font color="#077807">1</font><font color="#912f11">\]</font>  
                 <font color="#912f11">\[</font><font color="#077807">0</font> <font color="#077807">-1</font><font color="#912f11">\]</font> <font color="#912f11">\[</font><font color="#077807">0</font> <font color="#077807">1</font><font color="#912f11">\]</font>  
                 <font color="#912f11">\[</font><font color="#077807">1</font> <font color="#077807">-1</font><font color="#912f11">\]</font> <font color="#912f11">\[</font><font color="#077807">1</font> <font color="#077807">0</font><font color="#912f11">\]</font> <font color="#912f11">\[</font><font color="#077807">1</font> <font color="#077807">1</font><font color="#912f11">\]\]</font>  
        height <font color="#912f11">(</font><font color="#007080">count</font> board<font color="#912f11">)</font>  
        width <font color="#912f11">(</font><font color="#007080">count</font> <font color="#cd3700">(</font><font color="#007080">first</font> board<font color="#cd3700">)</font><font color="#912f11">)</font>  
        get-state <font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[\[</font>x y<font color="#912f11">\]</font> <font color="#912f11">\[</font>dx dy<font color="#912f11">\]\]</font>  
                    <font color="#cd3700">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>c <font color="#912f11">(</font><font color="#007080">+</font> x dx<font color="#912f11">)</font> r <font color="#912f11">(</font><font color="#007080">+</font> y dy<font color="#912f11">)\]</font>   
                      <font color="#ee9a00">(</font><font color="#912f11">if</font> <font color="#cdcd00">(</font><font color="#800090">or</font> <font color="#698b22">(</font><font color="#007080">&lt;</font> c <font color="#077807">0</font><font color="#698b22">)</font> <font color="#698b22">(</font><font color="#007080">=</font> c width<font color="#698b22">)</font> <font color="#698b22">(</font><font color="#007080">&lt;</font> r <font color="#077807">0</font><font color="#698b22">)</font> <font color="#698b22">(</font><font color="#007080">=</font> r height<font color="#698b22">)</font><font color="#cdcd00">)</font>  
                        <font color="#077807">\\space</font>  
                        <font color="#cdcd00">(</font><font color="#007080">get-in</font> board <font color="#912f11">\[</font>r c<font color="#912f11">\]</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
        count-lives <font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>p<font color="#912f11">\]</font>  
                      <font color="#cd3700">(</font><font color="#1f3f81">**reduce**</font> <font color="#007080">+</font> <font color="#ee9a00">(</font><font color="#1f3f81">**map**</font> <font color="#912f11">\#(</font><font color="#912f11">if</font> <font color="#912f11">(</font><font color="#007080">=</font> <font color="#077807">\\\#</font> <font color="#cd3700">(</font>get-state p %<font color="#cd3700">)</font><font color="#912f11">)</font> <font color="#077807">1</font> <font color="#077807">0</font><font color="#912f11">)</font> offsets<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
        next-state <font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>s p<font color="#912f11">\]</font>  
                     <font color="#cd3700">(</font><font color="#912f11">let</font> <font color="#912f11">\[</font>n <font color="#912f11">(</font>count-lives p<font color="#912f11">)\]</font>   
                       <font color="#ee9a00">(</font><font color="#912f11">if</font> <font color="#cdcd00">(</font><font color="#800090">or</font> <font color="#698b22">(</font><font color="#007080">=</font> n <font color="#077807">3</font><font color="#698b22">)</font>  
                               <font color="#698b22">(</font><font color="#800090">and</font> <font color="#008b00">(</font><font color="#007080">=</font> s <font color="#077807">\\\#</font><font color="#008b00">)</font> <font color="#008b00">(</font><font color="#007080">=</font> n <font color="#077807">2</font><font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font>  
                         <font color="#077807">\\\#</font>  
                         <font color="#077807">\\space</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)\]</font>   
    <font color="#ee9a00">(</font><font color="#800090">-&gt;&gt;</font> <font color="#cdcd00">(</font><font color="#1f3f81">**for**</font> <font color="#912f11">\[</font>y <font color="#912f11">(</font><font color="#007080">range</font> height<font color="#912f11">)</font> x <font color="#912f11">(</font><font color="#007080">range</font> width<font color="#912f11">)\]</font>  
           <font color="#698b22">(</font>next-state <font color="#008b00">(</font><font color="#007080">get-in</font> board <font color="#912f11">\[</font>y x<font color="#912f11">\]</font><font color="#008b00">)</font> <font color="#912f11">\[</font>x y<font color="#912f11">\]</font><font color="#698b22">)</font><font color="#cdcd00">)</font>  
      <font color="#cdcd00">(</font><font color="#007080">partition</font> width<font color="#cdcd00">)</font>  
      <font color="#cdcd00">(</font><font color="#1f3f81">**map**</font> <font color="#912f11">\#(</font><font color="#007080">apply</font> <font color="#007080">str</font> <font color="#912f11">%</font><font color="#912f11">)</font><font color="#cdcd00">)</font>  
      <font color="#007080">vec</font><font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; This is straight-forward. The only tricky part is to remember that the order </font>  
<font color="#786000">; of paramaters for the get-in function and the x-y coordinates is opposite to </font>  
<font color="#786000">; each other.   </font>

<font color="#786000">; 95: Write a predicate which checks whether or not a given sequence represents</font>  
<font color="#786000">; a binary tree. Each node in the tree must have a value, a left child, and a </font>  
<font color="#786000">; right child.</font>  
<font color="#786000">; (= (\_\_ '(:a (:b nil nil) nil)) true)</font>  
<font color="#786000">; (= (\_\_ '(:a (:b nil nil))) false)</font>  
<font color="#786000">; (= (\_\_ \[1 nil \[2 \[3 nil nil\] \[4 nil nil\]\]\]) true)</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> bt? <font color="#912f11">\[</font>t<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#912f11">if</font> <font color="#ee9a00">(</font><font color="#800090">or</font> <font color="#cdcd00">(</font><font color="#007080">not</font> <font color="#698b22">(</font><font color="#007080">sequential?</font> t<font color="#698b22">)</font><font color="#cdcd00">)</font>  
          <font color="#cdcd00">(</font><font color="#800090">and</font> <font color="#698b22">(</font><font color="#007080">=</font> <font color="#077807">3</font> <font color="#008b00">(</font><font color="#007080">count</font> t<font color="#008b00">)</font><font color="#698b22">)</font>  
               <font color="#698b22">(</font>bt? <font color="#008b00">(</font><font color="#007080">second</font> t<font color="#008b00">)</font><font color="#698b22">)</font>  
               <font color="#698b22">(</font>bt? <font color="#008b00">(</font><font color="#007080">last</font> t<font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font>  
    <font color="#077807">true</font> <font color="#077807">false</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#786000">; I think one of the unit tests of the problem is wrong: </font>  
<font color="#786000">; (= (\_\_ \[1 \[2 \[3 \[4 false nil\] nil\] nil\] nil\]) false)</font>  
<font color="#786000">; why shouldn't "false" be a legal tree node, or why should leaf have to be nil? </font>

<font color="#786000">; 96: Let us define a binary tree as "symmetric" if the left half of the tree </font>  
<font color="#786000">; is the mirror image of the right half of the tree. Write a predicate to </font>  
<font color="#786000">; determine whether or not a given binary tree is symmetric.</font>  
<font color="#786000">; (= (\_\_ '(:a (:b nil nil) (:b nil nil))) true)</font>  
<font color="#786000">; (= (\_\_ '(:a (:b nil nil) nil)) false)</font>  
<font color="#786000">; (= (\_\_ \[1 \[2 nil \[3 \[4 \[5 nil nil\] \[6 nil nil\]\] nil\]\]</font>  
          <font color="#786000">;\[2 \[3 nil \[4 \[6 nil nil\] \[5 nil nil\]\]\] nil\]\]) true)</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>t<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#ee9a00">(</font><font color="#912f11">fn</font> mir? <font color="#912f11">\[</font>l r<font color="#912f11">\]</font>  
     <font color="#cdcd00">(</font><font color="#912f11">if</font> <font color="#698b22">(</font><font color="#800090">or</font> <font color="#008b00">(</font><font color="#007080">=</font> <font color="#077807">nil</font> l r<font color="#008b00">)</font>  
             <font color="#008b00">(</font><font color="#800090">and</font> <font color="#96cdcd">(</font><font color="#007080">=</font> <font color="#00688b">(</font><font color="#007080">first</font> l<font color="#00688b">)</font> <font color="#00688b">(</font><font color="#007080">first</font> r<font color="#00688b">)</font><font color="#96cdcd">)</font>  
                  <font color="#96cdcd">(</font>mir? <font color="#00688b">(</font><font color="#007080">second</font> l<font color="#00688b">)</font> <font color="#00688b">(</font><font color="#007080">last</font> r<font color="#00688b">)</font><font color="#96cdcd">)</font>  
                  <font color="#96cdcd">(</font>mir? <font color="#00688b">(</font><font color="#007080">last</font> l<font color="#00688b">)</font> <font color="#00688b">(</font><font color="#007080">second</font> r<font color="#00688b">)</font><font color="#96cdcd">)</font><font color="#008b00">)</font><font color="#698b22">)</font>  
       <font color="#077807">true</font> <font color="#077807">false</font><font color="#cdcd00">)</font><font color="#ee9a00">)</font>   
   <font color="#ee9a00">(</font><font color="#007080">second</font> t<font color="#ee9a00">)</font> <font color="#ee9a00">(</font><font color="#007080">last</font> t<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>

<font color="#786000">; 97: Pascal's triangle is a triangle of numbers computed using the following </font>  
<font color="#786000">; rules: </font>  
<font color="#786000">; - The first row is 1.</font>  
<font color="#786000">; - Each successive row is computed by adding together adjacent numbers in the </font>  
<font color="#786000">;   row above, and adding a 1 to the beginning and end of the row.  </font>  
<font color="#786000">; Write a function which returns the nth row of Pascal's Triangle.</font>  
<font color="#786000">; (= (map \_\_ (range 1 6))</font>  
   <font color="#786000">;\[     \[1\]</font>  
        <font color="#786000">;\[1 1\]</font>  
       <font color="#786000">;\[1 2 1\]</font>  
      <font color="#786000">;\[1 3 3 1\]</font>  
     <font color="#786000">;\[1 4 6 4 1\]\])</font>  
<font color="#912f11">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>n<font color="#912f11">\]</font>  
  <font color="#cd3700">(</font><font color="#007080">nth</font> <font color="#ee9a00">(</font><font color="#007080">iterate</font>   
         <font color="#cdcd00">(</font><font color="#912f11">fn</font> <font color="#912f11">\[</font>pre<font color="#912f11">\]</font>   
           <font color="#698b22">(</font><font color="#007080">vec</font>   
             <font color="#008b00">(</font><font color="#007080">concat</font>   
               <font color="#912f11">\[</font><font color="#077807">1</font><font color="#912f11">\]</font>   
               <font color="#96cdcd">(</font><font color="#1f3f81">**map**</font> <font color="#00688b">(</font><font color="#912f11">fn</font> <font color="#912f11">\[\[</font>f s<font color="#912f11">\]\]</font> <font color="#483d8b">(</font><font color="#007080">+</font> f s<font color="#483d8b">)</font><font color="#00688b">)</font> <font color="#00688b">(</font><font color="#007080">partition</font> <font color="#077807">2</font> <font color="#077807">1</font> pre<font color="#00688b">)</font><font color="#96cdcd">)</font>   
               <font color="#912f11">\[</font><font color="#077807">1</font><font color="#912f11">\]</font><font color="#008b00">)</font><font color="#698b22">)</font><font color="#cdcd00">)</font>  
         <font color="#912f11">\[</font><font color="#077807">1</font><font color="#912f11">\]</font><font color="#ee9a00">)</font>  
       <font color="#ee9a00">(</font><font color="#007080">dec</font> n<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  

</font>
