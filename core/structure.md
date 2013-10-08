---

layout: ots
title: The template structure

---

# Doctype

The ﬁrst thing on a HTML page is the doctype, which as you might guess, 
tells the browser what type of document it's looking at, and how to read it.

Thankfully, HTML5's doctype is extremely simple - it's just `html`.

Open a new file in your editor and write this line first:

    <!DOCTYPE html>

You're now officially editing a html document!

# What is a tag?

We have already met the most important HTML element: a tag.
This gives structure to an HTML document and organizes the 
content in a hierarchy.

Tags contain characters that indicate the tags' purpose. For example, the <p></p> tags open and close paragraphs and the <li></li> tags wrap around lists.
Tags mark the beginning & end of an element and wrap the content of this element;
that's why it is always necessary to open and close our tags as we just saw.

	<p>This is a paragraph.</p>

Always double-check if you closed all your tags; otherwise, the browser can't understand what
the code is about and will not display the content correctly.

There are also some tags that are exceptions to this rule. When elements cannot contain anything else, then they don't need to be closed. For example, the following tags do not need to be closed.

	<br/>
	<input>
	<img>

There aren't so many of such tags, and you could easily learn them by writing more code :)

## HTML and Head tag

Coming back to our file, after the doctype we need to tell the browser that 
this is a HTML file with the following tags:

	<HTML>
	</HTML>

Inside the HTML tag we can write all our HTML elements.
We basically have two blocks: head and body.
Head contains the title of the page & the meta information about the page.
Most of the meta information are not visible to the user but has many purposes.
For example, meta tags tell search engines information about your page, such as who created it and a description of your page's content.

	<head>
		<title> My first Portfolio </title>
		<meta charset='utf-8'> 
		<meta name="description" content="Free Web tutorials">
	</head>

Inside our head tag, we first write a title of our website.
Check your website by opening your file in any browser and looking at what is written in your browser toolbar. That also provides a title for the page when it is added to favorites.

At the end we write another type of a meta tag, the description. We define 
what kind of meta tag it is in the name="description" and our description in the content="".

Last but not least there is a charset='utf-8' meta tag. 
This is the most important meta tag. Without it your website will not display
properly. It is always a good practice to include it right after the title tag.
Basically, it specifies to the browser the character encoding for the HTML document.
That means your browser will be able to read and correctly display all the special characters such as
€, $, è and so on.

Head tags can also include external files or resources, such as CSS or JavaScript files.
We will see later how to do this.

## Body tag

Finally, we are at the place where our content goes.
The body contains the actual content of the page. Everything that is contained in
the body is visible to the user.

Just after a head tag but still inside the HTML tag, let's add the body tags.

	<body>
	</body>

Everything that is written inside this tag will be displayed in
the browser.
Try to write some plain text between the body tags and check the file in your browser.

There are differents HTML elements that we can use to give a default style to 
our document like the <p></p> tags which we have already met.
Let's try to write a title followed by a paragraph.

	<body>
		<h1>I'm the title</h1>
		<p>I'm a paragraph</p>
	</body>

Title tags are straightforward to understand. They start from h1 with the biggest font going 
to h6 with the smallest font.

******

Are you wondering why we wrote the h1 and p tags inside the body tags?

That will not change at all how the browser reads or interpretates the document, but it
is a good practice among developers to write code like that in order to have a more clear 
document and still be able to work with it even after a long time or when ther are a lot of lines of code.

******

HTML gives us a chance to play a little bit with the style without needing a CSS yet.
There are some default styles like **< b >** for bold text or  **< i >** for italic text.

These tags are intended to wrap the text and stay inside the main HTML elements which 
they style.

	<p><b> I'm a bold text. </b></p>

**You can check your HTML cheat sheet and play around with differents HTML
elements and default styles.**

Before we move on to make your document look nicer, we should introduce another relevant tag,
the image tag.
<img> tag places an image on a HTML page. 
The image tag does not need to be closed, because it doesn't contain anything. In fact, the image
carried by this tag will be linked thanks to one of the attributes.

Attributes are modifiers of a HTML element. It works like this:
<tag attribute="value"></tag>

Image tags have several attributes. The most important attribute is src, which links to the 
the image file.

	<img src="images/cat.jpg">

The src attribute specifies the URL of an image. 

There are at least three other important attributes: alt, width and height.
**Alt** specifies an alternate text for an image. It is important especially if the user can't see the image, so that the user can still know what the missing image is about.
**Width** and **height,** as you can imagine, set the size of the image.
Let's update our image tag.

	<img src="images/cat.jpg" alt="little cat" width="200" height="150">

Look in your browser and... the image is there!

**Add another one or two images and play a little bit with them.**	





