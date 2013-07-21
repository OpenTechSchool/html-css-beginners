---

layout: ots
title: Pushing to Heroku

---

> This extra is lovingly provided by our coach [funkybrain](https://Github.com/funkybrain).

In this module we'll explore how to host your snazzy webapp on [Heroku](http://www.heroku.com).
What's Heroku? It's a hosting provider that, amongst many things, tries to simplify
your life with regards to deploying and hosting your application.
Why Heroku? Simply because Heroku works like magic with Git! This means that you can
save yourself all the headaches of app deployment and server maintenance.
Oh, and Heroku is free for casual users, i.e. if you have very little traffic.

Note: this module is written assuming you are programming with Ruby. If you want to try and push to Heroku using another language/framework (e.g. Python/Django) we can probably work it out, just grab one of the coaches.

# The Hosting Conundrun

Learning to code is a fun, creative endeavour. At some point, you may want to share your creation with the world... and depending on the technology you used, this can become a real thorn in your side. There's enough to do without having to get pulled into the complexities of deploying, maintaining and scaling your webapp on a public-facing server. The skills required are quite specific and go beyond coding your application.

Enter hosting services like Heroku. Hosting providers really try and simplify your life so that you can focus on your app, and not worry about all the piping and infrastructure necessary to make it run. The beauty of Heroku, as we will see, is that it makes deploying your application incredibly easy when you're a Git afficionado. And you are one, right?

# Playing with Heroku

## Setup

What we're going to do is create a Heroku account, and set-up Git so that it knows where to push your code when you want to send it to Heroku instead of your GitHub account.

You can either follow along the Heroku [Getting Started](https://devcenter.heroku.com/articles/quickstart) doc, or read on here to get a bit more context.

### Create a Heroku Account
This is the easiest bit! Head down to the [sign up](https://api.heroku.com/signup/devcenter) page and enter your email address. You'll receive the usual confirmation email etc. Make a good note of the email and password you created, as *it will be requested to login* from your console.

### Install the Heroku Client on Your Machine
Referred to as the 'Heroku Toolbelt', it has all the client-side code-magic to enable you to use Heroku from your console/terminal. Just pick the right OS from the [download page](https://toolbelt.heroku.com/) and install away. It will add the Heroku install directory to your path automatically.

### Login to the Heroku Client
From your terminal, type :
{% highlight sh %}
$ heroku login 
{% endhighlight %}
and then follow the prompts to enter your email, password and SSH key (it should automatically detect the one you created for GitHub).

You're basically now ready to deploy your app to Heroku, so make sure you are in your app's directory and get ready for some magic.

### Cast spell?
Well... almost, but we still need to do a few things. Heroku plays nice with most of the popular frameworks, so we'll just pick a [Ruby](https://devcenter.heroku.com/articles/ruby) based framework (e.g. [Sinatra](http://www.sinatrarb.com)) to illustrate how to deploy your app. We'll use a super barebone application called `app.rb` for our example, but you should use your exisitng web app and choose the appropriate parameters:

{% highlight ruby %}
require 'sinatra'

get '/' do
  "Hello, world"
end
{% endhighlight %}

Yep, that's our webapp ^^

### Some Configuration Necessary
OK so this is the only bit which can get a bit bothersome, so just take your time. At this point, Heroku knows nothing about your app, so we do need to give it some important information. You didn't think it was going to be THAT easy, did you? Bear in mind that you rarely have to redo any of this, it's mostly a one-off thing.

### Gemfile
All your app dependencies (e.g. Ruby gems) should be documented in a `Gemfile`, e.g:

{% highlight ruby %}
source :rubygems
gem 'sinatra', '1.1.0'
gem 'thin'
{% endhighlight %}

So double check that's the case, and then type:

{% highlight sh %}
$ bundle install
{% endhighlight %}

This will enable Heroku to automatically re-create the environment you are using with all the required dependencies using [bundler](http://gembundler.com/).

### Declare Process Type With Procfile
This part may be optional depending on the environment, framework and language you're using. The idea here is to let Heroku know what command is required to start the 'web dyno' (i.e. the web/app server in Heroku speak).

For a Rack based application like Sinatra, it's as simple as creating two files in your root directory.

A rackup file `config.ru` that says two things:
* The name of the main app: `app.rb` (but don't add the `.rb` extension.)
* And the command to start the Rack server

{% highlight ruby %}
//putting the './' in front of the app name is SUPER CRITICAL
//assume the server has no clue where his root is and where to find the file

require './app'
run Sinatra::Application

{% endhighlight %}

For completeness sake, you should also add a `Procfile.txt` in your root folder with the following instruction:

{% highlight ruby %}
web: bundle exec rackup config.ru -p $PORT
{% endhighlight %}

Replacing `$PORT` with the port the app server listens to. But in a strict Sinatra application you can omit all of this, it gets it by default.

### Create a Heroku App and link it to your WebApp
This is our final preparation step. A Heroku app is basically a Git remote repository coupled with a URL where your application will be visible to the world.

Run:
{% highlight sh %}
$ heroku create
{% endhighlight %}

This will create a Heroku app with a rather formidable name such as `blazing-comet-9984.herokuapp.com` (we'll see later how to rename it to a more digestible format).

You're all set. You've prepared all the files Heroku needs in order to handle your application, and you've created a remote repository on Heroku to accept your incoming application. Thus, the final step:

## Cast Spell!
First, push your code to the Heroku remote
{% highlight sh %}
$ git push heroku master
{% endhighlight %}
Notice that it's like pushing to GitHub, except it has the `heroku` word in there.

And then, you can simply open your browser and point to your app with one nifty command line:
{% highlight sh %}
$ heroku open
{% endhighlight %}
Which will open your default browser and point to `http://blazing-comet-99814.herokuapp.com`

And that's it! From now on, every time you want to push an update to your hosting server, just use `$ git push heroku master`.

## Renaming your webapp's URL
Clearly `http://blazing-comet-99814.herokuapp.com` is not the most user friendly URL. Not surprisingly, Heroku allows you to rename the URL's prefix. (you can also use [custom domain](https://devcenter.heroku.com/articles/custom-domains) names if you get very serious about your app).

Make sure you are in your app's root directory and type:

{% highlight sh %}
heroku apps:rename newname
{% endhighlight %}

Replacing `newname` with the name you want. And, voila, you can now access your app at `http://newname.herokuapp.com`

# But Where the Real Magic Happens is...
If you want to delve further into Heroku, let me tell you that if you run a database powered webapp, Heroku will really shine. It makes deployment and maintenance of your DB a much simpler affair. DB development is a whole other topic, but with Heroku you will be surprised by how quickly you'll be able to run your webapp with a DB in the backend. I encourage you to read Heroku's [doc](https://devcenter.heroku.com/categories/heroku-postgres) on the subject to wet your appetite. And while Heroku is very much a PostgreSQL centered service, there are a number of other options available, though not always free (unlike the PostrgeSQL basic plan which is free!)

If you made it this far, great job! If you are looking for a Hosting provider, I encourage you to shop around. I like Heroku, but there are plenty of solutions out there, and more coming out every 6 months, so find the one that best suits your needs.
