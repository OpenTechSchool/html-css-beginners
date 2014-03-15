---

layout: ots
title: Your first styled Hello World!

---

## Writing CSS

There are two ways to write CSS for a document.

An internal CSS code can be typed in the head section of the code.
The coding starts with the style tag, written just before the closing
`</head>` tag.

    <style type="text/css">
        ....
    </style>

This way is good when you do not have many styles. In such a case, it is easier
to refer to because the browser has no need to load another file.

The second way to write CSS for a document is with an "external" CSS  file. 

Open a new file in your editor and save it with a .CSS extension in the same
directory as your HTML file (give it a name like `styles.css` for now.)

Then you can link that to an HTML document using the following syntax. 
Write it just after the meta tag, before the closing `</head>` tag.

    <link href="styles.css" rel="stylesheet">

This is the best way if you have a lot of CSS to write and you want to 
keep it organized.

**TIP:** The link reference ("href") to `"styles.css"` is a path relative 
to the HTML document, same as the "src" for the `<img>` tag in the previous 
chapter.

## Let's add some colors!

CSS has a simple syntax.
The file consists of a list of rules. Each rule consists of one or more
selectors and a declaration block.

**Selectors** are used to declare which part of the markup a style applies to.
Let's take the h1 title we wrote in our HTML file and give it a nice red color.

    h1 {
        color: red;
    }

h1 is the selector, the HTML element we want to style.
*color* is one of the properties that we can give to our selector, and *red* is the 
value of this property.
The right sytrax is:

    selector {
        property: value; /* remember always to write a semicolon (;) after your value */
        property: value;
    }

Refresh your browser and see how the color of your title has changed.

Isn't it nice?
To give a background color to our paragraph, write

    p {
        background-color: #ddd;
    }

## Troubleshooting

Did the title text color not change when you refreshed?

Double check the name of the CSS file in the `<link>` tag, and also 
double check that the CSS file is in the same directory as the HTML 
file.

Also make sure that all rules end with a ; and are placed inside of the curly brackets of the selector you want to style.

******

Web colors are colors used in designing web pages. 
Colors may be specified as an RGB triplet or in hexadecimal format (a hex triplet).
Hexadecimal color codes begin with a number sign (#).
This number can be picked from a graphics software or from some nice web tool, such as, [Color picker](http://www.colorpicker.com/), for example.
When you have chosen your color, copy the number that starts with # and paste that in your CSS file.

Good to know: #000 is black and #fff is white.

******

Let's try now to give a nice border to our image, that we added to our page in the [first chapter](structure.md).

    img {
        border: 1px solid #000;
    }

Here we are giving the following style to all the img tags we have: a 1-pixel thick, solid black border to all four edges of our images.
If we want to give the style to just one of the four edges, for example, the top edge, we would write

    img {
        border-top: 1px solid #000;
    }

**Look at the [CSS cheat sheet](http://coding.smashingmagazine.com/2009/07/13/css-3-cheat-sheet-pdf/) and give some more styles to your images.**

## A short note on hierarchy

As you learned in [the structure section](structure.html) in HTML you can nest your tags inside of one another like so:

    <div id="main-content">
        <h1>The h1 tag indicates the primary header of the document.</h1>
        <p>Some text.</p>
    </div>

In CSS you can apply hierachical styling like this:

    p {
        color: black;
    }
    div p {
        color: red;
    }

So we have two rules here. The first says the text color in paragraphs should be black. The second rule is more *specific* - it says the text in paragraphs should be red, but only if those paragraphs are inside of a div tag. A more specific rule always beats a less specific rule.

## What's next?

Now you have the basic building blocks to start working on
[your portfolio](portfolio.html)


