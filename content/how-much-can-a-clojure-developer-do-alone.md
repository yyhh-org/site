---
Status: published
Lang: en
Title: How much can a Clojure developer do alone?
Date: 2021-03-23T17:45:35.382Z
Author: Huahai
Category: opinion
Tags: Clojure
---
Someone [asked on Reddit this question](https://www.reddit.com/r/Clojure/comments/mbil51/how_much_can_a_clojure_developer_do_alone/), for he's wondering if it is worth the time to learn Clojure well. He has dabbled in Clojure for half a year, but was not convinced of its benefits. He has not used REPL much, and was wondering if he was doing something wrong. He additionally has some related questions about the Clojure and functional programming in general, here are my two cents of an answer.

## I am not using the REPL much, am I doing something wrong?

Yes, if you are not using the REPL, you are not doing Clojure right. That's the answer. It may not be what one likes to hear, but it is true.

There are already a lot of blog posts and Youtube videos about what it means to be "using the REPL" in Clojure, or in Lisp in general. None of them articulated the points from a Human-computer Interaction point of view. As someone who earned a Ph.D. in that field, I think I am qualified to make this point.  

First, "using the REPL" does NOT mean typing your code in REPL. Heck, no, it's the opposite. 

"Using the REPL" actually means typing your code in your favorite editor. However, one sends the code to evaluate in a REPL, which may not even be visible at all. Once the code is evaluated, the results immediately show up in the editor, so you get the feedback right away. Obviously, this requires some upfront setup, but a proper Clojure REPL setup exists in all major editors. Just google it.

Note that one normally sends the code to evaluate with a single key stroke. Note also, a very important point that people often miss, is that this "sending code to evaluate" is uniquely convenient in Lisp because of the parentheses. 

There's a notion of "form" in Lisp, that is the code enclosed between a pair of parentheses, which can be independently evaluated. So, when next time someone insists that their favorite non-Lisp language also has a REPL, ask them, does it have a notion of "form"? 

The benefit of a form, is that one no longer needs to use a mouse or some awkward key combinations to painstakingly select a region of code first, before sending it out for evaluation. Instead, one can use a single key stroke that means "evaluate the form under the cursor", or "evaluate the form before the cursor", etc, to precisely define the scope and send the code at the same time. 

As someone who has published papers in human motor controls, I can assure you this simplification makes a huge difference in ergonomics. It reduces the cost of using a REPL significantly, to the extent, I would venture to estimate that half of the potential productivity gains (if any) of the Lisp family of languages come from using the REPL this way.

Psychologically, using REPL this way improves the [flow](https://en.wikipedia.org/wiki/Flow_(psychology)), the complete immersion in one's activity without interruption. No wonder [Clojure programmers is found to the happiest](https://www.computerworld.com/article/2693998/clojure-developers-are-the-happiest-developers.html): a mental state of flow improves well-being and life satisfaction.

Please, do yourself a favor, go learn and practice the skills of REPL-driven programming in Clojure. There are many [videos](https://www.google.com/search?q=repl+driven+programming+video) that show how it is done.

## Can I learn Clojure well all by myself?

For this one, my opinion is "probably not".

As alluded to above, significant amount of "doing Clojure right" is about some tiny bits of seemly unimportant things, but they add up. That's why I hold this unpopular opinion among Clojurians that Clojure is not a particularly good language for self-learning, unless one is very good at self-starting, which is not the case for the vast majority of people.

Most people need some trainings to be able to get into something new. If they have not been taught REPL driven programming, I don't think they can discover it by themselves, despite maybe hearing others talking about it constantly. Heck, if left alone, there are people who would complain about having to count parentheses, rather than taking the initiative to find tools to help themselves, for which there are plenty of options, e.g. paredit, smartparens, parinfer, and so on.

On the other hand, I seldom had any problems turning my fresh college graduates new hires into competent Clojure programmers within less than a month. The differences are two fold:

Pride. Fresh college graduates have none. When they encountered obstacles, they just ask questions or try harder, instead of going to the easier route of blaming the technology. Clojure is a particularly easy target to blame: It's niche, a Lisp, a JVM language, dynamic typing, etc, the list can go on and on.

Training. I made sure that my fresh college graduates were trained, down to the development environment setup. They also start working on a good code base right away. So they pick up the right habits at the beginning and never have to experience the kind of detours a self learner has to go through. There are lots of habits and setups that experienced Clojurians take for granted, but one has to see them to even know about them.

So what's the solution? I don't know. The only thing I can think of, is hoping that more Clojure shops are successful so we can hire more people, or Clojure finds a niche that it occupies fully so that when the time comes for that niche to explode, Clojure grows accordingly. 

For whoever is reading this though, the situation is much better, because you are already reaching out and are not trying to learn all by yourself. The Clojure community is one of the nicest programming language communities. People are very  welcoming to newcomers and are very helpful. Please reach out and get help. Here are some sites to get you started:

* [Clojurian Slack](http://clojurians.net/)
* [Clojureverse](https://clojureverse.org/)
* [Clojure Reddit](https://www.reddit.com/r/Clojure/)

## How much can a Clojure developer do alone? 

Now back to the main question, how productive can a Clojure programmer become? There are also a few related questions, I will answer one by one. 

### Does it really make such a difference to use Clojure? 

Yes, it really makes a huge difference to use Clojure. Think of it this way, Clojure is a language designed for software consultants by software consultants. Cognitect, the company behind Clojure, was a software consultancy, now acquired by a bank. Clojure is also ideal for a startup, where a couple of competent Clojure programmers can write a complex application that would took a huge team of developers in other languages years of work. For my startup, our clients always thought we had a 30+ person engineering team when we have had never more than half a dozen developers.

### How much faster does it made you develop software?  And in which areas? Did it improve performance because of easier composability? Did it made the code easier to understand because of the "better" abstractions once you got firm with them?"

All of the above. Composability, easier to understand, better abstraction, etc.

It is much faster to develop in Clojure. The language creator, Rich Hickey, made all the design choices to ensure that a software consultant can deliver good software in as short as possible time frame, so that this software consultant can make the most profit. For a software consultant, time is the main cost, so time to market is optimized in Clojure.

Technically, Clojure adds to Lisp the novel ingredients of immutable data, which significantly simplifies software development. There is no other language that places such an emphasis on programming directly with plain and naked data literals. Think of programming as [working with a richer JSON format](https://yyhh.org/blog/2016/12/data-oriented-programming-dop/) without all that serializations and transformations. How nice would that be? Well, that's exactly what Clojure programming is like.

Another important point is that Clojure is a very concise language.  [Empirical data](https://www.researchgate.net/publication/316922118_An_Investigation_of_the_Relationships_between_Lines_of_Code_and_Defects) shows that one of the only things reliably correlated with software quality is the number of lines of code. The more lines of code, the more bugs there will be. Clojure is one of the only four languages where language choices is statistically significantly correlated with software quality in [this large scale study](https://arxiv.org/pdf/1901.10220.pdf). The other two "good" languages are found to be Haskell and Ruby, the one "bad" language is C++, while Clojure has the highest statistical significance number on the "good" side. 

### Could you possibly develop a complex enterprise software in Clojure with just say 4-8 people, knowing Clojure really well?

Of course. It is not just possible, but it is also optimized for it. Clojure was developed to write complex enterprise software where user requirements are arbitrary and constantly changing. Please watch any of the [many Rich Hickey's videos](https://github.com/tallesl/Rich-Hickey-fanclub), as he articulated the motivation well. Plenty of big enterprises are taking advantage of Clojure, e.g. Amazon, Walmart, and so on. 

Personally, knowing Clojure let me dare to do more ambitious things. For example, I wouldn't have started [my company](https://juji.io) if I had not known Clojure. Before we had employees, I alone wrote the core of our chatbot platform, including a compiled domain specific language and its runtime, plus the Web front end and backend. With a small team, we had written and re-written the business facing Web application several times, which includes a no-code designer UI and an online IDE. We also have an API for programmers. All these development are done in Clojure, except some machine learning pieces done in Python.

## Here's my concern: I felt like, once you got functions on which other functions also depend on and expect a certain signature, you would also get a tree-like complexity where you have to scratch your head for a while to figure out how to solve it. And if the code base gets large enough, I can imagine that understanding the code and all the context just gets equally complex. 

The real situation in Clojure is actually a lot better than your imagination, because the immutable data localizes all functionalities, so one never has to look at the whole dependency graph to understand the code or to solve a problem. This is not something that can be said for Java-like object oriented programming, where functionalities are spread out into many layers of abstractions and into many objects.

A properly structured Clojure code base uses a few namespaces of pure functions. I tend to avoid many tiny files with only a few functions in them. We are not writing Java, after all. Instead, group related functions into a large file, so that one seldom needs to look over multiple files to change something. 

Again, I stress that in Clojure, because most functions are pure and dealing with immutable data, one does not need to keep all the complexity of the whole application in the head in order to solve problems. One mostly works locally. 

In my opinion, Clojure programming is different only in the small. Programming in the large, like software architecture, is mostly similar to other languages. The only thing of note, is that one may place more focus on pure data when designing the APIs [see e.g. my diff oriented architecture talk](https://youtu.be/n-avEZHEHg8). 

Finally, let me reveal a little publicized secret of programming. To navigate large code base, in addition to the usual "go to definition" hot keys in your IDEs or editors, a good programmer, in any language, relies heavily on text search, even in their own code bases. This is a skill that experienced coders tend not to talk publicly a lot about. So please know the searchers of your editor very very well, be it grep, silver, platinum, or whatever.

## What are the key skills a Clojure developer has to develop to gain from that language?

Having humility and ambition at the same time. The humility to know there is a lot to learn and the ambition to dare to do things that most thought impossible.

