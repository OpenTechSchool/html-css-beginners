---
layout: ots
title: push-to-heroku 
---
# Extra credit
    In this module we'll explore how to host your snazzy website on Heroku.
    Why Heroku? Simply because heroku works like magic with Git! And for us beginners,
    not having to pull your hair out to try and deploy your web app is a good thing.
    Oh, and Heroku is free for 'light' users, i.e. if you have very litle traffic.

# The Hosting Conundrun for Beginners

Learning to code is a fun, creative endeavour. At some point, you may want to share your creation with the world... and depending on the technology you used, this can become a real thorn in your side. There's enough to do without having to get pulled into the complexities of deploying your webapp on a publicly accessible server.

Enter hosting services like Heroku. Hosting providers really try and simplify your life so that you can focus on your app, and not all the piping and infrastructure necessary to make it run. The beauty of Heroku, as we will see, is that it makes deploying your application incredibly easy when you're a git afficionado. And you are one, right?

# Setup

What we're goign to do is create a Heroku account, and set-up Git so that it knows where to push your code when you want to send it to Heroku instead of your github account.

You can either follow along the Heroku [Gettign Started](https://devcenter.heroku.com/articles/quickstart) doc, or read on here to get a bit more context.

## Create a Heroku account
This is the easiest bit! head down to the [sign up](https://api.heroku.com/signup/devcenter) page and enter your email adress. You'll receive the usual confirmation email etc. Make a good note of the email and password you created, as it will be used to login from the console.

## Install Heroku client on your machine
Referred to as the 'Heroku Toolbelt', it has all the client side code-magic to enable you to use Heroku from your concole/terminal. Just pick the right OS from the [download page](https://toolbelt.heroku.com/) and install away. It will add the Heroku install directory to your path automatically.

## Login to Heroku client
From your terminal, type :
{% highlight sh %}
$ heroku login 
{% endhighlight %}
and then follow the prompts to enter your email, password and SSH key (it should automatically detect the one you created for github).

You're basically now ready to deploy your app to Heroku, so make sure you are in your app's directory and...

## Cast spell?
Well, almost, but we still need to do a few things... Heroku plays nice with most of the popular frameworks, so we'll just pick a [Ruby](https://devcenter.heroku.com/articles/ruby) based framework (e.g. Sinatra) to illustrate how to deploy your app. We'll use a super barebone application called 'app.rb':

{% highlight ruby %}
require 'sinatra'

get '/' do
  "Hello, world"
end
{% endhighlight %}

### Some configuration necessary
OK so this is the only bit which can get a bit bothersome, so just take your time. At this point, Heroku knows nothing about your app, so we do need to give him some important information. You didn't think it was going to be THAT easy, did you? Bear in mind that you rarely have to redo any of this, it's almost a one-off thing.

#### Gemfile
All your app dependencies should be documented in a Gemfile, e.g:

{% highlight ruby %}
source :rubygems
gem 'sinatra', '1.1.0'
gem 'thin'
{% endhighlight %}

So double check that's the case, and then type:

{% highlight sh %}
$ bundle install
{% endhighlight %}

This will enable Heroku to automatically re-create the environment you are using with all the required dependencies.

#### Declare process type with Procfile
This bit may be optional depending on the environement, framework and language you're using, but the idea here is to let Heroku know what command is required to start the 'web dyno' (i.e. the web/app server in Heroku speak).

For a Rack based application like Sinatra, it's as simple as creating two files in your root directory. A rackup file 'config.ru' that says two things:
* the name of the main app: 'app.rb' (but don't add the .rb extension.)
* and the command to start the Rack server

{% highlight ruby %}
# ok so putting the './' in front of the app name is SUPER CRITICAL
# assume the server has no clue where his root is and where to find the file

require './app'
run Sinatra::Application

{% endhighlight %}

For completeness sake, you should also add a 'Procfile.txt' in your root folder with the following instruction:

{% highlight ruby %}
web: bundle exec rackup config.ru -p $PORT
{% endhighlight %}

replacing $PORT with the port the app server listens to. But in a strict Sinatra application you can ommit all this, it gets it by default.

#### Create a heroku app and link it to your app
This is our final preparation step. A Heroku app is basically a Git remote coupled with a URL.
Run
{% highlight sh %}
$ heroku create
{% endhighlight %}

This will cerate a Heroku app with a rather formidable name like 'blazing-comet-99814.herokuapp.com' (we'll see later how to rename it to a more digestible format).

You're all set. You've prepared all the files Heroku needs in order to handle your application, and you've created an remote repository on Heroku to accept your incoming application. Thus, the final step:

### Cast spell!
First push your code to the Heroku remote
{% highlight sh %}
$ git push heroku master
{% endhighlight %}
Notice that it's like pushing to Github, except it has the heroku word in there.

And then, you can simpy open yur browser and point to your app with one nifty command line:
{% highlight sh %}
$ heroku open
{% endhighlight %}
Which will open your default browser and point to 'blazing-comet-99814.herokuapp.com'

And that's it! From now on, every time you want to push an updtae to your hosting server, just '$ git push heroku master'.

## but where the real magic happens is...
If you run a databse powered app, Heroku takes on all its value. TBC.


testing image link:
![alt_text](images/heroku.GIF)

---
to be deleted later
# Markup Guide

# First level section
## Second level section
### Third level section
#### Fourth level section

* List item
  * Sub item
  * Sub item 2
* List it m 2

1. Ordered list item
2. Ordered list item 2
3. Ordered list item 3
  * Sub item 1
  * Sub item 2
4. Ordered list item 4
  1. Ordered sub item 1
  2. Ordered sub item 2
5. Ordered list item 5


*emphasis text* for emphasis

**strong text** for strong

Getting literal with `backticks`

    Or use an indent of 4 spaces,
    to get yourself a code block,
    that looks lovely.

> Do a bit of blockquoting. You can still reflow the text as much as you like.
Newlines are awesome.
And made of win.

[links for nerds](http://slashdot.org)

[links for internal stuff](section8.html)

This is a horizonal rule:

******

If you want to highlight some ruby code:

{% highlight ruby %}
def foo
  puts 'foo'
end
{% endhighlight %}

Bit of command line:

{% highlight sh %}
$ holla holla
get dolla
$ 
{% endhighlight %}

For a more complete list of languages see [Pygments languages](http://pygments.org/docs/lexers/)

