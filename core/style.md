---

layout: ots
title: Your first styled Hello World!

---

## Writing CSS

There are two ways to write CSS for a document.

An internal CSS code can be typed in the head section of the code.
The coding starts with the style tag, written just before the closing
head tag.

    <style type="text/css">
        ....
    </style>

This way is good when you do not have many styles. In such a case, it is easier
to refer to because the browser has no need to load another file.

The second way to write CSS for a document is with an "external" CSS file. First, you open a new file in your editor
and save it with a .CSS extension.
Then, you can link that to a HTML document using the following syntax.
Write it just after the meta tag.

    <link href="path/toyour/file.css" rel="stylesheet">

This is the best way if you have a lot of CSS to write and you want to
keep it organized.

Once you link your external CSS file, open your HTML file in the
browser, open your console and go to the Network tab.
You should see the path of your CSS file and under the STATUS column
see a *200 OK* response.
That means your file is read from your browser and linked to your HTML document
in the right way.
Now we are ready to work with it.

## Let's add some colors!

CSS has a simple syntax.
The file consists of a list of rules. Each rule consists of one or more
selectors and a declaration block.

**Selectors** are used to declare which part of the markup a style applies to.
Let's take the h1 title we wrote in our HTML file and give it a nice red color.

    h1 {
        color: red;
    }

h1 is the selector, the HTML elemnt we want to style.
*color* is one of the properties that we can give to our selector, and *red* is the
value of this property.
The right sytrax is:

    selector {
        property: value; ** remember always to write a ; after your value **
        property: value;
    }

Refresh your browser and see how the color of your title has changed.

Isn't it nice?
To give a background color to our paragraph, write

    p {
        background-color: #ddd;
    }

******

Web colors are colors used in designing web pages.
Colors may be specified as an RGB triplet or in hexadecimal format (a hex triplet).
Hexadecimal color codes begin with a number sign (#).
This number can be picked from a graphics software or from some nice web tool, such as, [Color picker](http://www.colorpicker.com/), for example.
When you have chosen your color, copy the number that starts with # and paste that in your CSS file.

Good to know: #000 is black and #fff is white.

******

Let's try now to give a nice border to our images.

    img {
        border: 1px solid #000;
    }

Here we are giving the following style to all the img tags we have: a 1-pixel thick, solid black border to all four edges of our images.
If we want to give the style to just one of the four edges, for example, the top edge, we would write

    img {
        border-top: 1px solid #000;
    }

**Look at your CSS cheat sheet and give some more styles to your images. **







