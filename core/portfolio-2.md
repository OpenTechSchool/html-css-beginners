---

layout: ots
title: Create your personal Portfolio

---

So far we already build the core of our website. Now we need an home page and a contact page.
Here we explain still some basic concept but after that you have more freedom to do and experiemnt
new stuff.

# Home page and positioning
Let's start from the hoem page.

**Goal**

The page is made by: 
- navigation menu
- big centered and resizible image
- two sentence intro text (on the top of the image)

So let's open a new file and set the basic structure. 
For make the nav menu we can just copy what we have done in the first part.
Than take an image that you like. Should be big enough and with good resolution.

Just after the nav tag, include your image and give to it a class name.
Now you need to set the width of just this image as 100%.	

	.home-imag {
		width: 100%
	}

In this way your image will follow the size of the windows browser.
Is possible that when the window is very small or very big you can see a white space at the bottom of the image.
You can change it setting also hight: 100%. But now you need to be sure that you image isn't stretched.

After the image, write another header tag within h1 and h2, add a class name to your header so you can style 
and not be confused with the other one. (I will use header-home as class name)
In the CSS we are goint to write that:

	.header-home {
		position: relative;
		top: -300px;
	}
Here we are changing the position of this element, and bring it outside of the normal flow. His position is 
now relative to his parent element (in our case the div#wrap-centered). Now you can move your element where
you prefer in the page using the properties top, right, bottom and left.

So, what is a positioning?
When a box is taken out of normal flow, all content that is still within normal flow will ignore it 
completely and not make space for it Elements can be positioned using the top, bottom, left, and right 
properties. However, these properties will not work unless the position property is set first. They also work
differently depending on the positioning method.

There are four different positioning methods.

**Static positioning**
A statically positioned box is one that is in normal flow, from top to down

**Fixed Positioning**
An element with fixed position is positioned relative to the browser window.
What make it possible is: position: fixed. 
than you can play changing the position, add a different pixel value to top, bottom, left or right positioning

**Relative Positioning**
A relative positioned element is positioned relative to its normal position. Elements that come after a relatively-positioned element behave as if the relatively-positioned element was still in its ‘normal flow’ position - leaving a gap for it
What make it possible is: position: relative. 
than you can play changing the position, add a different pixel value to top, bottom, left or right positioning

**Absolute Positioning**

An absolute positioned box is moved out of the normal flow entirely
What make it possible is: position: absolute. 
than you can play changing the position, add a different pixel value to top, bottom, left or right positioning

**Overlapping Elements: z-index property**

When elements are positioned outside the normal flow, they can overlap other elements. The z-index property specifies the stack order of an element (which element should be placed in front of, or behind, the others).
What make it possible is: z-index: n°pixel. 

Nowing that, create your own home page!

# Form elements
Time to create the contact page!

**Goal**

Create a page with:
- navigation menu
- contact form as main content
- footer

Contact form is made by Name, surname, gender, age, email, comment field, agree button and send button.

Has we already did before let's open a new page, copy all the structure and the nav menu and the footer from
part 1.

(FORM ELEMENTS)

# a tag

Good! Our portfolio is almost ready.
Now we need just one thing to do. Link all your pages togheter.
For do that there is a special tag. a tag (anchor).
Taking nav menu, we need to had a tag to our li elements:

	<li><a href="home.HTML" >Home |</a> </li>

The most important attribute of the < a > element is the href attribute, which indicates the link’s destination.
link's destination is the name and the extencion which you gave to your other pages. Be careful to type it right.
If the page that you are going to link is not in the same root, you need to specify in which folder it can be
found.
For example if i have the contact page in a contact folder i write:

	<li><a href="contact/contact.HTML"> Contact </a> </li>

Check in the browser and... Done!

By default the a tag is styled like this:
- An unvisited link is underlined and blue
- A visited link is underlined and purple
- An active link is underlined and red

You can change the style and the color selecting the a tag.

** :hover**
For getting the nice effect when the mouse move over a link and it change color you need to use the :hover selector.

	a:hover {
		color: red;
	}

	


