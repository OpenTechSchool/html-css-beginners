---
layout: ots
title: Setup
---

## Create a GitHub account

The first and easiest thing to do is setup a GitHub account. Most people use the
GitHub Free account, which gives you unlimited public repositories. You can sign
up [ here ]( https://github.com/signup/free ).

## Download and install Git

We'll be using the plain command-line Git, but there is also a packaged GitHub
program for OSX and Windows that contains command-line Git.

* [ GitHub for Mac ]( http://mac.github.com/ )
* [ GitHub for Windows ]( http://windows.github.com/ )

On Linux, most distributions have a git package. Try to get `git`, `gitk` and `git-gui`
packages installed. Once you have it installed you will need to generate a SSH key
and associate it with GitHub. Run `ssh-keygen -t rsa` to generate a key. Then copy
`~/.ssh/id_rsa.pub` to the [ SSH Settings page ]( https://github.com/settings/ssh ) on GitHub.

