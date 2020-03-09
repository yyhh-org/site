Title: txt2tags: a Lightweight Document Authoring Format
Date: 2008-01-04 00:07
Author: Huahai
Category: notebook
Tags: GTD, Editor
Slug: txt2tags-a-lightweight-document-authoring-format
Alias: /blog/2008/01/txt2tags-lightweight-document-authoring-format
Lang: en

![txt2tags](http://txt2tags.sourceforge.net/img/t2tgems.png)

Fresh ideas often pop up when one is not working, e.g. while in shower or in bed. When that happens, one needs to jot them down fast. Of course, a piece of paper and a pen is still the best solution in term of speed. However, if a computer is conveniently available, typing in text has the advantage of saving text re-entry time, being easily re-organizable and expandable into something more substantial, such as an article. For these advantages to materialize, a good document format is needed for quick document creation and text entry. MS Word may work for many people if MS Office is the only environment they work in. For others, especially those who value portability, a platform agnostic solution would be better. Another point against a WYSIWYG editor like Word is that it mixes presentation with content, which is generally bad. When I use Word, I habitually try to adjust the font, the layout, etc, which basically interrupt text input.

Speaking of portability, plain text is without question the king. So, when we need extra features, such as structure, list, table, links and so on, we add them on top of plain text. The question now becomes how much to add? Many formats trade power over simplicity. For example, LaTeX is great, many people I know write papers with LaTeX, myself included. However, LaTeX is too complex for quick text entry. Wiki is great for documentation, but there are just too many different kinds of wiki tags for me to remember. Here, I think [txt2tags](http://txt2tags.sourceforge.net) strikes the right balance between power and simplicity.

txt2tags has a minimalist markup language. All the marks are non-word symbols (so they won't confuse spell checkers) that are fairly intuitive. For example, =this is top level section title=, ==this is second level==, +this top level title is numbered+, \*\*this text is bold\*\*, //this text is italic//, - this is a list item, + this is a numbered list item. Many of these marks are what people are already using in informal text such as email messages. There really ain't much to learn here. Compared with [other lightweight markup language](http://en.wikipedia.org/wiki/Lightweight_markup_language), I think txt2tags has the most natural syntax.

txt2tags format additionally supports tables, links, images, comments, quotations, and horizontal lines. However, cross-references and footnotes are not supported. As an initial authoring format, I think this feature set is sufficient. If more complex structures such as complicated tables, formulas, and cross-references are needed, they can be inserted at the final document production stage. At the authoring stage, there is generally no need to worry about them. If it is necessary to include them, e.g. important formula, txt2tags allows them to be inserted as already tagged code.

A single python script takes txt2tags files (\*.t2t) and converts them into different formatted documents, including LaTeX, HTML, Unix manual page, PageMaker, plain text (yes, you sometimes need them), among others. This blog is written in txt2tags and then converted to HTML. In fact, [books](http://txt2tags.sourceforge.net/writing-book.html) can be written in text2tags, because it supports multiple file includes, so each chapter can live in its own file. txt2tags can also automatically generate table of content.

As vim user, we expect niceties such as syntax highlighting and vim key-mappings for txt2tags. These can all be found on txt2tags Web site. Or if one uses Debian, these are included in the txt2tags Debian package already. For people like to have GUI, there's a Tcl/Tk GUI interface for txt2tags. And a Web interface is available too.

For quickly jotting down ideas, I have tried mind-mapping tools (freemind, kdissert), outliners (TVO, vimoutliners), and note-takers (basket, knotes). They work to some degree but are all very limited in term of content expandability and portability. I just wish I had found txt2tags earlier.

txt2tags also makes a good addition to my text based GTD solution. I will be using it as my main information collection format. Because txt2tags' list format is very compatible with [taskpaper](http://yyhh.org/blog/2007/12/simple-gtd-list-solution-desktop-web-and-possibly-mobile)'s list -- both use "-" to indicate list item, and use indention to indicate nesting level -- I can simply yank a list from a t2t file, and put it in my taskpaper project list. Nice.
