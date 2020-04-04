---
Title: Develop clojure Web applications with vim
Date: 2011-05-02 23:02
Author: Huahai
Category: notebook
Tags: Programming, Clojure, Editor, Vim
Slug: develop-clojure-web-applications-with-vim
Alias: /blog/2011/05/develop-clojure-web-applications-vim
Lang: en
---

I recently started to learn [clojure](https://clojure.org) programming. It is an interesting experience. Ever since I learned computer programming almost 20 years ago, in Pascal, on a VAX minicomputer terminal, I have not experienced this newbie sensation with a computer language. The sense of excitement and novelty is high, and the eagerness to put the language to use is higher still. So for my new project at work, I am doing it with clojure.

This is a visual analytics project, and the visual part will be on the Web. It amazes me [how much work](https://www.glenstampoultzis.net/blog/clojure-web-infrastructure/) has already been done for the Web using this 3 years old language. So it should be easy for me to get started. Here's what I have so far.

**  
Know your lein  
**

The standard build tool for clojure projects these days seems to be lein, short for [leiningen](https://github.com/technomancy/leiningen). It is just a script, download it, make it executable, put it on your path. Also make sure you have java installed. Now go to whatever directory your project will live in, run lein:

`lein new myproject`

This creates the default project structure for a project creatively named "myproject", and downloads dependencies from the Internet, including clojure itself (clojure is built on java virtual machine, so the clojure language runtime is just a jar file).

Now in the "mypoject" directory, there is a "project.clj" file. This file controls everything about the project, except the writing code part. Edit the file according to your needs. There is a very extensive [sample project.clj](https://github.com/technomancy/leiningen/blob/master/sample.project.clj) that I find very informative. My project.clj so far looks like this:

<font face="monospace" size="1em">  
<font color="#375288"> 1 </font><font color="#912f11">(</font>defproject myproject <font color="#077807">"0.0.1-SNAPSHOT"</font>  
<font color="#375288"> 2 </font>  <font color="#1f3f81">**:description**</font> <font color="#077807">"MyProject has super duper visual analytics capabilities"</font>  
<font color="#375288"> 3 </font>  <font color="#1f3f81">**:dependencies**</font> <font color="#912f11">\[\[</font>org.clojure/clojure <font color="#077807">"1.2.1"</font><font color="#912f11">\]</font>  
<font color="#375288"> 4 </font>                 <font color="#912f11">\[</font>org.clojure/clojure-contrib <font color="#077807">"1.2.0"</font><font color="#912f11">\]</font>  
<font color="#375288"> 5 </font>                 <font color="#912f11">\[</font>compojure <font color="#077807">"0.6.2"</font><font color="#912f11">\]</font>  
<font color="#375288"> 6 </font>                 <font color="#912f11">\[</font>hiccup <font color="#077807">"0.3.4"</font><font color="#912f11">\]</font>  
<font color="#375288"> 7 </font>                 <font color="#912f11">\[</font>ring <font color="#077807">"0.3.7"</font><font color="#912f11">\]</font>  
<font color="#375288"> 8 </font>                 <font color="#912f11">\[</font>commons-logging <font color="#077807">"1.1.1"</font><font color="#912f11">\]</font>  
<font color="#375288"> 9 </font>                 <font color="#912f11">\[</font>org.apache.lucene/lucene-core <font color="#077807">"3.1.0"</font><font color="#912f11">\]</font>  
<font color="#375288">10 </font>                 <font color="#912f11">\[</font>xalan <font color="#077807">"2.7.1"</font><font color="#912f11">\]</font>  
<font color="#375288">11 </font>                 <font color="#912f11">\[</font>javaewah <font color="#077807">"0.1.0"</font><font color="#912f11">\]</font>  
<font color="#375288">12 </font>                 <font color="#912f11">\[</font>com.my.work/secret-lib1 <font color="#077807">"0.3.4b"</font><font color="#912f11">\]</font>  
<font color="#375288">13 </font>                 <font color="#912f11">\[</font>com.my.work/secret-lib2 <font color="#077807">"0.1.0"</font><font color="#912f11">\]\]</font>  
<font color="#375288">14 </font>  <font color="#1f3f81">**:dev-dependencies**</font> <font color="#912f11">\[\[</font>lein-ring <font color="#077807">"0.4.0"</font><font color="#912f11">\]</font>  
<font color="#375288">15 </font>                     <font color="#786000">;\[org.clojars.autre/lein-vimclojure "1.0.0"\]</font>  
<font color="#375288">16 </font>                     <font color="#912f11">\[</font>clj-stacktrace <font color="#077807">"0.2.1"</font><font color="#912f11">\]\]</font>   
<font color="#375288">17 </font>  <font color="#1f3f81">**:repositories**</font>   
<font color="#375288">18 </font>            <font color="#912f11">{</font><font color="#077807">"myrepo"</font>   
<font color="#375288">19 </font>             <font color="#912f11">{</font><font color="#1f3f81">**:url**</font>   
<font color="#375288">20 </font>              <font color="#077807">"<https://myrepo.my.com:8080/artifactory/libs-release-local>"</font><font color="#912f11">}}</font>  
<font color="#375288">21 </font>  <font color="#1f3f81">**:source-path**</font> <font color="#077807">"src/clojure"</font>  
<font color="#375288">22 </font>  <font color="#1f3f81">**:java-source-path**</font> <font color="#077807">"src/java"</font>  
<font color="#375288">23 </font>  <font color="#1f3f81">**:warn-on-reflection**</font> <font color="#077807">true</font>  
<font color="#375288">24 </font>  <font color="#786000">;:main com.my.myproject.runtime.core)</font>  
<font color="#375288">25 </font>  <font color="#1f3f81">**:ring**</font> <font color="#912f11">{</font><font color="#1f3f81">**:handler**</font> com.my.myproject.runtime.core/app<font color="#912f11">})</font>  
</font>

Let me explain line by line. The first line is the project name and the current version number (using the so called [semantic versioning](https://semver.org) scheme).

The third line starts the dependencies definition. These dependencies are libraries written in jvm languages such as java or clojure. lein will automatically find and download them from public repositories if they are publicly available. This is the case for libraries referred in line 3 - 10, where the last three libs are open source java libs and the rest are open source clojure libs: [compojure](https://github.com/weavejester/compojure) is a lightweight Web framework, which builds upon [ring](https://github.com/mmcgrana/ring), which abstract HTTP into a simple API, [hiccup](https://github.com/weavejester/hiccup) allows one to write html in clojure syntax.

The lib on line 11 is also open source, however, it has not been packaged by the author and submitted to a pubic repository, so lein will not be able to find it. What I did was to package it as a jar file myself and deploy it to a private repository I setup for my team, so my team members can all access to the same libs without needing to commit the libs to our version control system, which is not suitable for handling binary data. This private repository is defined on line 17 to 20. Here the repository server is a standard installation of [artifactory](https://www.jfrog.com/products.php). The libs on line 12 and 13 are our in-house developed java libraries, which are deployed the same way.

By default, lein expect clojure code in "myproject/src". Since we will be mixing java code and clojure code, we put them in separate folders. These are defined in line 21 and 22.

Line 14 starts the dev-dependencies. These are the dependencies for developers' convenience and will not be included in the final product. [lein-ring](https://github.com/weavejester/lein-ring) is a plugin for facilitating Web development in clojure that utilizes ring. Basically, it adds a ring command for lein. For example,

`lein ring server-headless`

will start a jetty server with the Web app running on port 3000 (default). The Web app is defined on line 25, which is just a simple app to show a greeting in this case. The code consists of two files. core.clj defines the main routing table for the Web app:

<font face="monospace">  
<font color="#375288"> 1 </font><font color="#912f11">(</font><font color="#800090">ns</font> com.my.myproject.runtime.core  
<font color="#375288"> 2 </font>  <font color="#cd3700">(</font><font color="#1f3f81">**:use**</font> compojure.core  
<font color="#375288"> 3 </font>        hiccup.middleware  
<font color="#375288"> 4 </font>        com.my.myproject.runtime.views<font color="#cd3700">)</font>  
<font color="#375288"> 5 </font>  <font color="#cd3700">(</font><font color="#1f3f81">**:require**</font> <font color="#912f11">\[</font>compojure.route <font color="#1f3f81">**:as**</font> route<font color="#912f11">\]</font>  
<font color="#375288"> 6 </font>            <font color="#912f11">\[</font>compojure.handler <font color="#1f3f81">**:as**</font> handler<font color="#912f11">\]</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#375288"> 7 </font>  
<font color="#375288"> 8 </font><font color="#912f11">(</font>defroutes main-routes  
<font color="#375288"> 9 </font>  <font color="#cd3700">(</font>GET <font color="#077807">"/"</font> <font color="#912f11">\[\]</font> <font color="#ee9a00">(</font>index-page<font color="#ee9a00">)</font><font color="#cd3700">)</font>  
<font color="#375288">10 </font>  <font color="#cd3700">(</font>route/not-found <font color="#ee9a00">(</font>page-404<font color="#ee9a00">)</font><font color="#cd3700">)</font>  
<font color="#375288">11 </font>  <font color="#cd3700">(</font>route/resources <font color="#077807">"/"</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#375288">12 </font>  
<font color="#375288">13 </font><font color="#912f11">(</font><font color="#912f11">def</font> app  
<font color="#375288">14 </font>  <font color="#cd3700">(</font><font color="#800090">-&gt;</font> <font color="#ee9a00">(</font>handler/site main-routes<font color="#ee9a00">)</font>  
<font color="#375288">15 </font>      <font color="#ee9a00">(</font>wrap-base-url<font color="#ee9a00">)</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
</font>

views.clj defines the pages to show:

<font face="monospace">  
<font color="#375288"> 1 </font><font color="#912f11">(</font><font color="#800090">ns</font> com.my.myproject.runtime.views  
<font color="#375288"> 2 </font>  <font color="#cd3700">(</font><font color="#1f3f81">**:use**</font> <font color="#912f11">\[</font>hiccup core page-helpers<font color="#912f11">\]</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#375288"> 3 </font>  
<font color="#375288"> 4 </font><font color="#912f11">(</font><font color="#800090">defn</font> index-page <font color="#912f11">\[\]</font>  
<font color="#375288"> 5 </font>  <font color="#cd3700">(</font>html  
<font color="#375288"> 6 </font>    <font color="#912f11">\[</font><font color="#1f3f81">**:head**</font>   
<font color="#375288"> 7 </font>     <font color="#912f11">\[</font><font color="#1f3f81">**:title**</font> <font color="#077807">"Welcome"</font><font color="#912f11">\]</font>   
<font color="#375288"> 8 </font>     <font color="#912f11">(</font>include-css <font color="#077807">"/css/style.css"</font><font color="#912f11">)\]</font>  
<font color="#375288"> 9 </font>    <font color="#912f11">\[</font><font color="#1f3f81">**:body**</font>  
<font color="#375288">10 </font>     <font color="#912f11">\[</font><font color="#1f3f81">**:h1**</font>   
<font color="#375288">11 </font>       <font color="#077807">"Hello World!"</font><font color="#912f11">\]\]</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
<font color="#375288">12 </font>  
<font color="#375288">13 </font><font color="#912f11">(</font><font color="#800090">defn</font> page-404 <font color="#912f11">\[\]</font>  
<font color="#375288">14 </font>  <font color="#cd3700">(</font>html  
<font color="#375288">15 </font>    <font color="#912f11">\[</font><font color="#1f3f81">**:head**</font>   
<font color="#375288">16 </font>     <font color="#912f11">\[</font><font color="#1f3f81">**:title**</font> <font color="#077807">"Sorry"</font><font color="#912f11">\]</font>   
<font color="#375288">17 </font>     <font color="#912f11">(</font>include-css <font color="#077807">"/css/style.css"</font><font color="#912f11">)\]</font>  
<font color="#375288">18 </font>    <font color="#912f11">\[</font><font color="#1f3f81">**:body**</font>  
<font color="#375288">19 </font>     <font color="#912f11">\[</font><font color="#1f3f81">**:h1**</font> <font color="#077807">"Page not found"</font><font color="#912f11">\]\]</font><font color="#cd3700">)</font><font color="#912f11">)</font>  
</font>

One very nice thing about lein-ring is that it will automatically pick up any changes made in the project. That's right, live changes, no need to wait for the code to compile, restart the server, etc, just refresh the browser and you will see the changes. This is extremely convenient for Web development, especially for experimentation in clojure REPL.

**vimclojure**

I am a vi addict. For my fix, there is a [vimclojure](https://www.vim.org/scripts/script.php?script_id=2501) plugin for clojure development with vim. To have dynamic features such as code snippet evaluation, code completion etc, there is a need to start a nailgun server so vimclojure can contact with a clojure REPL. This script is what I use:

<font face="monospace" size="1em">  
<font color="#375288"> 1 </font><font color="#786000">\# clojure jar is also installed in ~/.vim/lib</font>  
<font color="#375288"> 2 </font><font color="#007080">CL\_CP</font>=.:~/.vim/lib/\*  
<font color="#375288"> 3 </font>  
<font color="#375288"> 4 </font><font color="#1f3f81">**if** </font><font color="#1f3f81">**\[**</font> <font color="#1f3f81">**-f**</font> <font color="#1f3f81">**"**</font><font color="#077807">project.clj</font><font color="#1f3f81">**"**</font> <font color="#1f3f81">**\]**</font><font color="#1f3f81">**;**</font> <font color="#1f3f81">**then**</font>  
<font color="#375288"> 5 </font>  <font color="#007080">CP</font>=<font color="#912f11">\`lein classpath\`</font>:<font color="#1f3f81">**"**</font><font color="#800090"> $CL\_CP</font><font color="#1f3f81">**"**</font>  
<font color="#375288"> 6 </font><font color="#1f3f81">**else**</font>  
<font color="#375288"> 7 </font>  <font color="#007080">CP</font>=<font color="#1f3f81">**"**</font><font color="#800090"> $CL\_CP</font><font color="#1f3f81">**"**</font>  
<font color="#375288"> 8 </font><font color="#1f3f81">**fi**</font>  
<font color="#375288"> 9 </font>  
<font color="#375288">10 </font><font color="#1f3f81">**if** </font><font color="#1f3f81">**\[**</font> <font color="#800090"> $\#</font> <font color="#1f3f81">**-eq**</font> <font color="#077807">0</font> <font color="#1f3f81">**\]**</font><font color="#1f3f81">**;**</font> <font color="#1f3f81">**then**</font>   
<font color="#375288">11 </font>     <font color="#1f3f81">**exec**</font> java -server -cp <font color="#1f3f81">**"**</font><font color="#800090"> $CP</font><font color="#1f3f81">**"**</font> vimclojure.nailgun.NGServer <font color="#077807">127</font>.<font color="#077807">0</font>.<font color="#077807">0</font>.<font color="#077807">1</font>  
<font color="#375288">12 </font><font color="#1f3f81">**else**</font>  
<font color="#375288">13 </font>     <font color="#1f3f81">**exec**</font> java -server -cp <font color="#1f3f81">**"**</font><font color="#800090"> $CP</font><font color="#1f3f81">**"**</font> vimclojure.nailgun.NGServer <font color="#800090"> $1</font>   
<font color="#375288">14 </font><font color="#1f3f81">**fi**</font>  
</font>

I normally run this script in the root directory of the project, this allows "lein classpath" to pick up all the classpaths for the REPL session. There's also a lein-vimclojure plungin that will install vimclojure and start a nailgun server for you, but I found it does not load "user.clj", so my convenient functions defined there are not autoloaded. I will stick to my script.

For better navigation of clojure source code, vim users need [TagList](https://www.vim.org/scripts/script.php?script_id=273) plugin. The plugin does not automatically work with clojure though. [This blog post](https://kuriqoo.blogspot.com/2011/02/using-clojure-in-vim.html) has a solution, and it worked for me. Basically, this tells TagList to treat clojure code just like other Lisp code, which it is.

That's all folks.
