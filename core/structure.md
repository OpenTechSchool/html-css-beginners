---

layout: ots
title: The template structure

---

# Doctype

The ﬁrst thing on an HTML page is the doctype, which tells the browser which 
version of the markup language the page is using.

Open a new file in your editor and write this line as first:

    <!Doctype html>
    
The doctype is case-insensitive. 
DOCtype, doctype, DocType and DoCtYpe are all valid


# What is a tag?

We already have met the most important html elemnt: a tag.
Is a way to give a structure in an HTML document and a way to organize the 
content in a hierarchy.

Tags contain characters that indicate the tags purpose. Like <p></p> tag is 
about paragraph or <li></li> stay for list.
Tags marks the beginning & end of an element and wrap the content of this element,
that's why is always foundamental open and close our tag as we just saw.

	<p>This is a paragraph</p>

Always double check if you closed all your tags, otherwise the browser can't understand what
the code is about and will not display the content correctly.

There are also some exception, elements that cannot contain anything else like

	<br/>
	<input>
	<img>

But they aren't so many and you could easily learn them writing more code :)

## Html and Head tag

Coming back to our file, after the doctype we need to tell to the browser that 
this is a html file

	<html>
	</html>

Inside the html tag we can write all our html elemnts.
We basically have two block: head and body.
Head contains the title of the page & meta information about the page.
Most of the information are not visible to the user, but has many purposes.
For example meta tag are also good to tell search engines about your page,
who created it, and a description.

	<head>
		<title> My first Portfolio </title>
		<meta charset='utf-8'> 
		<meta name="description" content="Free Web tutorials">
	</head>

Inside our head tag, we first wrote a title of our website.
Give a first check, open your file in any browsers and look what is write 
in your browser toolbar. That's also provides a title for the page when it is added to favorites.

At the end we write one of the different type of meta tag, the description. We define 
which kind of meta tag is in name="description" and our description in content="".

Last but not least there is a charset='utf-8'. 
This one is the most important meta tag and without it your web site will not display
properly. Is always a good practice to include it right after the title tag.
Basically specifies to the browser the character encoding for the HTML document.
That's mean your browser will be able to read and correctly display all the special character as
€, $, è and so on.

Head tag is also made for include external files or resource as css or javascript files.
We will see later how to do this.

## Body tag

Finally we are at the place where our content goes.
The body contains the actual content of the page. Everything that is contained in
the body is visible to the user.

Just after a head tag but still inside the html tag let's add the body.

	<body>
	</body>

Now we can see that everything is written inside this tag will be displayed in
the browser.
Try to write plain text and check the file in your browser.

There are differents html elements that we can use to give a default style to 
our document like the <p></p> that we already met.
Let's try to write a title followed by a paragraph.

	<body>
		<h1>I'm the title</h1>
		<p>I'm a paragraph</p>
	</body>

Titles are straightforward to understand. They starting from h1 with the biggest going 
until h6 with the smaller.

******

Are you wondering why we wrote the h1 and p tags bit inside respect of body tag?

That will not change at all how the browser read or interpretate the document but
is a good practice between developer write code like that in order to have more clear 
document and still be able to work with it even after long time or when code lines
are a lot.

******

Html give us a chance to play little bit with the style without needing a css yet.
There are some default style like **< b >** for bold text or  **< i >** for italic text.

These tags are intended to wrap the text and stay inside the main html elements which 
they will stylize.

	<p><b> I'm a bold text </b></p>

**You can check on your html cheat sheet and try to play around with differents html
elements and default style.**

Before move to make your file look nicer, we should introduce another relevant tag,
the image tag.
<img> tag place an image in an html page. 
The image tag not need to be closed because doesn't contain anything. Infact the image
carried by this tag will be linked thanks to one of the attributes.

Attributes is a modifier of an HTML element. It work like that:
<tag attribute="value"></tag>

Image tag has several attributes the most important is src, the one that will link the 
the image file.

	<img src="images/cat.jpg">

The src attributes specifies the URL of an image. 

There are at least other three important attributes: alt, width and height.
**Alt** specifies an alternate text for an image. Is important in particular if for some
reason the user can't see the image, and still can know what is about the missing image.
**Width** and **height** as you can image, will set the size of the image.
Let's update our image tag.

	<img src="iamges/cat.jpg" alt="little cat" width="200" height="150">

Look in your browser and.. the image is there!

**Add another one or two image and play a little bit with them**	





