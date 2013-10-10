---

layout: ots
title: The template structure

---

### Preamble: How to write a HTML document

This is actually pretty simple: HTML is written in just a plain text document. 
Even Microsoft Notepad can write one just fine, although you might wish to use 
a code editor like Sublime Text, Gedit, or Textmate instead. 

A HTML file always uses the extension **.html** to indicate its filetype.

# Doctype

The ﬁrst thing on a HTML page is the **doctype**, which as you might guess, 
tells the browser what type of document it's looking at, and how to read it.

Thankfully, HTML5's doctype is extremely simple - it's just `html`.

Open a new file in your editor and write this line first:

{% highlight html %}
<!DOCTYPE html>
{% endhighlight %}

You're now officially editing a html document!

# Elements and Tags

These are the basic building blocks of HTML.

**Elements** *are* what makes up a HTML document. Because you can have zero, 
one or more elements inside another, this is what makes HTML *heirarchical*. 
An element can include three things: a tag, attributes, and content.

A **Tag** is the thing that indicates an element's purpose. For example, 
the `<p>` tag indicates a paragraph of text is in that element, and the `<li>` 
represents a 'list item'. You'll notice they're always surrounded by angle 
backets. *Opening* and *Closing* tags mark the beginning and end of an 
element and wrap its content, like so:

{% highlight html %}
<p>This is a paragraph.</p>
{% endhighlight %}

You can see the closing tag includes a `/` before its name; otherwise it would 
be another opening tag!

**Always** double-check that you've closed all your elements; otherwise, a 
browser can and will get mixed up trying to understand your HTML document.

There are some specific elements that are exceptions to this rule. 
When elements cannot contain anything else, then they don't need to be closed. 
For example, the following elements are referred to as 'self-closing':

{% highlight html %}
<hr>
<input>
<img>
{% endhighlight %}

There aren't so many of such elements, and you should easily pick up which are 
which by writing some more code :)

Lastly, *nesting* elements isn't so hard, and is fundamental to how HTML works. 
It looks just like this:

{% highlight html %}
<p>This is a sentence, with a <span>span</span> element inside it.</p>
{% endhighlight %}

or this:

{% highlight html %}
<div id="page-title">
    <h1>The h1 tags indicates the primary header of the document</h1>
</div>
{% endhighlight %}

You'll notice that HTML doesn't actually care about the whitespace or 
newlines *between* tags. It would end up looking the same if the above had 
been fit onto one line.

In the above example, you can see our first case of an **attribute**. It 
starts with a lowercase name, and then is almost always followed by an 
`=` and a 'value' that's surrounded in double quotes, `"like this"`. An element 
can have many attributes, in which case you separate them by spaces, as you'll 
see soon. Attributes give information about an element in particular.

In this case, the `<div>` tag (which is used to *divide* groups of elements up)
has an `id` attribute assigned to `page-title`. That's telling us that this 
section of the document is designed to hold the page's main title. You will 
learn more about specific attributes later!

## Html and Head Elements

Coming back to our file (hope you're coding along!), after the doctype we 
begin our document with a root `html` element, just like so:

{% highlight html %}
<html>
</html>
{% endhighlight %}

It encompasses every other element in our HTML document, nothing should go 
outside it! Next, the document is broken up into two important parts: 
The **head** and **body**.

The head contains the title of the page & information **about** the page 
(*meta* information). Most meta information isn't visible to the user, 
but it has many purposes. For example, meta elements can tell search engines 
information about your page, such as who created it and a description of 
your page's content. Here's an example `head` element:

{% highlight html %}
<head>
    <meta charset="UTF-8"> 
    <meta name="description" content="Free Web tutorials">
    <title>My first Portfolio</title>
</head>
{% endhighlight %}

You can see meta tags are one of the self-closing elements! 
First off, there is a charset meta tag. 
This is the most important meta tag. Without it your website might not display 
properly. It is best practice to include it as the first element inside the 
head element. Basically, it specifies to the browser the character encoding 
for the HTML document. That means your browser will be able to read and 
correctly display all the special characters such as €, $, è and so on. `uft-8` 
is usually the best general encoding to use.

Here we've also written another type of a meta tag, the description. 
We define what kind of meta tag it is with the `name` attribute and put our 
description in the *value* of the content attribute.

Inside our head element, we have lastly written a title of our website. Chuck 
the above code in your file (inside your `html` element), and change the 
content of the `<title>`. Then you can check your document by opening your 
file in a browser and looking at what is written in your browser toolbar. 
That also provides a title for the page when it is added to favorites.

Head tags can also include external files or resources, such as CSS or 
JavaScript files. We will see later how to do this.

## The Body

Finally, we are at the place where our content goes. 
The body contains the actual content of the page. Everything that is 
contained in the body is visible to the user.

Just after the closing head tag but still inside the html element, 
let's add the body tags.

{% highlight html %}
<body>
</body>
{% endhighlight %}

Everything that is written inside this tag will be displayed to the user.
Try to write some plain text between the body tags and check the file 
in your browser.

There are different HTML elements that we can use to indicate different types 
of content in our document, like the <p></p> tags which we have already met.
Let's try writing a title, followed by a paragraph.

{% highlight html %}
<body>
    <h1>I'm the title.</h1>
    <p>And I'm a paragraph!</p>
</body>
{% endhighlight %}

Heading elements are straightforward to understand. They start from h1 with the 
biggest font and importance, going to h6 with the smallest font.

******

Are you wondering why we wrote the h1 and p tags *indented* inside 
the body tags?

That will not change at all how the browser reads or interpretates the 
document, but it is a good practice among developers to write code like that 
in order to have a more clear document and still be able to work with it 
even after a long time or when there is a lot of lines of code. It also shows 
the heircharcical nature of HTML pretty well.

******

So far, our entire document might look like this:

{% highlight html %}
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
        <h3>This is a sub-heading...</h3>
        <p>Well now we're just blathering on.</p>
    </body>
</html>
{% endhighlight %}


Hopefully the document in your file looks similar, but not exactly the same. 
You might have changed some of the text... does it all work in your browser?

There are two questions you might be asking, which we intend to answer:

1. Right now I can basically write paragraphs and headers. What are some other 
   HTML elements and how can I use them? How would I get a picture?

2. Ok, so I have some content, but this looks utterly bland. How do I spice it 
   up a little?

Read on to find out!

******

lastly, you might also wonder why you're writing all these elements by hand, 
when you could make up the same stuff in a Word document.

Well, think about some of the cooler websites around that you've seen on the 
web, and their complex layouts. Do you think you could replicate them 
using Word? How long might it take? That's the power of manual control that 
HTML (and CSS, and Javascript) gives to the web and web developers. You can 
learn it too!
