---

layout: ots
title: Setup

---

# Create a GitHub account

The first and easiest thing to do is setup a GitHub account. Most people use the
GitHub Free account, which gives you unlimited public repositories. You can sign
up [ here ]( https://github.com/signup/free ).

Note that GitHub is designed around sharing with the whole world. With a free
account, everything you upload will be publicly available. This includes the
email address that you use when you configure Git.

# Download and install Git

We'll be using the plain command-line Git. The easiest way to install Git on Mac
or Windows is to use the prepackaged GitHub for Mac and GitHub for Windows. Not
only do they provide the Git command line, but they also include a GUI interface
to streamline some interactions with GitHub.

* [ GitHub for Mac ]( http://mac.github.com/ )
* [ GitHub for Windows ]( http://windows.github.com/ )

## Linux installation

On Linux, most distributions have a git package. Try to get `git`, `gitk` and `git-gui`
packages installed. Once you have it installed you will need to generate a SSH key
and associate it with GitHub. Run `ssh-keygen -t rsa` to generate a key. Then copy
`~/.ssh/id_rsa.pub` to the [ SSH Settings page ]( https://github.com/settings/ssh ) on GitHub. Please refer to the help page entitled [ Generating SSH Keys ]( https://help.github.com/articles/generating-ssh-keys#platform-all) if you run into problems on any of the operating systems.

You should set your name and email address as well. These will be added to any commits
you make:

	$ git config user.name "Your Name"
	$ git config user.email "youremailaddress@example.com"

Things get a little prettier if you turn on colors:

	$ git config color.ui auto
