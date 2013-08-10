---

layout: ots
title: GitHub Wikis

---

Every repository on GitHub can have a wiki enabled for it. It's not
the most complete wiki platform, but it does make it very easy to
host documentation without any fuss.

As an example, take a look at the
[Resque](https://github.com/resque/resque) repository, which has a
very [simple wiki](https://github.com/resque/resque/wiki) containing
a few of the things that you usually don't add to the main
repository. In this case there are a few links to presentations about
the project, and lists of links to similar projects.

The key difference between repositories and wikis are that wikis are
*open by default*. Anybody can make changes to the wiki without having
to clone or create a pull request. As the wiki owner, you will not
receive any notifications to changes that others make to your
wiki.

You can enable your repository wiki using the GitHub web interface, in
the *Admin* tab of your repository.

## Bonus

A GitHub wiki is also a Git repository. So you can have a local copy
of everything, and even make wiki changes locally before pushing them
to GitHub. To clone it, add a ``.wiki`` to the url, like so:

    $ git clone https://github.com/defunkt/resque.wiki.git
