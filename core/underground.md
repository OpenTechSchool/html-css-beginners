---

layout: ots
title: Social Coding in the Underground

---

Welcome to the Underground! We are a secret organisation 
planning world domination. This involves a lot of planning, which 
means we need to know all the best cafes, bars and restaurants 
around the globe. After all, nobody wants to take over the world 
on an empty stomach.

The Underground is organised like this:

* The Grand Oligarchy: The OTS organisers. Supreme Leaders of the 
  Underground. The Grand Oligarchs have full control of the 
  organisational effort.
* The Coaches. Learned they are in the ways of Social Coding. They
  encourage the efforts of the students, and can communicate directly
  with the Oligarchy.
* The Students. New initiates to the Underground. Yet to fully immerse 
  themselves in the wonders of social coding, beholden to their coaches.

# Crisis!

The Underground is in crisis! The most honourable Grand Oligarchs 
have declared that we do not have enough cafes, bars or restaurants in 
our repository. Our planning efforts depend heavily on having enough 
food, caffeine and alcohol. Without places to hang out the 
organisation will wither away, as students, coaches and even the 
Oligarchy themselves spend more and more of their time at home, 
browsing cat pictures on the Internet.

Your mission is to add to our database of bars, restaurants and 
cafes. The goal is to get your changes into the master repository 
[OpenTechSchool/underground](https://github.com/OpenTechSchool/underground). 
However, the Oligarchs do not accept changes from just anybody. 
The Oligarchs will only accept pull requests from one of 
their trusted lieutenants, the Coaches.

# Find your coach

To contribute some code, first you'll need to find a coach. There are
a few ways to do this:

* Sequester one in a non-violent, friendly way, and ask nicely.
* Check the "Forks" on the `OpenTechSchool/underground` 
  repository. There will be coaches on there.
* Kindly ask one of your friendly co-students for some assistance.

Your coach will have an `underground` repository of their very
own. This is the one you'll need to contribute to. Then the coach will
forward your changes, and the changes of others, to the Oligarchs' 
repository.

# Fork this!

There are two methods to contributing on GitHub. The first and most
direct is for the owner to grant `push` access to you. This allows you
to `clone` their repository directly and push changes without requiring
their approval. Very convenient, but also a security nightmare and a
real hassle to add and remove people from the list.

What sets GitHub apart is their second method of contribution:
forking. When you _fork_ someone's repository, you get a complete copy
of their repository under your name. Then you are free to make any
changes you want, it's _your code_ (well, except for the
copyright). Your Git repository is exactly the same as theirs. The
only difference in GitHub is that your repository will be shown as
"forked from" theirs, so people know what the "real" repository is
(but we all know that yours is so much better).

So what you are going to do is _fork_ the repository of _your 
coach_. *DO NOT FORK THE OPENTECHSCHOOL REPOSITORY DIRECTLY!* 
You can click the Fork button on the GitHub page for your coach.

# Adding content in Markdown format

To add a new bar, club or restaurant we use a file format called
Markdown (extension .md). Think of it as a simpler version of
HTML. It allows you to write rich text in a simple text file and have
it be readable in both a text editor and a web browser. In GitHub you
can use Markdown in pull requests, comments, issues, wiki pages, gists
and almost everywhere you write text. In fact, even this course
material is written in Markdown, and hosted directly from the course
GitHub repository. It's simplicity and ubiquity make it well worth
learning.

In HTML, you might write something like this:

{% highlight html %}<h1>This is a large heading</h1> 
<p>This is a paragraph with <em>emphasis</em> and <strong>strong</strong> text.</p>
{% endhighlight %}

In Markdown this is much simpler:

    # This is a large heading

    This is a paragraph with _emphasis_ and *strong* text.

The main caveat is that you need to put a blank line between
paragraphs. Otherwise it will just lump all your text together.

# Think Globally, Commit Locally

Because the Underground is a global organisation, there are
directories in its repository for each city it is active in. Add your
contributions locally under your city's directory!

# Commit and Push

After you've made your contributions locally, it's time to get them to
the coach. We'll do this by (1) pushing to _your_ repository on GitHub,
then (2) submit a _pull request_ to your coach, (3) kindly asking them to
accept your changes into _their_ GitHub repository. Your coach will
eventually do the same thing, submitting a _pull request_ to the Oligarchy.

Use the same method as before to `add` and `commit` to your local
repository, then `push` to your repository on GitHub. Now you should
be able to see your changes on your repositories GitHub page.

# Pull request!

Time to create a pull request! Open your browser and navigate to
_your_ `underground` repository. There you can see the "Pull
Request" button up the top. Click it, and GitHub will start the Pull
Request process:

![Pull request button](images/pull-request.png)

A pull request is a GitHub way of saying "I made some changes and I
think you should add them to your repository". It allows developers to
share changes entirely within the website. If the developer on the
other end accepts your pull request then GitHub will copy your changes
over to their repository and merge them automatically.

If you see "Oops! master  is already up-to-date.." then it probably
means that you still need to `push` your local changes to GitHub.

Otherwise, make sure your coach is on the left and your repository is
on the right. Then fill out a friendly comment and click `Send pull
request`.

Now your coach will shortly receive a pull request notification.

## Shenanigans

It's best practice to add funny pictures as comments to a pull
request. And by best practice, we mean not really best practice. But
it is fun, and it shows how to use Markdown in comments.

Add a comment to your pull request using Markdown. The format for
adding an image is:

    ![image alt text](http://example.com/url-to-funny-pic.jpg)

The "image alt text" is the text that is displayed when the image
fails to load, or if the person is using a screen reader (yes, there
are blind programmers!). So maybe try to come up with a long-winded
in-depth analysis of what is happening in the image. For example: 

	![A cat, wearing a business suit, is sitting a table with a newspaper in hand. Looking up, the cat ponders: "I should buy GitHub".](http://i.qkme.me/3rgytr.jpg)

becomes:

![A cat, wearing a business suit, is sitting a table with a newspaper in hand. Looking up, the cat ponders: "I should buy GitHub".](http://i.qkme.me/3rgytr.jpg)

Sure, it's highly unlikely that anybody will ever read your
alt-text. But one day, maybe, someone will have a chuckle
at it.

# Upstream changes

Congratulations on making it this far! You're almost there!

There is one more thing left to do: keeping up to date with
upstream. In Git _upstream_ refers to some remote repository that you
consider higher or more authoritative than yours. At the moment your
local repository has one upstream repository, your GitHub
repository. When you type `git pull`, that's where it pulls from.

In this case you might consider your coach as also being upstream, or
even the oligarchs (aka OTS Organisers) at the top. If they push any
changes to their repository, then you'll want to be able to pull those
changes into your repository. For all you know, your coach might have
completely overwritten all your changes and added a curse for your
pets in the README file. Let's add another upstream to see what is
happening:

{% highlight sh %}
$ git remote add upstream https://github.com/OpenTechSchool/underground
{% endhighlight %}

This adds an upstream repository called `upstream`. Now we can
`fetch` directly from the Oligarchs. This will download the
`OpenTechSchool/underground` repository and store it under
the name `upstream`, so it won't interfere with your changes:

{% highlight sh %}
$ git fetch upstream
{% endhighlight %}

If you want to bring the changes into your work, use `merge`:

{% highlight sh %}
$ git merge upstream/master
{% endhighlight %}

You might want to have a look at the changes it brought, by typing :

{% highlight sh %}
$ git log
{% endhighlight %}

This lists all the commits from the most recent one. 
`git log` has lots of options, but you might find it more entertaining
not learning them and use the ugly but very informative:

{% highlight sh %}
$ gitk
{% endhighlight %}

Now bear in mind, your GitHub repository doesn't know about these
changes yet, so you'll need to `push` to get it up-to-date:

{% highlight sh %}
$ git push
{% endhighlight %}

And that's it! You're done!
