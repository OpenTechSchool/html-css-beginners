--------------

layout: ots title: The template structure

--------------

Preamble: How to write a HTML document
--------------------------------------

This is actually pretty simple: HTML is written as a plain text
document. A HTML file always uses the extension **.html** to indicate
its filetype.

Text editor
-----------

You will need a plain text editor in order to edit HTML files.

You can also get fully graphical WYSIWYG (What You See Is What You Get)
HTML editors, that let you edit the web page graphically with a similar
interface to programs like Word. These can be useful, but many people
working with HTML & CSS prefer a plain text editor and that's what we'll
be using today.

If you already have a plain text editor installed (perhaps from a
previous OTS workshop) then you'll be fine. Otherwise here are some
suggestions:

Windows
~~~~~~~

`Notepad++ <http://www.notepad-plus-plus.org/>`__ is free and suitable,
or you could try `Sublime Text <http://www.sublimetext.com/>`__.

OS X
~~~~

`TextWrangler <http://www.barebones.com/products/textwrangler/>`__ is
free and suitable. Other good choices (with a few more advanced features
you can grow into) include `Sublime
Text <http://www.sublimetext.com/>`__ or `Text
Mate <http://macromates.com/>`__.

Linux
~~~~~

GEdit comes pre-installed on many Linux distributions. Otherwise you
might want to try `Sublime Text <http://www.sublimetext.com/>`__ or one
of the dozens of other text editors available on Linux.

--------------

**Text editor up and running? Great, time to create an HTML document!**

Doctype
-------

The ﬁrst thing on an HTML page is the **doctype**, which as you might
guess, tells the browser what type of document it's looking at, and how
to read it.

Thankfully, HTML5's doctype is extremely simple - it's just ``html``.

Open a new file in your editor and write this line first:

::

    <!DOCTYPE html>

Then save it with the file extension ``.html``. You're now officially
editing an html document!

Structuring your project
------------------------

You can create your HTML files anywhere you like, but we recommend you
use directories to organise things so they're easy to find later.

-  Create a directory somewhere (your home folder, or your desktop) for
   this workshop. Name it something like *OTS\_HTML\_Workshop*.

-  Create another directory inside that one for this first exercise.
   Name it something like *exercise1*.

-  From inside your editor, save your first HTML file inside the
   *exercise1* directory. Name it something like *page.html*.

As time goes by, we will be adding more files to this directory and
eventually adding whole new directories alongside exercise1 for new
projects.

Elements and Tags
-----------------

These are the basic building blocks of HTML.

**Elements** *are* what makes up a HTML document. Because you can have
zero, one or more elements inside another, this is what makes HTML
*heirarchical*. An element can include three things: a tag, attributes,
and content.

A **Tag** is the thing that indicates an element's purpose. For example,
the ``<p>`` tag indicates a paragraph of text is in that element, and
the ``<li>`` represents a 'list item'. You'll notice they're always
surrounded by angle backets. *Opening* and *Closing* tags mark the
beginning and end of an element and wrap its content, like so:

::

    <p>This is a paragraph.</p>

You can see the closing tag includes a ``/`` before its name; otherwise
it would be another opening tag!

**Always** double-check that you've closed all your elements; otherwise,
a browser can and will get mixed up trying to understand your HTML
document.

There are some specific elements that are exceptions to this rule. When
elements cannot contain anything else, then they don't need to be
closed. For example, the following elements are referred to as
'self-closing':

::

    <hr>
    <input>
    <img>

There aren't so many of such elements, and you should easily pick up
which are which by writing some more code :)

Lastly, *nesting* elements isn't so hard, and is fundamental to how HTML
works. It looks just like this:

::

    <p>This is a sentence, with a <span>span</span> element inside it.</p>

or this:

::

    <div id="first-heading">
        <h1>The h1 tags indicates the primary header of the document</h1>
    </div>

You'll notice that HTML doesn't actually care about the whitespace or
newlines *between* tags. It would end up looking the same if the above
had been fit onto one line.

In the above example, you can see our first case of an **attribute**. It
starts with a lowercase name, and then is almost always followed by an
``=`` and a 'value' that's surrounded in double quotes, ``"like this"``.
An element can have many attributes, in which case you separate them by
spaces, as you'll see soon. Attributes give information about an element
in particular.

In this case, the ``<div>`` tag (which is used to *divide* groups of
elements up) has an ``id`` attribute assigned to ``first-heading``.
That's telling us that this section of the document is designed to hold
the first heading shown on the page. You will learn more about specific
attributes later!

Html and Head Elements
----------------------

Coming back to our file (hope you're coding along!), after the doctype
we begin our document with a root ``html`` element, just like so:

::

    <html>
    </html>

It encompasses every other element in our HTML document, nothing should
go outside it! Next, the document is broken up into two important parts:
The **head** and **body**.

The head contains the title of the page & information **about** the page
(*meta* information). Most meta information isn't visible to the user,
but it has many purposes. For example, meta elements can tell search
engines information about your page, such as who created it and a
description of your page's content. Here's an example ``head`` element:

::

    <head>
        <meta charset="UTF-8"> 
        <meta name="description" content="Free Web tutorials">
        <title>My first Portfolio</title>
    </head>

You can see meta tags are one of the self-closing elements! First off,
there is a charset meta tag. This is the most important meta tag.
Without it your website might not display properly. It is best practice
to include it as the first element inside the head element. Basically,
it specifies to the browser the character encoding for the HTML
document. That means your browser will be able to read and correctly
display all the special characters such as €, $, è and so on. ``UTF-8``
is usually the best general encoding to use.

Here we've also written another type of a meta tag, the description. We
define what kind of meta tag it is with the ``name`` attribute and put
our description in the *value* of the content attribute.

Inside our head element, we have lastly written a title of our website.
Chuck the above code in your file (inside your ``html`` element), and
change the content of the ``<title>``. Then you can check your document
by opening your file in a browser and looking at what is written in your
browser toolbar. That also provides a title for the page when it is
added to favorites.

Head tags can also include external files or resources, such as CSS or
JavaScript files. We will see later how to do this.

The Body
--------

Finally, we are at the place where our content goes. The body contains
the actual content of the page. Everything that is contained in the body
is visible to the user.

Just after the closing head tag but still inside the html element, let's
add the body tags.

::

    <body>
    </body>

Everything that is written inside this tag will be displayed to the
user. Add a ``<body>`` to your existing HTML document and then write
some plain text between the body tags and view it in your browser.

**TIP**: To reload the same HTML document in the browser, use the Reload
Current Page function (Ctrl-R or F5)

Types of content
----------------

There are different HTML elements that we can use to indicate different
types of content in our document, like the

.. raw:: html

   <p></p> 

tags which we have already met. Let's try writing a title, followed by a
paragraph.

::

    <body>
        <h1>I'm the title.</h1>
        <p>And I'm a paragraph!</p>
    </body>

Heading elements are straightforward to understand. They start from h1
with the biggest font and importance, going to h6 with the smallest
font.

Indentation
-----------

Are you wondering why we wrote the h1 and p tags *indented* inside the
body tags?

That will not change at all how the browser reads or interpretates the
document, but it is a good practice among developers to write code like
that in order to have a more clear document and still be able to work
with it even after a long time or when there is a lot of lines of code.
It also shows the heircharcical nature of HTML pretty well.

Comments
--------

It is also possible to put "comments" in your HTML. Comments in HTML are
there to remind you (or other people editing the HTML file) without
changing the way the page displays in a browser.

Like other HTML elements, comments are written by using a tag. Although
comment tags look a little different:

::

    <!-- I am a comment -->

The "start comment" tag is ``<!--`` and the "end comment" tag is
``-->``.

Comments can also enclose other HTML elements, to "comment them out".
This is a useful technique when you're experimenting with a page to see
how it looks when you change things around.

For example, try commenting out the ``h1`` heading in your current page:

::

    <body>
        <!-- <h1>I'm the title.</h1> -->
        <p>And I'm a paragraph!</p>
    </body>

If you reload the page in your browser, you'll notice the heading has
vanished.

Remove the comment tags (so the heading appears again) before moving on
to the next section.

Images
------

Headings and paragraphs give you the basics of text. What about images?

Images have to kept in separate image files, outside the HTML file. Find
a favourite image on the web and save it in the same directory as your
HTML file (right-click the image in your browser and "Save Image...").

If you don't have a picture in mind then `here's a page with a photo of
some kittens that you can
use <http://www.flickr.com/photos/nengard/67501122/sizes/s/>`__ (Cute
cats on the internet? Egad!)

After you have your image, you can include it in your HTML page by using
an ``<img>`` tag.

::

    <img src="kittens.jpg">

Add the ``<img>`` tag anywhere inside the "body" of your HTML document
where you'd like the image to appear. Replace "kittens.jpg" with the
file name of the image that you saved in the same directory as the HTML
file.

Notice that ``<img>`` is one of the tags that doesn't need a sepaate
closing tag. You could put ``</img>`` after the tag if you like, it
doesn't change the way the browser views the page.

**TIP:** The image source name ("src") of ``kittens.jpg`` is a path
relative to the HTML document. So in this case ``kittens.jpg`` is
located in the same directory, but you could use a name like
``"images/kittens.jpg"`` if you put the image file into a subdirectory
called "images". You can even use full URLs like
``"http://myawesomesite.com/pictures/kittens.jpg"``, but it's best to
avoid this if you can use a relative path instead.

Alt Text
~~~~~~~~

A good habit to get into is using "alt text" to describe the contents of
an image:

::

    <img src="kittens.jpg" alt="Some kittens">

The alt text is a textual description of what's in the image. This is
important for anyone who can't see the images (for instance vision
impaired people using a screenreader.) Any image that isn't purely
decorative should have a description set with the "alt=" attribute.

Putting it all together
-----------------------

So far, our entire document might look like this:

::

    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8"> 
            <meta name="description" content="Free Web tutorials">
            <title>My first Portfolio</title>
        </head>
        <body>
            <h1>I'm the title.</h1>
            <p>And I'm a paragraph!</p>
            <p>
                 <img src="kittens.jpg" alt="All the kittens are shown here">
            </p>
            <h3>This is a sub-heading...</h3>
            <p>Well now we're just blathering on.</p>
        </body>
    </html>

Notice that the kitten image is part of its own paragraph here, so it is
shown on a new line in the browser.

Hopefully the document in your file looks similar, but not exactly the
same. You might have changed some of the text... does it all work in
your browser?

Why not use Word?
-----------------

You might wonder why you're writing all these elements by hand, when you
could make up the same stuff in a Word document.

Well, think about some of the cooler websites around that you've seen on
the web, and their complex layouts. Do you think you could replicate
them using Word? How long might it take? That's the power of manual
control that HTML (and CSS, and Javascript) gives to the web and web
developers. You can learn it too!

What's next?
------------

You may be thinking at this stage that your HTML page looks pretty
bland. How can you spice it up a little?

Read on to find out in the next section, `your first styled Hello
World! <style.html>`__.
