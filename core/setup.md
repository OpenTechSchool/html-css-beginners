---

layout: ots
title: Setup

---

# Create a GitHub account

The first and easiest thing to do is setup a GitHub account. Most people use the
GitHub Free account, which gives you unlimited public repositories. You can sign
up [here]( https://github.com/signup/free ).

Note that GitHub is designed around sharing with the whole world. With a free
account, everything you upload will be publicly available. This includes the
email address that you use when you configure Git.

# Download and install Git

We'll be using the plain command-line Git. The easiest way to install Git on Mac
or Windows is to use the prepackaged GitHub for Mac and GitHub for Windows. Not
only do they provide the Git command line, but they also include a GUI interface
to streamline some interactions with GitHub.

* [GitHub for Mac]( http://mac.github.com/ )
* [GitHub for Windows]( http://windows.github.com/ )

The GitHub application makes it very easy to work with Git and Github's repositories. 
If you'd like a bit more control, you can install the official installers from git's 
homepage:

* [git-scm.com]( http://git-scm.com/ )

## Linux installation

On Linux, most distributions have a git package. Try to get `git`, `gitk` and `git-gui` 
packages installed. Once you have it installed you will need to generate a SSH key 
and associate it with GitHub. Run `ssh-keygen -t rsa` to generate a key. Then copy 
`~/.ssh/id_rsa.pub` to the [SSH Settings page]( https://github.com/settings/ssh ) 
on GitHub. Please refer to the help page entitled 
[Generating SSH Keys]( https://help.github.com/articles/generating-ssh-keys#platform-all) 
if you run into problems on any of the operating systems, and/or ask one of the coaches.

You should set your name and email address as well. These will be added to any commits
you make:

	$ git config --global user.name "Your Name"
	$ git config --global user.email "youremailaddress@example.com"

These configuration settings apply to all git work you will do in the future; 
You can also apply local settings, for just one project if you'd like. To 
find out more about git's config, you can type `git help config`, visit a 
good [help page](http://git-scm.com/book/en/Customizing-Git-Git-Configuration) 
on it, or ask one of the coaches!

You can make things a little prettier if you turn on colors:

	$ git config --global color.ui auto
