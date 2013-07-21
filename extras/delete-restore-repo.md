---
layout: ots
title: Delete and restore your local repository
---

## Preparation

This exercise is similar to the [delete-restore scenario](delete-restore.html) but not quite the same. This time you will give evidence that you trust GitHub. You will be deleting not only all content in your local working directory but also the repository itself. Therefore, it is important that you check for two things. First, you should have committed all work to your local repository. `git status` will tell you about untracked files or uncommitted changes. Second, you should have pushed all commits to the remote repository (GitHub in this case).

### Check the status of the local and the remote repository

A good way to check the status both of the local and the remote repository is to review the last commit in the history. In order to guarantee that you know about all changes that might have happened in the remote repository run `git fetch` before reviewing the commit history. The command will retrieve the current state from the remote repository without affecting any local changes. After having done so you can output the message of the last commit as follows.

{% highlight sh %}
$ git log -1
commit ca79e1c5fc081552a96a176275730b5f8cfd3363
Author: Tobias Preuss <tobias@opentechschool.org>
Date:   Sat Oct 20 15:06:07 2012 +0200

    Added delete-restore scenario.
{% endhighlight %}

The parameter `-1` limits the output to the last commit. The remote repository aliased as `origin` can be inspected as follows.

{% highlight sh %}
$ git log -1 origin
commit d5630aec495d6a176275730b5f8cfd3114cb52a9
Author: Steven Farlie <steven.farlie@gmail.com>
Date:   Sat Oct 20 14:50:27 2012 +0200

    Added chapter on Berlin.
{% endhighlight %}

If the commits deviate from each other as in the above examples you should definitely `push` your local commits to the remote repository before continuing.

## Delete all content and the repository

When you verfied that everything is synchronized and no files are left untracked or have changes you should hazard to delete the repository. We will simply remove the entire folder which contains the `.git/` folder and everything else.

{% highlight sh %}
$ cd ~
$ rm -rf myfirstrepo
{% endhighlight %}

![Relaxed looking cat stating: When I panic I make this face](../images/panic_cat.jpg)

## Restore the repository

I imagine you are a bit nervous after having deleted all work. Don't worry, there is an easy way to restore everything what you've done before. In order to do so you need to find out about the address of the remote repository. GitHub shows the address right at the top of the repository listing. You can choose between `HTTP`, `SSH` and `Git Read-only`. The favored transfer method is `SSH`. Copy the address and then run the following command in your home directory.

{% highlight sh %}
$ cd
$ git clone git@github.com:johndoe/myfirstrepo.git .
{% endhighlight %}

This command will create a directory named `myfirstrepo`, copy the `.git/` folder and checkout all files for you. It will further link the remote repository to your local copy.

Please check the contents of the newly created folder.

{% highlight sh %}
$ ls -1a myfirstrepo
{% endhighlight %}

All files and folders should be back.

## Lessons learned

The interesting aspect learned from this exercise is that the remote repository is an exact copy of the local one. That means whenever you clone your repository to some other location and push the latest changes you are safe to loose your local copy. Sounds weird? No longer, I guess. You also learned how to inspect the remote repository using `git fetch` and `git log`.

