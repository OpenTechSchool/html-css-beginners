---
layout: default
title: Your first repository
---

# Your first repository

{% highlight sh %}
$ git init myfirstrepo
Initialized empty Git repository in /tmp/myfirstrepo/.git/
{% endhighlight %}

Git creates a directory called `myfirstrepo`, this is where you'll be keeping all
your code. Then git creates a subdirectory called `.git` which is where it keeps
all the settings and history for this repository. It starts with a dot, which means
that it is a hidden directory, to keep it out of the way of your files.

So at the moment, you have a completely blank repository that is ready to add
files. From now on, your command line will need to be inside `myfirstrepo` so
that git knows which repository to use. The `status` command in git will let you
know this current status of your repository:

{% highlight sh %}
$ cd myfirstrepo
$ git status
# On branch master
#
# Initial commit
#
nothing to commit (create/copy files and use "git add" to track)
{% endhighlight %}

## Add a file

We can put any type of file into Git. It is especially good at keeping track of
text files such as Python, Javascript, HTML and CSS. A very common file is the
README, which is used to tell people what the repository is about.

Create a new file called `README` inside `myfirstrepo/` with your text editor.
You can put any text inside here. Maybe you would like something a little
mysterious? We could put some Keats in here:

    Here will I kneel, for thou redeemed hast
    My life from too thin breathing: gone and past
    Are cloudy phantasms. Caverns lone, farewel!
    And air of visions, and the monstrous swell
    Of visionary seas! No, never more
    Shall airy voices cheat me to the shore
    Of tangled wonder, breathless and aghast.

Yes, this seems suitable.

Once you have the file saved then it's time to add it to your repository. In
git, you add and remove files with the `add` and `rm` commands.

{% highlight sh %}
$ git status
# On branch master
#
# Initial commit
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	README
nothing added to commit but untracked files present (use "git add" to track)
{% endhighlight %}

Here git is saying that the README file is not being tracked. Let's add it.

{% highlight sh %}
$ git add README
$ git status
# On branch master
#
# Initial commit
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#
#	new file:   README
#
{% endhighlight %}

Ok, it's in. Now we can create our first commit. A commit is a snapshot of the
repository at a particular point in time. Everything that we `add` counts
towards the next commit.

For now we just want the new README file in our commit. So let's commit it:

{% highlight sh %}
$ git commit -m "This is my first commit."
[master (root-commit) 199b7a1] This is my first commit.
 1 file changed, 7 insertions(+)
 create mode 100644 README
{% endhighlight %}

And `log` will tell us that the commit is now in the repository:

{% highlight sh %}
$ git log
commit 199b7a1457ebd5c1df3cb5fde21a45b769d9c31c
Author: Steven Farlie <steven.farlie@gmail.com>
Date:   Mon Oct 15 15:01:26 2012 +0200

    This is my first commit.
{% endhighlight %}


# Pushing to GitHub

