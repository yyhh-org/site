Title: Complete OpenSSH Client Public Key Solution on Debian
Date: 2007-11-12 10:14
Author: Huahai
Category: notebook
Tags: Linux
Slug: complete-openssh-client-public-key-solution-on-debian
Alias: /blog/2007/11/complete-openssh-client-public-key-solution-debian
Lang: en

My work requires me to connect to many different SSH servers, and I have different passwords for each server. It's a pain in the neck trying to type in many different passwords everyday. The obvious solution is to use OpenSSH's public key login solution, so passwords are no longer needed to connect to SSH servers from a single client (e.g. my office desktop).

**Key Generation and Distribution**

To use public key authentication, it is necessary to generate a pair of keys on your client machine. Do the following as normal user:

` mkdir ~/.ssh chmod 700 ~/.ssh ssh-keygen -q -f ~/.ssh/id_rsa -t rsa`

You will be prompted for typing in passphrase for the private key. As a matter of security, use a different passphrase from your login password to this client machine. This process generates two files in *~/.ssh*: *id\_rsa* is your private key, and you should keep it as a secret at all cost! Use this command to make it unreadable for anyone but you:

`chmod go-rwx ~/.ssh/id-rsa`

*id\_rsa.pub* is your public key, and you need to distribute this key to whatever server you want to connect to.

Basically, you need to upload your *id\_rsa.pub* file to all your SSH servers. You can use your favorite FTP or SFTP software to do that, or use commands such as *scp*, *sftp*, or even *ftp* if the server still supports it. After *id\_rsa.pub* is uploaded to your server. You need to SSH to the server, and create a directory *~/.ssh* if it does not exist already, and then

`cat id_rsa.pub >> ~/.ssh/authorized_keys`

to append this public key to *authorized\_keys* file. Now you should be able to SSH to your server without typing in server password, only your private key passphrase is needed. Still, repeatedly type in the same passphrase can quickly become a burden in itself. The solution is to use *ssh-agent*.

**Setup ssh-agent**

*ssh-agent* is part of the OpenSSH client package. The concept is simple: you only needs to type in passphrase for your private key once, and *ssh-agent* will remember it and use it whenever you need to make SSH connections in a session. Simple, right? It's actually more than that. Due to the diverse configurations of different Linux systems, setting up *ssh-agent* to work with one's system is notoriously troublesome. Here, I offer my simple solution that works on Debian sid.

On Debian, *ssh-agent* is by default configured to be launched during X server starting process. In fact, *ssh-agent* is the program that starts your window manager! For example, *ssh-agent startkde* is how your X session is started if you use KDE. This way, all your GUI programs inherit *ssh-agent* environment, and you only need to type in passphrase once to make SSH connections from **GUI** applications. However, if you try to make SSH connection from a **Shell**, you do not have *ssh-agent* environment variables!

You may have read people suggesting to use [keychain](http://www.gentoo.org/proj/en/keychain/) to work with *ssh-agent*. However, *keychain* does not work on my Debian sid system. Instead of reusing existing *ssh-agent* process as it advertises, *keychain* launches its own *ssh-agent*, which ruins the whole business. The problem, is that the original *ssh-agent* launched by *Xsession* does not export environment variables SSH\_AGENT\_PID and SSH\_AUTH\_SOCK. So *keychain* does not know about the existing *ssh-agent* process. Of course, there's no way for the first *ssh-agent* to export environment variables because it's not even live in a shell.

Apparently, this problem can be solved by some complex solutions. Read [here](http://blog.plover.com/oops/ssh-agent.html) for an example (this solution does not work for me because on my system *lsof* cannot reliably find the socket used by *ssh-agent*). Fortunately, a much simpler solution is suggested by some comments there.

This simple solution utilizes *ssh-agent*'s address-binding option "-a". This option allows one to bind the socket used by *ssh-agent* to any path name. Now you don't have to search for the socket, you can just put the socket where you want it and you always know where it is. For example, I bind it to "/tmp/ssh-agent", then SSH\_AUTH\_SOCK should be exported as the value "/tmp/ssh-agent". It's that simple!  
Of course, we need to ask the original *ssh-agent* launched by *Xsession* to use this address-binding option. Edit file */etc/X11/Xsession.d/90x11-common\_ssh-agent* as root, change only one line:

` from: SSHAGENTARGS= to: SSHAGENTARGS="-a /tmp/ssh-agent"`

Hit Ctrl-alt-backspace to restart X server. Look at your */tmp* directory, there should be a file *ssh-agent* there.

Now we need to export the appropriate environment variables in shell. Edit file *~/.bashrc*, and add these two lines:

` export SSH_AUTH_SOCK=/tmp/ssh-agent export SSH_AGENT_PID=$(pgrep ssh-agent)`

When you start a terminal, *env* command should now have these two variables.  
After these simple edits, we still miss one thing. That is, *ssh-agent* is still empty, containing no identities. To add yourself to the agent, use *ssh-add* command. To be convenient, I just put it in my KDE startup script: *~/.kde/Autostart/start*. I also make sure to install a *ssh-askpass* package (there're a couple of choices), so I get a GUI prompt asking me to type in SSH passphrase once I enter KDE. After this one and only passphrase input, I can SSH as many times and as many places as I want without typing in a single password again. What a relief!
