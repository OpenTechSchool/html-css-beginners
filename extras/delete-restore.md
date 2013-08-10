---
layout: ots
title: Delete and restore all files
---

## Preparation

Git toutes that it keeps all our repository files tracked under its version control. 
Now it is time to prove that you trust Git - you will be deleting all 
files and folders in your working directory! A good starting point for 
this experience is to check whether you've committed all changes. The easiest 
way to see this is to run `git status` in the working directory. The 
output should look similar to the following.

{% highlight sh %}
$ cd ~/myfirstrepo
$ git status
# On branch master
nothing to commit (working directory clean)
{% endhighlight %}

If you have untracked or modified files you should definitely take care 
of those before continuing. Please refer to the 
[introduction section](core/first-repo.html) or ask one of the coaches 
if you need assistance on this subject.

## Delete all content in your working directory

There are several ways to delete files and folders. You could open a file 
explorer, select the files and folders and simply delete them. Another 
option is to use the command line. Since you already working in this 
environment you should also learn how to delete files and folders. Please 
mind: You will delete all files and folders **except** one `.git/` folder. 
That is important! The following command will also omit other hidden files. 
Be sure to navigate into the correct directory before running the remove 
command.

{% highlight sh %}
$ cd ~/myfirstrepo
$ rm -rf **/*
sure you want to delete all the files in ~/myfirstrepo/** [yn]? y
{% endhighlight %}

You can immediately check to see what happens by listing the contents of the directory.

{% highlight sh %}
$ ls -1a
.
..
.git
{% endhighlight %}

As you can see all that is left are the `.git/` folder and the `.gitignore` file. Congratulations! You successfully deleted all the work you have put into this project. :-)

![A frightened cat](../images/frightened_cat.png)

## Restoring the content of your project

So how can you get back all the files and folders which you created in hours of work? It is very easy and fast forward. One command will recover them. Please mind the `.` following after `git checkout` which points to the current directory.

{% highlight sh %}
$ git checkout .
{% endhighlight %}

Since there will be no output following to the command you need to check yourself whether your work has been restored successfully. A directory listing using `ls -1a` should satisfy you.

## Lessons learned

From this task you should have learned at least two things. First, as long as you take care of the `.git/` folder and commit your changes on a regular basis everything will be fine. Second, `git checkout` is quite useful to restore all content to the working directory which is kept in the repository.

If you want to go a step further go to another exercise: [Delete and restore your local repository](delete-restore-repo.html).

