Title: Compiz-Fusion on KDE:
Date: 2007-10-29 00:39
Author: Huahai
Category: notebook
Tags: Linux, Xorg
Slug: compiz-fusion-on-kde
Alias: /blog/2007/10/compiz-fusion-kde
Lang: en

**Introduction**  
Nowadays, it is not uncommon to see people multi-tasking with a dozen of windows open. With an 12 inch small screen, Thinkpad X61 really needs an efficient window manager for me to get serious work done. I have been struggling to find a good choice. Of course, 3D desktop seemed to be a reasonable candidate. However, I was quite hesitated to jump on the 3d desktop bandwagon before. One of the reasons is that I did some scientific research work on 3D virtual environment as a PhD student several years ago, and I knew the technology was quite limited in term of mimicking human interaction with the real world. And the benefit of 3D vs 2D wasn't really well established, even in theory. But now almost every vendor is having a 3D desktop project going on right now, I think I should probably give them a try.

Being a Linux user (I use Debian + KDE), I look for open source solution. The hottest project on open source 3d desktop seems to be compiz and its friends beryl. There are plenty of [demo videos of them on youtube](http://youtube.com/results?search_query=compiz-fusion&search=Search). These two projects recently merged back, and the new project is called [Compiz-Fusion](http://www.compiz-fusion.org/). They just released their latest version compiz-fusion 0.60 on Oct. 20, 2007. So I headed towards their download page, and fetched all the tar balls. It's strange that they did not package the whole thing into a simple tar ball. Anyway, it's not a big deal. But you have to follow certain order to compile and install the pieces. It took me a while to find [the page about this specific order](http://wiki.compiz-fusion.org/Installation). Also, you need to install a bunch of packages to satisfy all the dependencies. For an experienced Linux user, this is not a problem. It is not so with anybody else though. Of course, most of the Linux distributions package some earlier versions of compiz or beryl, but the volatile nature of 3d desktop development makes those packages unattractive, since they are not supported as upstream developers have moved on to newer, but completely different versions.

**Installation**

Once the compiz-fusion 0.60 is compiled and installed, you should hold in check your urge to use it immediately. First, you need to configure your X server. This aspect is pretty [well documented](http://wiki.compiz-fusion.org/Hardware/Intel) for my Intel 965GM graphic chip on X61. It involves just a few edits in */usr/X11/xorg.conf*. Once X server is setup and reloaded, you can give compiz-fusion a spin by issuing *compiz --replace* shell command. Unfortunately, this is usually when the frustration begins. If you are lucky and compiz's working, it brings about some seemly disastrous results: all windows title bars disappear so you cannot move them, programs crash, etc. If you are not lucky, nothing happens, or you get some obscure error messages. My experience progressed from being unlucky to lucky, and eventually, to success.

In the unlucky stage, I got this seemly popular error message:

/usr/bin/compiz (core) - Error: Another window manager is already running on screen: 0  
/usr/bin/compiz (core) - Fatal: No manageable screens found on display :0

However, the reason is hard to find. After a really lengthy search on the Web, I finally found the problem: I previously disabled desktop icon in KDE. If it is the case, the default windows manager in KDE, called kwin, will refuse to relieve the control (I found it on a ubuntu forum, can't remember exactly where). So I re-enabled desktop icon in KDE control center. Now I got a similar, yet also popular error message:

>compiz (core) - Fatal: GLX\_EXT\_texture\_from\_pixmap is missing  
>compiz (core) - Error: Failed to manage screen: 0  
>compiz (core) - Fatal: No manageable screens found on display :0.0

This one is easier to solve. For Intel based graphic chip, direct rendering with pixmap does not work. So according to the Compiz wiki, I need to specify indirect rendering with an environment variable, use *LIBGL\_ALWAYS\_INDIRECT=1 compiz --replace* to start compiz.

Once compiz-fusion is started correctly, it is a great window manager. You can do all the wobbly windows, cube desktop, shifting windows and other dizzily effects you've seen on videos. It 's fast on this slim laptop with only an Intel integrated graphic chip. Compiz-Fusion has a plugin architecture that allows third parties to develop new effects and widgets. Open compiz-fusion configuration manager *ccsm*, you will find many such plugins. New plugins are developed daily. What I find most useful are those window managing plugins. For example, with Scale plugin enabled (it's default), when you move mouse over to top right corner (all actions are configurable), all the windows on the desktop slide and scale to make a nice bird-eye view, very convenient for switching between windows. And the often-seen cube desktop is useful too. And they are several others.

**Setup Compiz-Fusion as Default Window Manager in KDE**

Since I like compiz-fusion so far. I would like to keep it as my default window manager for now. The best way of doing that is to create a separate Compiz-Fusion session, so if things go bad with Compiz-Fusion, you can still go back to regular KDE or Gnome session. To do that, we create a desktop file for Compiz-Fusion session, the desktop manager such as kdm or gdm (which I use, for its support of ThinkFinger) will pick it up and make a session menu entry in the greeting screen. My desktop file is */usr/share/xsessions/compiz-fusion.desktop*, and it contains:

` [Desktop Entry] Encoding=UTF-8 Name=Compiz-Fusion Exec=/usr/local/bin/start-compiz-fusion.sh Icon= Type=Application`

Here, */usr/local/bin/start-compiz-fusion.sh* tells KDE to use compiz-fusion as the default window manager. This way, the original KDE window manager, kwin, will not be loaded and then unloaded. This method will solve a lot of display problems people have reported online, such as system tray items getting pushed out of system tray, gobbled displays, disappearing window title bars, etc. This script contains:

` #!/bin/sh export KDEWM="/usr/bin/compiz-fusion" exec startkde`

Finally, */usr/bin/compiz-fusion* contains the actual call to compiz, so make it executable. In my case, it is:

` #!/bin/sh LIBGL_ALWAYS_INDIRECT=1 compiz --replace --sm-disable ccp`

**Workaround to Suspend Problem**

After setting up Compiz-Fusion as my default window manager. I set out to test its compatibility with my other system configurations. I indeed found one problem with putting my X61 to sleep using s2ram. The sleep went very well, maybe too well, the laptop immediately and automatically waked up! This was extremely annoying. Again, an obscure workaround was found. Basically, you need to open up *ccsm*, go to "General Options" -&gt; "Display Settings" tab, and uncheck "Sync to VBlank". Apparently, this video card setting allows some general purpose events (GPE event) to be generated, even after sleep, and the ACPI daemon picks them up, thus waking up the system. The root of this problem seems to be a Linux kernel issue. Disabling "Sync to VBlank" might have a slight distortion effect on the 3D desktop if you spin the cube too hard, however, I find that barely noticeable.

In summary, the latest 0.60 release of Compiz-Fusion seems to work very well with my brand new Thinkpad X61. And 3D desktop seems to be of some usefulness. Let me try it out for more days.
