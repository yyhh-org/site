Title: Switching to Spacemacs from Vim for Clojure/ClojureScript Development
Date: 2015-08-13 06:00
Author: Huahai
Category: opinion
Tags: Editor, Spacemacs, Programming, Clojure 
Slug: switching-to-spacemacs-from-vim-for-clojureclojurescript-development
Alias: /blog/2015/08/switching-spacemacs-vim-clojure-clojurescript-development
Lang: en

Clojure has been my primary programming language for a couple of years now. During this period, I have relied on my trusty Vim text editor as the development environment. Coding Clojure in Vim had been an enjoyable experience with these excellent Vim plugins:

1.  [vim-clojure-static](https://github.com/guns/vim-clojure-static)
2.  [fireplace.vim](https://github.com/tpope/vim-fireplace)
3.  [paredit.vim](http://www.vim.org/scripts/script.php?script_id=3998)
4.  [Rainbow Parentheses Improved](https://github.com/luochen1990/rainbow)
5.  [vim-clojure-highlight](https://github.com/guns/vim-clojure-highlight)
6.  [vim-cljfmt](https:://github.com/venantius/vim-cljfmt)

So, why am I switching? Well, Clojure is, after all, a LISP. The tooling coverage for Clojure in the LISP's natural habitat, Emacs, is simply more complete than in Vim. I did not realize the extent of the discrepancy until last week, when some guys in the Clojure meetup demonstrated impressive refactoring features of their Emacs Clojure development environment.

To be fair, fireplace is doing an adequate job of supporting the most of dynamic features necessary for Clojure programming: code evaluation, documents lookup, tests and so on. I have been productive with it in the last couple of years. On the other hand, as my projects grow bigger and more complex, better support for debugging and refactoring seems to become desirable. These capabilities exist in Emacs.

Of course, I am not about to give up the Vim style text editing. As a HCI researcher in my previous life, I know that theoretically, Vim style text editing is simply better than text editing with GUI and a mouse, because Fitts' Law is real and it hurts. In addition, the superiority of modal editor vi over non-modal editor emacs for text editing has been empirically established as far back as 1983<a href="#footnote1_e69wwp8" id="footnoteref1_e69wwp8" class="see-footnote" title="Poller, M.F., Garter, S.K. A Comparative Study of Moded and Modeless Text Editing by Experienced Editor Users. In Proceedings of CHI &#39;83, pp 166-170">1</a>.

For my case, an ideal situation would be to keep the text editing style of Vim, but use it in Emacs to get the benefit of extensive Clojure support. Not surprisingly, plenty of people have worked towards such solutions. The latest effort is in the form of [spacemacs](https://github.com/syl20bnr/spacemacs), a fantastic open source project that is enjoying an outpouring enthusiasm from the community, earning more than 3000 github stars in a very short time.

I had to try it. Try as I did. And I can say that I am not disappointed.

To be honest, the on-boarding process left a lot to be desired. First, on OSX, there's already a default installation of emacs, which would not work with spacemacs. The recommended homebrew installation of emacs is simple enough, but one needs to rename the default emacs and make the homebrew one the default. This is not mentioned in the guide.

I found configuring the editor to be surprisingly easy, considering I knew nothing about emacs before (other than the key combination to quit from one). The majority of the Vim key bindings I tried work as desired. The ones that did not work are not hard to change. Within a couple of hours, I have managed to create a configuration that replicates most of the key bindings of paredit.vim, which I need to be productive coding Clojure. Here are my `dotspacemacs/config` to achieve these and more.

<font face="monospace"><font color="#9a7200">(</font><font color="#719899">**defun**</font> remove-background-color <font color="#9a7200">()</font>  
  <font color="#009799">"Useful for transparent terminal."</font>  
  <font color="#9a7200">(</font><font color="#719899">**unless**</font> <font color="#9a7200">(</font>display-graphic-p <font color="#9a7200">(</font>selected-frame<font color="#9a7200">))</font>  
    <font color="#9a7200">(</font>set-face-background <font color="#9a7200">'</font><font color="#9a7599">default</font> <font color="#009799">"unspecified-bg"</font> <font color="#9a7200">(</font>selected-frame<font color="#9a7200">))))</font>  
<font color="#9a7200">(</font><font color="#719899">**defun**</font> dotspacemacs/config <font color="#9a7200">()</font>  
  <font color="#009799">"Configuration function.</font>  
<font color="#009799"> This function is called at the very end of Spacemacs initialization after</font>  
<font color="#009799">layers configuration."</font>  
  <font color="#719872">;; Make evil-mode up/down operate in screen lines instead of logical lines</font>  
  <font color="#9a7200">(</font>define-key evil-motion-state-map <font color="#009799">"j"</font> <font color="#9a7200">'</font><font color="#9a7599">evil-next-visual-line</font><font color="#9a7200">)</font>  
  <font color="#9a7200">(</font>define-key evil-motion-state-map <font color="#009799">"k"</font> <font color="#9a7200">'</font><font color="#9a7599">evil-previous-visual-line</font><font color="#9a7200">)</font>  
  <font color="#719872">;; Also in visual mode</font>  
  <font color="#9a7200">(</font>define-key evil-visual-state-map <font color="#009799">"j"</font> <font color="#9a7200">'</font><font color="#9a7599">evil-next-visual-line</font><font color="#9a7200">)</font>  
  <font color="#9a7200">(</font>define-key evil-visual-state-map <font color="#009799">"k"</font> <font color="#9a7200">'</font><font color="#9a7599">evil-previous-visual-line</font><font color="#9a7200">)</font>  
  <font color="#719872">;; clojure mode config</font>  
  <font color="#9a7200">(</font><font color="#719899">**require**</font> <font color="#9a7200">'</font><font color="#9a7599">clojure-mode-extra-font-locking</font><font color="#9a7200">)</font>  
  <font color="#9a7200">(</font>add-hook <font color="#9a7200">'</font><font color="#9a7599">clojure-mode-hook</font> <font color="#9a7200">**\#'smartparens-strict-mode**</font><font color="#9a7200">)</font>  
  <font color="#9a7200">(</font>add-hook <font color="#9a7200">'</font><font color="#9a7599">clojure-mode-hook</font> <font color="#9a7200">**\#'evil-smartparens-mode**</font><font color="#9a7200">)</font>  
  <font color="#9a7200">(</font>add-hook <font color="#9a7200">'</font><font color="#9a7599">clojure-mode-hook</font> <font color="#9a7200">**\#'rainbow-delimiters-mode**</font><font color="#9a7200">)</font>  
  <font color="#719872">;; start a light theme when launched as GUI</font>  
  <font color="#9a7200">(</font><font color="#719899">**when**</font> <font color="#9a7200">(</font>display-graphic-p<font color="#9a7200">)</font>  
      <font color="#9a7200">(</font><font color="#719899">**progn**</font>  
        <font color="#9a7200">(</font>disable-theme <font color="#9a7200">'</font><font color="#9a7599">darkburn</font><font color="#9a7200">)</font>  
        <font color="#9a7200">(</font>load-theme <font color="#9a7200">'</font><font color="#9a7599">leuven</font> <font color="#719899">**t**</font><font color="#9a7200">)</font>  
        <font color="#9a7200">(</font>enable-theme <font color="#9a7200">'</font><font color="#9a7599">leuven</font><font color="#9a7200">)))</font>  
  <font color="#719872">;; remove background color for both server and client</font>  
  <font color="#9a7200">(</font>add-hook <font color="#9a7200">'</font><font color="#9a7599">window-setup-hook</font> <font color="#9a7200">'</font><font color="#9a7599">remove-background-color</font><font color="#9a7200">)</font>  
  <font color="#9a7200">(</font>add-hook <font color="#9a7200">'</font><font color="#9a7599">server-visit-hook</font> <font color="#9a7200">'</font><font color="#9a7599">remove-background-color</font><font color="#9a7200">)</font>  
  <font color="#719872">;; remove trailing whitespace when saving</font>  
  <font color="#9a7200">(</font>add-hook <font color="#9a7200">'</font><font color="#9a7599">before-save-hook</font> <font color="#9a7200">'</font><font color="#9a7599">delete-trailing-whitespace</font><font color="#9a7200">)</font>  
  <font color="#719872">;; toggle comments</font>  
  <font color="#9a7200">(</font>define-key evil-normal-state-map <font color="#009799">",c "</font> <font color="#009799">" cl"</font><font color="#9a7200">)</font>  
  <font color="#719872">;; match paredit.vim key-binding</font>  
  <font color="#9a7200">(</font>define-key evil-normal-state-map <font color="#009799">",W"</font> <font color="#009799">" kw"</font><font color="#9a7200">)</font>  <font color="#719872">; wrap with ()</font>  
  <font color="#9a7200">(</font>define-key evil-normal-state-map <font color="#009799">",w\["</font>        <font color="#719872">; wrap with \[\]</font>  
    <font color="#9a7200">(</font><font color="#719899">**lambda**</font> <font color="#9a7200">(</font><font color="#9a7200">**&optional**</font> arg<font color="#9a7200">)</font> <font color="#9a7200">(</font>interactive <font color="#009799">"P"</font><font color="#9a7200">)</font> <font color="#9a7200">(</font>sp-wrap-with-pair <font color="#009799">"\["</font><font color="#9a7200">)))</font>  
  <font color="#9a7200">(</font>define-key evil-normal-state-map <font color="#009799">",w{"</font>        <font color="#719872">; wrap with {}</font>  
    <font color="#9a7200">(</font><font color="#719899">**lambda**</font> <font color="#9a7200">(</font><font color="#9a7200">**&optional**</font> arg<font color="#9a7200">)</font> <font color="#9a7200">(</font>interactive <font color="#009799">"P"</font><font color="#9a7200">)</font> <font color="#9a7200">(</font>sp-wrap-with-pair <font color="#009799">"{"</font><font color="#9a7200">)))</font>  
  <font color="#9a7200">(</font>define-key evil-normal-state-map <font color="#009799">",S"</font> <font color="#009799">" kW"</font><font color="#9a7200">)</font>  <font color="#719872">; splice, i.e unwrap an sexp</font>  
  <font color="#9a7200">(</font>define-key evil-normal-state-map <font color="#009799">",J"</font> <font color="#009799">" kJ"</font><font color="#9a7200">)</font>  <font color="#719872">; join two sexps</font>  
  <font color="#9a7200">(</font>define-key evil-normal-state-map <font color="#009799">",O"</font> <font color="#9a7200">'</font><font color="#9a7599">sp-split-sexp</font><font color="#9a7200">)</font> <font color="#719872">; split an sexp</font>  
  <font color="#9a7200">(</font>define-key evil-normal-state-map <font color="#009799">",I"</font> <font color="#009799">" kr"</font><font color="#9a7200">)</font>  <font color="#719872">; raise current symbol</font>  
  <font color="#9a7200">(</font>define-key evil-normal-state-map <font color="#9a7200">(</font>kbd <font color="#009799">", &lt;up&gt;"</font><font color="#9a7200">)</font> <font color="#009799">" kE"</font><font color="#9a7200">)</font> <font color="#719872">; splice kill backward</font>  
  <font color="#9a7200">(</font>define-key evil-normal-state-map <font color="#9a7200">(</font>kbd <font color="#009799">", &lt;down&gt;"</font><font color="#9a7200">)</font> <font color="#009799">" ke"</font><font color="#9a7200">)</font> <font color="#719872">; forward</font>  
  <font color="#719872">;; These are different from vim, here cursor should NOT be on delimits</font>  
  <font color="#9a7200">(</font>define-key evil-normal-state-map <font color="#009799">",&gt;"</font> <font color="#009799">" ks"</font><font color="#9a7200">)</font>  <font color="#719872">; forward slurp</font>  
  <font color="#9a7200">(</font>define-key evil-normal-state-map <font color="#009799">",&lt;"</font> <font color="#009799">" kS"</font><font color="#9a7200">)</font>  <font color="#719872">; backward slurp</font>  
<font color="#9a7200">)</font></font>

 

As can be seen, all these functionality of Vim have already been coded up by someone and included in spacemacs as functions, all I did was changing their key-bindings. That was easy :-). I am looking forward to the journey ahead with spacemacs.

-   <span id="footnote1_e69wwp8"><a href="#footnoteref1_e69wwp8" class="footnote-label">1.</a> Poller, M.F., Garter, S.K. A Comparative Study of Moded and Modeless Text Editing by Experienced Editor Users. In Proceedings of CHI '83, pp 166-170</span>
