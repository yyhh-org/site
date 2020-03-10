---
Title: Display LaTeX Math on Drupal with MathJax
Date: 2011-07-18 20:19
Author: Huahai
Category: notebook
Tags: SysAdmin, Drupal, Math, LaTeX
Slug: display-latex-math-on-drupal-with-mathjax
Alias: /blog/2011/07/display-latex-math-drupal-mathjax
Lang: en
---

[MathJax](http://www.mathjax.org/) seems to be the emerging standard for displaying math on the Web at this moment. It is supported by American Mathematical Society and American Physical Society, and has already been adopted by major math related discussion venues such as Physics Forums and Stack Exchange. MathJax displays math using CSS and Web fonts instead of images, so the quality is very high and is resize-friendly. Below are some examples:

Inline math: the geometric product $\boldsymbol{uv}$ of vectors $\boldsymbol{u}$ and $\boldsymbol{v}$ is $\boldsymbol{u}\cdot\boldsymbol{v} + \boldsymbol{u}\wedge\boldsymbol{v}$, where $\boldsymbol{u}\cdot\boldsymbol{v}$ is the inner product and $\boldsymbol{u}\wedge\boldsymbol{v}$ is the outer product. 

Display math: the rotation of vector $\boldsymbol{u}$ by angle $\theta$ in plane $\boldsymbol{i}$ is $$R_{\boldsymbol{i}\theta}(\boldsymbol{u}) = e^{-\boldsymbol{i}\theta/2}\boldsymbol{u}e^{\boldsymbol{i}\theta/2}$$

Some random expressions copied directly from the [short math guide for latex](ftp://ftp.ams.org/ams/doc/amsmath/short-math-guide.pdf): $$\begin{pmatrix}
\alpha& \beta^{*}\\
\gamma^{*}& \delta
\end{pmatrix}$$ $$\frac{{\displaystyle\sum_{n &gt; 0} z^n}}
{{\displaystyle\prod_{1\leq k\leq n} (1-q^k)}}$$ $$2^k-\binom{k}{1}2^{k-1}+\binom{k}{2}2^{k-2}$$

Finally, an obligatory integral: $$\int \!\!\! \int_D f(x,y)\,dx\,dy$$

The math input could be either LaTeX or MathML, embedded in regular HTML text. MathJax is a Javascript library, so it works at the browser's side. After the HTML is rendered, the MathJax code scans the output, find pieces of text marked by user defined math delimiters (more on that later), and replaces them by typesetted math. The math may take a couple of seconds to show up depending on the browser and the network speed. The MathJax library can be fetched from content delivery network (CDN), so it is fairly simple to add MathJax to any Web site. Here is how I did it for this Drupal 6 site.

There is a [Drupal module for MathJax](http://drupal.org/project/mathjax) that loads MathJax from CDN for every Drupal page. The module also allows Drupal pages to be selectively MathJax enabled according to some URL patterns. By default, all pages are MathJax enabled except for these paths: *admin/*, node/add/*, node/*/edit/*, which is reasonable. However, path based selective enabling is still a bit crude, because most pages would not contain math, so MathJax simply slows down page rendering for most pages without any benefit. It would be great if the selection can also be tag based, so only the posts tagged as "math" and maybe the front page need to incur such slow down. Another useful feature would be to allow MathJax configuration within the module. The default configuration of MathJax is not very reasonable for Drupal, <span style="text-decoration: line-through">so users have to add the configurations manually to the page template at this time</span>. **Updated Aug.25, 2011:** Julou, the author of the module, has responded to my feature request and added a text area for MathJax configuration in the development version of the module. I have tested it and it works.

One of the most annoying default settings of MathJax is the definition of math delimiters. For inline math, the default delimiters are ( ), and for math on its own line, the default delimiters are [ ].  Because ( ) and [ ] are so commonly used in regular non-math text, this default setting is unreasonable for Drupal, as MathJax will remove the parentheses and change the text font to be math like for a Drupal page. Double dollar sign is okay, but to show the regular dollar sign properly, it needs to be escaped by reverse backslash, which is not the default setting of MathJax. Also, the default message display of MathJax is a bit too much for my taste, and I minimized them a bit.

If your site has the [print module](http://drupal.org/project/print) installed, you need to copy the file *print.tpl.php* to your theme templates directory, and add the same as above so the print friendly version also show math properly. 

For more MathJax configuration options, please refer to the [MathJax documentation](http://www.mathjax.org/docs/1.1/configuration.html)

