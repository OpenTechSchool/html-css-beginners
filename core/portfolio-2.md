---

layout: ots
title: Create your Personal Portfolio

---

So far we built the core of our website. Now we need a home page and a contact page.
Here we explain some basic concepts but after that you have the freedom to experiment.

## Home page and positioning
Let's start from the home page.

**Goal**

The home page is made by: 

* navigation menu
* big centered and resizable image
* two sentence intro text (on the top of the image)

So let's open a new file and set the basic structure. 
To make the nav menu we can just copy what we have done in the first part.
Then, take an image that you like. It should be big enough and with good resolution.

Just after the nav tag, include your image and give it a class name.
Now you need to set the width of just this image as full-width, which is 100%.  

    .home-imag {
        width: 100%
    }

In this way your image will follow the size of the browser window.
It is possible that when the window is very small or very big, you can see a white space at the bottom of the image.
You can change it setting the height: 100%. But now you need to be sure that you image isn't stretched.

    .home-imag {
        height: 100%
    }

After the image, write another header tag within h1 and h2, add a class name to your header so you can style it 
and not be confused with the other one. (I will use header-home as the class name)
In the CSS we are goint to write this:

    .header-home {
        position: relative;
        top: -300px;
    }
Here we are changing the position of this element by bringing it outside of the normal flow. Its position is 
now relative to its parent element (in our case the div#wrap-centered). Now you can move your element where
you prefer in the page using the properties top, right, bottom and left.

So, what is positioning?
When a box is taken out of the normal flow, all the content that is still within normal flow will ignore it 
completely and not make space for it. Elements can be positioned using the top, bottom, left, and right 
properties. These properties will not work, however, unless the position property is set first. They also work
differently depending on the positioning method.

There are four different positioning methods.

**Static positioning**
A statically positioned box is one that is in normal flow, from top to bottom.

**Fixed Positioning**
An element with fixed position is positioned relative to the browser window.
What makes it possible is: position: fixed. 
After setting this, you can play with changing the position, adding a different pixel value to top, bottom, left or right positioning.

**Relative Positioning**
A relatively positioned element is positioned relative to its normal position. Elements that come after a relatively-positioned element behave as if the relatively-positioned element was still in its ‘normal flow’ position - leaving a gap for it.
What makes it possible is: position: relative. 
After setting this, you can play with changing the position, adding a different pixel value to top, bottom, left or right positioning.

**Absolute Positioning**

An absolutely positioned box is moved out of the normal flow entirely.
What makes it possible is: position: absolute. 
After setting this, you can play with changing the position, adding a different pixel value to top, bottom, left or right positioning.

**Overlapping Elements: z-index property**

When elements are positioned outside of the normal flow, they can overlap other elements. The z-index property specifies the stack order of an element (which element should be placed in front of, or behind, the others).
What make it possible is: z-index: n°pixel. 

Knowing all that, create your own home page!




## Contact page
Time to create the contact page!

**Goal**

Create a page with:

* a small paragraph about yourself
* some nice links to contact you

The contact page will have the same structure as the page you created before. So just copy the file and rename it to `contact.html` or something like that.
Then you remove everything inside the `#wrap-centered` div container because that's where you want to display the contact page now.

Next let's add a paragraph to tell the user who you are. You can do that using the `<p> </p>` tag.
Inside that tag you can write some text that will be displayed to the user.
For example: `<p>Hi I am Mr. Smith. Feel free to contact me.</p>`
You also can add a linebreak after the first sentence with a `<br>` tag and maybe you want to highlight your name by making it italic: `<i>Mr. Smith</i>`.
If you want to add more styling to the paragraph you should do that in the CSS file. Just add a class to the paragraph `<p class="contact-intro">` and over in the CSS file add some styling to the text:

    .contact-intro {
        font-size: 20px;
        font-family: Arial;
        margin: 10px;
    }

That's it for the short introduction. Now let's get to the links where visitors of your site can actually contact you.
Just create a list for the different contact options using the `<ul> </ul>` tag (ul for unordered list) and also add a class to the list so you can style it later on: `<ul class="contact-links">`.
For now we want to add links to Mail, Twitter, Facebook and Github. So you have to create four list items with `<li> </li>` tags.
Inside each item you add a link tag so the user of your site can click on something. You can do that using an `<a href="#"> </a>` tag. You can ignore the `href` attribute for now. We will cover that later to make the links actually work. 
In general you can use everything as a link. A button element, an image or just plain text. But let's create a stylish icon using CSS here. 
For doing so add the first letter of the name of each link in the link tag and add some classes to the links so you can style them. Add one class `contact-link` to each link to apply styles to all links and add a unique class for each link (`mail`, `twitter`, `facebook`, `github`). The hole list should look like the following:

    <ul class="contact-links">
        <li><a href="#" class="contact-link mail">m</a></li>
        <li><a href="#" class="contact-link twitter">t</a></li>
        <li><a href="#" class="contact-link facebook">f</a></li>
        <li><a href="#" class="contact-link github">g</a></li>
    </ul>

Now you can style the links using CSS.
You can change the font, create a box for each link in a different colour and position the letter pixel perfect for each link individually.
Here is some simple styling. Have a look at it and adjust it to your needs:

    .contact-links {
        padding: 0;
    }

    .contact-links li {
        list-style: none;
    }

    .contact-link {
        display: block;
        float: left;
        margin: 10px;
        text-decoration: none;
        color: white;
        font-family: Arial;
        font-weight: 900;
        font-size: 35px;
    }

    .mail {
        background: #dd1812;
        width: 39px;
        height: 45px;
        padding: 1px 0 0 9px;
    }

    .twitter {
        background: #00acee;
        width: 30px;
        height: 42px;
        padding: 4px 0 0 18px;
    }

    .facebook {
        background: #3B5998;
        width: 30px;
        height: 42px;
        padding: 4px 0 0 18px;
    }

    .github {
        background: #171515;
        width: 35px;
        height: 46px;
        padding: 0 0 0 13px;
    }

That's it for this section. Feel free to extend and customize the contact page in every way you can imagine.




## a tag

Good! Our portfolio is almost ready.
Now we need just one more thing: to link all your pages together.
To do that there is a special tag: a tag (anchor).
In our nav menu, we need to add an a tag to our li elements:

    <li><a href="home.html" >Home |</a> </li>

The most important attribute of the `<a>` element is the href attribute, which indicates the link's destination.
Your link's destination is the name and the extension to which you gave your other pages. Be careful to type it right.
If the page to which you are going to link is not in the same root, you need to specify in which folder it can be
found.
For example, if I have the contact page in a contact folder I write:

    <li><a href="contact/contact.html"> Contact </a> </li>

Check in the browser and... Done!

By default the a tag is styled like this:
- An unvisited link is underlined and blue
- A visited link is underlined and purple
- An active link is underlined and red

You can change the style and the color by selecting the a tag.

**:hover**
To get the nice effect of changing the color of a link when the mouse moves over it, you need to use the :hover selector.

    a:hover {
        color: red;
    }
