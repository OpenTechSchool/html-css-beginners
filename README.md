---
layout: ots
title: README
---

This is a friendly how-to for contributors to the HTML and CSS workshop
at OpenTechSchool.
About the course:

An HTML and CSS basic workshop for beginners that never write HTML/CSS before and
want to know how to start.

# Class format

At OpenTechSchool we tend to go *practical* and *at your own pace*.

At your own pace means that we provide access to the complete course notes at
the beginning of the session. Then students can progress individually. Some
students will get through very quickly, others will take some time, and others
will finish the core work with time to spare. The core work should be
completable by everyone. To keep things interesting we supply various
additional topics which are entirely optional.

A class schedule looks like this:

    11:00 - Students still arriving, writing name tags, setting up laptops.
    12:30 - Introductions, wifi instructions and location of coursework.
    12:35 - Students learn stuff.
    18:00 - Thankyous, maybe demonstrations.


# Author Guide

So, fork this repository. The guide is written as a [Jekyll](http://jekyllrb.com/)
site, hosted on GitHub pages. It's set up so you can just write pages in Markdown.
A markup guide is below.

Course work goes under `core/` or `extras/`. It's all linked together by
`index.md` in the root direcory.

* `core/` covers the basic goals of the course. In this course that means
  setting up Git, creating a GitHub account, creating a repo, etc etc. Put any
  images in `core/images/`
* `extras/` are all the interesting things people can do once they have
  completed the basics. Things like hosting with GitHub Pages, or doing Pull
  Requests and exploring GitHub can be done here. Put any images in
  `extras/images/`

It's easiest to start at the end. Think of a fun and interesting topic to add to
the extras. Then you can copy this file to get an idea for formatting.

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

[links for internal stuff](section8.HTML)

This is a horizonal rule:

******

If you want to highlight some ruby code:

    def foo
        puts 'foo'
    end

Bit of command line:

    $ holla holla
    get dolla
    $

For a more complete list of languages see [highlight.js](http://softwaremaniacs.org/media/soft/highlight/test.HTML)

