---
Status: published
Title: An Mac Look for my KDE Desktop
Date: 2007-12-05 10:04
Author: Huahai
Category: notebook
Tags: Linux
Slug: an-mac-look-for-my-kde-desktop
Alias: /blog/2007/12/mac-look-my-kde-desktop
Lang: en
---

Although I have never laid my hands on an Apple computer, I have seen people going crazy about them. I remember seeing some kids shouting hysterically in front of Apple store on the release day of Tiger a few years ago. The user interface of Apple's OS is said to be one of the selling points. So when I was feeling tired of Mepis Linux's default look last night, I decided to try an OS X look for a change. It turned out to be relatively easy to do.

<img src="https://farm3.static.flickr.com/2063/2088772436_89e4266cbc_z.jpg" id="__mce_tmp" />

**KDE widget** Basically, getting an OS X Tiger look and feel on KDE involves installing a theme that imitates its look and feel. There is a KDE theme called [Baghira](https://baghira.sourceforge.net/)that does just that. It's so popular that Debian sid has it in the pool, so

`apt-get install kwin-baghira`

as root should get it installed. Once it's installed, launch *KDE Control Center -&gt; Appearance and Themes -&gt; Style*, and change *Widget Style* to Baghira. Also, go one step up to *Colors*, and change *Color Scheme* to *Aqua Blue*. Now you should get Tiger look and feel for all the KDE widgets. This theme can be further configured using a tool called *bab*. One can launch bab from from command line and find it in the system tray. Right click it to open configuration screen.

**Compiz window decoration** Since I use compiz-fusion as my default window manager, Baghira theme's own kwin decoration settings does not work. Of course, compiz-fusion can use kwin as window decorator, but it's less stable than *emerald*, compiz's own window decorator. It would be great if emerald has an OS X looking theme. Sure enough, there are quite a few emerald themes that can do that. Launch *emerald-theme-manager* tool, one can download GPL or non GPL'ed themes. I tried them one by one, and found at least three OS X imitators. In the end I chose "dreamtiger-baghira" as it matches Baghira theme.

**OS X style menubar** One can set up an OS X style menubar on top of screen in KDE Control Center -&gt; Desktop -&gt; Behavior. I did that, but the old KDE panel was still around and it was not possible to remove it. So I removed all of the panel's content, and set it to auto hide at a corner so it won't bother me any more. Following [Baghira theme's instruction](https://baghira.sourceforge.net/OS_Clone-en.php), I added Baghira's Starter to the menubar. Now the menu of KDE application with current mouse focus will show up in the menubar. This behavior took some used to, but I think I am liking it because it makes application windows look cleaner and takes less screen space. There are some caveats using OS X style menubar in KDE. Icons in system tray does not scale, so their bottoms are cropped off. This is not a big deal since I hide most of the system tray icons. Another issue, is that full screen mode in VirtualBox is no longer really full screen because the menubar is always visible. This is a bit annoying especially if you want to do a presentation or playing full screen games in the virtual machine. I have yet to find a way to hide the menubar. Also, I have been using a Mac like docker, [kxdocker](https://www.xiaprojects.com/index.php?section=All&project=KXDocker), for years, so there's no need to change here.

**GTK application** Baghira theme does not apply to GTK applications, which I have plenty: firefox, synaptic, openoffice, gvim, etc. To have a consistent look across all applications, I needed to set up OS X like theme for GTK application too. Again, there are several GTK themes can do that. I chose to download [OSX-Tiger](https://www.gnome-look.org/content/show.php/OSX-Tiger+theme?content=56577) theme because it's small. I unpacked it and moved the unpacked directory to */usr/share/themes*. Since a full installation of gnome desktop wasn't something I wanted to do, I needed a small tool to let GTK applications aware of and use this theme. A command line tool called *switch2* can be installed from Debian pool (package name is *gtk-theme-switch*) to do that:

`switch2 /usr/share/themes/OSX-theme`

**Icons** It doesn't help if one uses an OS X theme without OS X like icons. I chose to install [OS-L](https://www.kde-look.org/content/show.php?content=16564) icon set. It includes a script to build the icon set, one can then pick it in KDE Control Center -&gt; Appearance & themes -&gt; Icons.

**Fonts** To do a full blown imitation of OS X look, matching fonts are required. Unfortunately, we have to use the real thing here. Download [Mac fonts](https://www.osx-e.com/downloads/misc/macfonts.html), unpack and put the directory under */usr/share/fonts/truetype*. To easily achieve font consistence across all GUI applications, I changed */etc/fonts/local.conf* to make these Mac fonts as X server's preferred fonts. My */etc/fonts/local.conf*is here:

<span style="font-family: monospace;"> <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*fontconfig*</span><span style="color: #06287e;">*&gt;*</span>  
  <span style="color: #a0b0c0;">*&lt;!*</span><span style="color: #a0b0c0;">*-- Disable anti-alias for Chinese fonts less or equal to 12px --*</span><span style="color: #a0b0c0;">*&gt;*</span>  
  <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*match*</span><span style="color: #06287e;">* *</span><span style="color: #e5a00d;">*target*</span>=<span style="color: #4070a0;">"font"</span><span style="color: #06287e;">*&gt;*</span>  
    <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*test*</span><span style="color: #06287e;">* *</span><span style="color: #e5a00d;">*qual*</span>=<span style="color: #4070a0;">"any"</span><span style="color: #06287e;">* *</span><span style="color: #e5a00d;">*name*</span>=<span style="color: #4070a0;">"family"</span><span style="color: #06287e;">* *</span><span style="color: #e5a00d;">*compare*</span>=<span style="color: #4070a0;">"eq"</span><span style="color: #06287e;">*&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*string*</span><span style="color: #06287e;">*&gt;*</span>WenQuanYi Bitmap Song<span style="color: #5b3674;">*&lt;/string&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*string*</span><span style="color: #06287e;">*&gt;*</span>AR PL Mingti2L Big5<span style="color: #5b3674;">*&lt;/string&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*string*</span><span style="color: #06287e;">*&gt;*</span>AR PL KaitiM Big5<span style="color: #5b3674;">*&lt;/string&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*string*</span><span style="color: #06287e;">*&gt;*</span>AR PL KaitiM GB<span style="color: #5b3674;">*&lt;/string&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*string*</span><span style="color: #06287e;">*&gt;*</span>AR PL SungtiL Big5<span style="color: #5b3674;">*&lt;/string&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*string*</span><span style="color: #06287e;">*&gt;*</span>AR PL New Sung<span style="color: #5b3674;">*&lt;/string&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*string*</span><span style="color: #06287e;">*&gt;*</span>AR PL ShanHeiSun Uni<span style="color: #5b3674;">*&lt;/string&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*string*</span><span style="color: #06287e;">*&gt;*</span>AR PL ZenKai Uni<span style="color: #5b3674;">*&lt;/string&gt;*</span>  
    <span style="color: #5b3674;">*&lt;/test&gt;*</span>  
    <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*test*</span><span style="color: #06287e;">* *</span><span style="color: #e5a00d;">*name*</span>=<span style="color: #4070a0;">"pixelsize"</span><span style="color: #06287e;">* *</span><span style="color: #e5a00d;">*compare*</span>=<span style="color: #4070a0;">"less\_eq"</span><span style="color: #06287e;">*&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*double*</span><span style="color: #06287e;">*&gt;*</span>12<span style="color: #5b3674;">*&lt;/double&gt;*</span>  
    <span style="color: #5b3674;">*&lt;/test&gt;*</span>  
    <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*edit*</span><span style="color: #06287e;">* *</span><span style="color: #e5a00d;">*name*</span>=<span style="color: #4070a0;">"antialias"</span><span style="color: #06287e;">*&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*bool*</span><span style="color: #06287e;">*&gt;*</span>false<span style="color: #5b3674;">*&lt;/bool&gt;*</span>  
    <span style="color: #5b3674;">*&lt;/edit&gt;*</span>  
    <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*edit*</span><span style="color: #06287e;">* *</span><span style="color: #e5a00d;">*name*</span>=<span style="color: #4070a0;">"hinting"</span><span style="color: #06287e;">*&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*bool*</span><span style="color: #06287e;">*&gt;*</span>true<span style="color: #5b3674;">*&lt;/bool&gt;*</span>  
    <span style="color: #5b3674;">*&lt;/edit&gt;*</span>  
  <span style="color: #5b3674;">*&lt;/match&gt;*</span>  
  <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*alias*</span><span style="color: #06287e;">*&gt;*</span>  
    <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>serif<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
    <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*prefer*</span><span style="color: #06287e;">*&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>AppleGaramond<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>DejaVu Serif<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>Bitstream Vera Serif<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>Times New Roman<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>Times<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>AR PL New Sung<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>AR PL ShanHeiSun Uni<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>AR PL Mingti2L Big5<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>AR PL SungtiL GB<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>SimSun<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
    <span style="color: #5b3674;">*&lt;/prefer&gt;*</span>  
  <span style="color: #5b3674;">*&lt;/alias&gt;*</span>  
  <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*alias*</span><span style="color: #06287e;">*&gt;*</span>  
    <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>sans-serif<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
    <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*prefer*</span><span style="color: #06287e;">*&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>Lucida Grande<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>DejaVu Sans<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>Bitstream Vera Sans<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>Arial<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>Verdana<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>Helvetica<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>AR PL New Sung<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>AR PL ShanHeiSun Uni<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>AR PL kaitiM Big5<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
      <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>AR PL kaitiM GB<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
    <span style="color: #5b3674;">*&lt;/prefer&gt;*</span>  
   <span style="color: #5b3674;">*&lt;/alias&gt;*</span>  
   <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*alias*</span><span style="color: #06287e;">*&gt;*</span>  
     <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>monospace<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
     <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*prefer*</span><span style="color: #06287e;">*&gt;*</span>  
       <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>DejaVu Sans Mono<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
       <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>Bitstream Vera Sans Mono<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
       <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>Courier New<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
       <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>Courier<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
       <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>AR PL New Sung<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
       <span style="color: #06287e;">*&lt;*</span><span style="color: #06287e;">*family*</span><span style="color: #06287e;">*&gt;*</span>AR PL ShanHeiSun Uni<span style="color: #5b3674;">*&lt;/family&gt;*</span>  
     <span style="color: #5b3674;">*&lt;/prefer&gt;*</span>  
  <span style="color: #5b3674;">*&lt;/alias&gt;*</span>  
<span style="color: #5b3674;">*&lt;/fontconfig&gt;*</span>  
</span>

Here, I chose "AppleGaramond" as the default serif font, "Lucida Grande" as the default san-serif font. I kept my original monospace font intact since I like it. For menu and toolbar fonts, I changed them to "Lucida MAC" in KDE Control Center -&gt; Appearance & Themes -&gt; Fonts. They make menus look very clear to read.

**Firefox** Firefox doesn't respect KDE's font size setting so its UI font often looks much bigger than other applications. We have to manually set its UI fonts to have consistency. Create a file *~/.mozilla/firefox/xyzxyz.default/chrome/userChrome.css* (or just copy the example from the same directory, replace "xyzxyz" with the actual directory name), and change the font size. Finally, get a Mac-looking compatible firefox theme should make firefox looks better. There are many options, I chose [macfox II](https://addons.mozilla.org/en-US/firefox/addon/3174) for its clean look.

**Update: 12/06/2007 09:42:07 AM (EST)** It turned out I don't like "AppleGaramond", it's too much newspaper like. I eventually rolled back to "DejaVu Serif" as my default serif font (mostly used in Web content viewing). Also, Baghira theme crashes [basket note pads](https://basket.kde.org/) application. I sent a bug report to basket developer, haven't heard back yet.
