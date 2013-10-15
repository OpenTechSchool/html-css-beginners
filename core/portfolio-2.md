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

## Form elements
Time to create the contact page!

**Goal**

Create a page with:

* navigation menu
* contact form as main content
* footer

Your contact form will have the following fields: name, surname, gender, age, email, comment field, agree button and send button.

As we already did before, let's open a new page, copy all the structure, the nav menu, and the footer from
part 1.

(FORM ELEMENTS)

## a tag

Good! Our portfolio is almost ready.
Now we need just one more thing: to link all your pages together.
To do that there is a special tag: a tag (anchor) that defines a hyperlink.
The most important attribute of the < a > element is the href attribute, which indicates the link’s destination.
So the HTML syntrax for a link look like this: 

    <a href="yourUrl">Link text</a>

There are different types of links.
You can create an **external link**, a link that go to another web site. This
link is absolute and basically need all the line that usually you see or type
in the Url bar of your browser.
If we want to link our web site to the OTS site, it look like this:

     <a href="http://opentechschool.org">OpenTechSchool</a>

Also very important is the Internal link or rather a link that point on your
own web site, point just to another page of the same website.
And that one is also the one we need right now, so let's proceed with our
portfolio. 
In our nav menu, we need to add an a tag to our li elements:

    <li><a href="home.html" >Home |</a> </li>


Be careful to type the url right.
If the page to which you are going to link is not in the same root, in the same folder of your file, you need to specify in which one it can be
found.
For example, if I have the contact page in a contact folder I write:

    <li><a href="contact/contact.html"> Contact </a> </li>

Check in the browser and... Done!
Now you can do the same for the rest of your nav menu and for your social buttons links.

By default the a tag is styled like this:

* An unvisited link is underlined and blue
* A visited link is underlined and purple
* An active link is underlined and red

You can change the style and the color by selecting the a tag.

There still at least one important link to explain. The mailto link.
Write mailto: myemail@google.com tell to the browser to open the default
email programm on the user machine with the email destinatary field already fill in. Nice, isn't it?
So go ahead and write the mailto link with your personal email instead of # 
in your contact list and try it out.

**:hover**
To get the nice effect of changing the color of a link when the mouse moves over it, you need to use the :hover selector.

    a:hover {
        color: red;
    }


Great! We are done but if you still have a time keep going to play with your potrfolio, make it nicer, change colors, fonts, add images or whatever you like most and be ready for present it at the end of the workshop.
We want to see your amazing personal website!

Don't hesitated to ask to our coaches if you have any question.

