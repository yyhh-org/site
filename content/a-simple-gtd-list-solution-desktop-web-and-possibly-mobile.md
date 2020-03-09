Title: A Simple GTD List Solution: Desktop, Web and Possibly Mobile
Date: 2007-12-10 04:25
Author: Huahai
Category: notebook
Tags: GTD, Editor, Vim
Slug: a-simple-gtd-list-solution-desktop-web-and-possibly-mobile
Alias: /blog/2007/12/simple-gtd-list-solution-desktop-web-and-possibly-mobile
Lang: en

I have been searching for a lightweight list solution since I started trying out the [Getting Things Done (GTD)](http://en.wikipedia.org/wiki/Getting_Things_Done) approach a few days ago. Unlike calendar events, list items (projects and actions) do not associate with a particular time and date, therefore, using a calender for them is not appropriate. According to [David Allen](http://www.davidco.com/), for lists, we should "just go for simplicity, speed, and fun". Here I operationalize that into these properties:

* Simple, but can still do these:

      - Handle lists for "project", "next-action", "waiting-for" and "maybe"
      - Be able to tag an item with "context", and organize items by context
      - Support sub-list


* Quick and easy input, review, and operate, whenever, wherever

      - Platform and location independent: home, office, road, online, offline
      - Synchronized and consistent
      - Preserve persistence and ownership (lists live else where won't do)
      - Easily searchable
      - Integrated with work environment (e.g. maintain reference to support materials)


* Good-looking, functional, familiar and consistent interface


This set of desiderata is of course incomplete, just what I can think of right now. All these can actually be comfortably handled by paper based solutions for most people I think. However, for people whose primary work environment is digital, the second major item is not very amicable for a paper based solution, because getting things transferred between digital and paper world is a lot of hassle. If the input and output of one's work are all in the digital environment, it becomes necessary to avoid the paper world, and to find an all digital solution to get things done. At this point, I think I found a simple solution, [TaskPaper](http://hogbaysoftware.com/products/taskpaper).

*TaskPaper* is a Mac based list software. I do not own a Mac, so why is it my solution? Well, TaskPaper uses a very simple and intuitive syntax representing lists in plain text. That is to say, they stick to the basics, and try to take what's good about paper-based solution, and bring that to digital world. Since plain text is the most platform independent format, portability is not a problem any more. Easy and quick input is taken care of with a good text editor. Searchability, persistence, and synchronization is easy to achieve with textual data. So there you have it, a solution that meets all the desiderata.

Wait, how about its support for GTD? Here, TaskPaper's syntax is specifically tailored to GTD. Nothing more. Let's see an example:  

<font face="monospace">  
**<span class="underline">Example Project:</span>**  
<font color="#bebebe">- Start example project file @computer @done</font>  
<font color="#5b3674">*-* </font>Brainstorm project with colleagues <font color="#5b3674">*@work*</font>  
<font color="#5b3674">*-* </font>Email Joan about project <font color="#5b3674">*@email*</font>  
**<span class="underline">Next Project:</span>**  
<font color="#5b3674">*-* </font>Draft ideas for next project <font color="#5b3674">*@anywhere*</font>  
<font color="#5b3674">*-* </font>Email Bob to arrange meeting <font color="#5b3674">*@email*</font>  
</font>

This list contains two projects. Project names end with ":". Tasks in a project start with "-". Context tags start with "@". "@done" is a special tag indicating completion of a task. That's it. All the syntax for TaskPaper! I don't think it can be made simpler, and everyone should be able to pick it up in no time. In addition, the possibility of customizing the format to suit one's own needs seems to be very high. For example, [wiki words](http://en.wikipedia.org/wiki/Personal_wiki) can be naturally included in the list to handle reference to project support materials.

For vim user, there's a [taskpaper.vim](http://www.vim.org/scripts/script.php?script_id=2027) plugin that makes it a little easier to edit and review TaskPaper lists. The current released version of taskpaper.vim doesn't seem to correctly handle indented tasks due to a quotation peculiarity of vim regular expression. I have sent a small patch below to the author of taskpaper.vim (update12/10/2007 10:49:08 PM (EST): it will be included in the next release, I am told).

<font face="monospace">  
<font color="#e5a00d">*--- taskpaper.vim 2007-09-25 07:33:28.000000000 -0400*</font>  
<font color="#e5a00d">*+++ taskpaper.vim.new 2007-12-09 08:20:06.000000000 -0500*</font>  
<font color="#007020">**@@ -36,7 +36,7 @@**</font>  
   
 " toggle @done context tag on a task  
 function! ToggleDone()  
<font color="#70a0d0">*-    if (getline(".") =~ "^\\s\*- ")*</font>  
<font color="#5b3674">*+    if (getline(".") =~ '^\\s\*- ')*</font>  
         let isdone = strridx(getline("."),"@done")  
         if (isdone != -1)  
             substitute/ @done//  
<font color="#007020">**@@ -45,7 +45,10 @@**</font>  
             substitute/$/ @done/  
             echo "done!"  
         endif  
<font color="#5b3674">*+    else* </font>  
<font color="#5b3674">*+        echo "not a task."*</font>  
     endif  
<font color="#5b3674">*+*</font>  
 endfunction  
   
 map &lt;buffer&gt; &lt;LocalLeader&gt;td :call ToggleDone()&lt;cr&gt;  
</font>

There is also a [taskpaper.web](http://code.google.com/p/taskpaper-web/) that you can drop in your own php-supported Web site. This is useful when you do not have access to your desktop but have access to your own Web site. Of course, then you have to set up file synchronization between the Web copy of your lists and your desktop or mobile copies. For the former, you can run a *cron* job to regularly *rsync* these files. For the later, I am not sure since I no longer use a PDA or smart phone (it's funny that I was among the first generation of Palm users, but I no longer use any of these when they become so popular nowadays. I just carry my laptop around).

Anyway, I just started experimenting with this methods for GTD lists. I will have more to say when I got more experience using it.

\*For the meaning of some of the GTD terms, it's best to read [the book](http://www.amazon.com/Getting-Things-Done-Stress-Free-Productivity/dp/0142000280).
