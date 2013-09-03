---

layout: ots
title: Your first styled Hello World!

---
## Writing css

There are two ways to write a css for a document.

An internal CSS code can be typed in the head section of the code.
The coding is started with the style tag, written just before the closing
head tag.
	
	<style type="text/css">
		....
	</style>

This way is good to use when you not many style. In this case is easier
to referred and browser not need to load another file.

Or an "external" CSS file. First you need to open a new file in your editor
and save it with .css extension.
Than you can associated with an HTML document using the following syntax. 
Write it just after the meta tag.

	<link href="path/toyour/file.css" rel="stylesheet">

That's the best way if you have a lot of css to write and you want to 
keep it organize.

Once you linked your external css file, open yoout html file in the
browser, open your console and go in the Network tab.
You should see the path of your css file and under the STATUS coloum 
see a *200 OK* response.
That mean your file is read from your browser and linked at your html 
in the right way.
Now we are ready to work with it.

## Let's give some colors!

CSS has a simple syntax.
The file consists of a list of rules. Each rule consists of one or more
selectors, and a declaration block.

**Selector** are used to declare which part of the markup a style applies to.
Let's take the h1 title we wrote in our html file and give to it a nice red color.

	h1 { 
		color: red;
	}

h1 is the selector. The html elemnts we want to style.
*color* is one of the property that we can give to our selector and *red* is the 
value of this property.
The right sytrax is:

	selector {
		property: value; ** remember always to write a ; after your value **
		property: value;
	}	

Refresh your browser and see how the color of you title is changed.

Isn't it nice?
For give a backgorund color to our paragph will write

	p {
		background-color: #ddd;
	} 	

******

Web colors are colors used in designing web pages. 
Colors may be specified as an RGB triplet or in hexadecimal format (a hex triplet).
Hexadecimal color codes begin with a number sign (#).
This number sign can be picked from a Graphics software or from some nice web tool.
For example: [Color picker](http://www.colorpicker.com/)
Choose the color, copy the number that start with # and than past in your css file.

Good to know: #000 is black and #fff is white.

******
	

Let's try now to give a nicer border to our images.

	img {
		border: 1px solid #000;
	}	

Here we are givin the style to all the img tags we have, giving 1px thicK,
solid and black to all the four borders of our images.
If we would like to give the style just to one of the four border we should write

	img {
		border-top: 1px solid #000;
	}

**Look at your css cheat sheet and giev some more style to your images. **







