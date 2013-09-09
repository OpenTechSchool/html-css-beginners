---

layout: ots
title: Create your personal Portfolio

---

# HTML5 structure and CSS starter
## Main Content

We will start building the main page, our personal presentation since is the one that will give the 
main structure to the whole web site design.


**GOAL**
We are going to design a page with the main menu, the content and footer.
We fill in the content with an image next to some text.
We are going to do all of this with the HTML5 elements so keep open your HTML cheatsheet.

Taken file like the one we just wrote but without any content. (Head with meta-tag, title and 
style.CSS linked and body but comletely empty.)

Let's start wrapping all our page in a div for give a centered design to our page.
 *"Div tag defines a section in an HTML file and is used to group element to format 
 them with CSS, to layout a web page."*

Div is a general tag and can be used in many different situation just to wrap up others HTML
elements and style them. For this reason we need to give to it a name, otherwise we can't style each one 
in different way.
There are two way to give a name to a div tag. With a id or with a class.
Think about at id as a pesonal and UNIC name as your surname/name and about the class is like personal 
characteristics as color of your hares or your age. 
Id, the unique one, is used just when need to write specific style valid only for this element. 
Class are more common and used for group different HTML elements and give them the same style and characteristics.

We can now start to write our main page content:

	<div id="wrap-centered">
	</div>

Since we have just one main content we can use id selector.

In style.CSS we make this div always centered in the middle. 
In CSS for call the class we need to write "." and the class name just after it. 
For the Id is the same but with " # " instead if "."

	.wrap-centered {
		width: 100%;
		margin: 0 auto;
	}

Defined the width of an element and than give to it "margin: 0 auto" is a common rules for make
the element centered.
We use 100% instead of 100px for the easily fact that we wont our page responsive or in other worlds we want 
that the page resize when the browser windows change dimensions.
Now everything will stay inside this div will be centered.

In the CSS style, at the beginning of the file let's write also somehting like that:

	* { padding: 0; margin: 0; border: 0; }

<<<<<<< Updated upstream
That's set all the elements "\*", with default padding, margin and border equal to 0px. 
=======
That's set all the elements " * ", with default padding, margin and border equal to 0px. 
>>>>>>> Stashed changes
This is really important to do because everybrowser set a default size for some tags and without 
set all of them again to 0px will be impossible to calculate the  position of HTML elements and to
positioning them in the space, since every browser will interpeter that in a different way.	

## Menu
Time to write our menu.
Inside of the div we are going to write our first HTML5 element.

	<nav>
		<ul>
			<li>Home |</li>
			<li>Contact</li>
		</ul>
	</nav>

Here we have 3 new elements. First the nav tag. That's tag mean navigation and wrap up all the elements
that are essential for the navigation in the website.
Ul is a type of list, unordered. In th list, has the world suggest, we keep elements that usually stay in 
a list and each element are wrap up in a li tag.

In style.CSS:

	nav {
		width: 100%;
		margin-top: 20px;
	}

	nav ul {
		font-decoration: none;
		float: right;
		margin-right: 20px;
	}

	nav li {
		display: inline;
		font-decoration: none;
		color: ##08c;
	}

Nav ul is a way to specify that i'm talking about not all the ul in the page but just the one that is nav's child.
Most of the property we write here you already know or you can eaily check on the cheatsheet. 
We want to talk about one of them, really particular and with big power: float: right.

That's tell to the selector selected to get out from the normal flow of the HTML element (usually HTML element are block element, that's mean that they are displayed one after the other vertically in the page as a block.) and move to the most 
right side of the div where is wrap up.

If you check in your browser, the nav ul is displayed on the right. 
Float can be set on the right or on the left. Always be carefull with that because this will change the flow of all the HTML
elements, not just the one that you are going to modify.

We just said that usually the HTML element are like a block displayed in a vertical flow. And we can change this flow 
thanks to float property. Another propery that allow us to change the flow is display: inline. 
Actually thsi property don't change the flow, rather make an element inline (so will stay on one line instead folling down) 
instead as a block.
Check your menu navigation.

Last thing we need to do before move on is to clear everything in order to restore the normal flow, since we 
change it setting float to right.

	<div class="clear"></div>

And in the CSS file:

	.clear {
		clear: both;
	}	

Here we create a new div with class clear and call this one in CSS giving clear both. That will clear both value, right
and left. Other two possible values are "right" or "left". 
When you mess up with floatting element, before starting a new design section is always a good practice put "clear:both"
to be sure your flow is still the default one.

## The footer

Footer is called, as the name say, that part of the page that stay at the end of the page and give some general and 
maybe secondary information, like in a book.
The interested tag is:

	<footer>
		<p></p>
	</footer>

Inside the p tag you can write what you prefer. Maybe who made this website or your email.
In CSS file:

	footer {
	margin-top: 50px;
	}

	footer p {
		text-align: center;
	}

We don't really need to style the footer but is nice to give to it a space to breath with a margin-top: 50px. 
Than we just set the alignament of the text in the p tag as center.
That's all what we need for the footer.

## Box Model and fonts

Finally we start to build our content. First of all some structure. We said we are going to design two coloum
design, one coloum is a kind of sidebar and this tag is called aside and the other one, the most important one,
is a section wrapping up several articles.
In order to have more control on this two-coloum design, contain all of it in a div.content and give to it some
basic CSS, as we already did it for the wrap div.

tips: When you are not sure if your CSS is working in the properly way and you want to check exactly the size,
margins or else of your element, give to it a casual background-color, so it display the element is all it's size.

	<div class="content">
		<aside>
		</aside>
		<section>
		</section>
	</div>

In style.CSS:

	.content {
	width: 70%;
	margin:0 auto;
	}

	aside {
		width: 35%;
		margin: 20px;
		border-right: 1px solid #000;
		min-height: 300px;
		float: left;
	}

	section {
		width: 55%;
		display: inline-block;
		padding: 10px;
		margin: 20px 10px;
	}

First we gave a size to the content and place it in the middle of the page. Than we place the aside tag with some
margins to breath, a minimum height and a width. We also highi-light the border-right of this element so it display
a line that divide aside from section.
Last we give a float: left in order to make the section (or whatever we will write after the aside) slip next to the
aside, right on its left.
Is really important to set display: inline-block for the section

In the aside let's place an image, our personal profile image.

	<aside>
		<img src="me.jpg"/>
	</aside>

	img {
		width: 272px;
		margin-top: 10px;
	}

When you don't know the size of your image, you can place it and than open your console and check from there,
try to write different width size and see what the best one. 
Of course the best way to do this work is cut your image before, kwoning the size, with some Graphical Programs
like Photoshop or gimp but for now that is enough.

Time to write your personal presentation!

	<section>
		<article>
			<header>
				<h1>Title</h1>
				<h2>Second title</h2>
				<p>Hello hello hello</p>
			</header>
		</article>	
	</section>

Here we contain inside the section an article tag. Each article tag is compose from header tag, a tag that is 
made for wrap up all the h tags. So we place inside of it an h1 and h2 tag. Followed from a p tag where finally
all our content is written. Write at least some text inside your article, we will need later on.


Before make our article looking better, we need to know some basic knowledge about Box model.
What is a box model and why is so importan?

Every element in web design is a rectangular box. (Yes, either block and inline element. You can set padding,
margins and border on both of them.) 
In CSS, the term "box model" is used when talking about design and layout.
The CSS box model is essentially a box that wraps around HTML elements, and it consists of: margins, borders, 
padding, and the actual content.
The box model allows us to place a border around elements and margins and padding around this element too.
How is the size of the box calculated exactly? Here is a diagram:

<img src="../images/CSS-box-model.gif" />

What these elements do?
* Margin: Clears an area around the border. The margin does not have a background color, it is completely transparent
* Borders: A border that goes around the padding and content. The border can have a personal color and thickness
* Padding: Clears an area around the content. The padding is affected by the background color of the box
* Content: The content of the box, where text and images, text or others elements appear

Margin is the unique that doesn't affect the size of the box itself, but it affects other boxes in the page.
The size of the box itself is calculated like this:

**Width:** width + padding-left + padding-right + border-left + border-right

**Height:** height + padding-top + padding-bottom + border-top + border-bottom

Tips: Remember to set all of this elemnents to "0px" when you start your .CSS files as we did at the very beginning.

So, now that we know how to calculate the box around our elements, let's play with it around the article, 
header and h tags.

**Text style**

The text in the document are still pretty boring, let's style it.
What we already know so far is how to change a color and how to make the text align on the center.
As you probably already understood, the others values of text-align are left, right and justified, 
by default the value is left.
When text-align is set to "justify", each line is stretched so that every line has equal width, and the left and right margins are straight (like in magazines and newspapers).
An important decision to take is which font we are going to use for the project?
You can specify the type of font whit the font-family property.

There are two types of font family names:
generic family: a group of font families with a similar look (like "Serif" or "Monospace")
font family: a specific font family (like "Times New Roman" or "Arial") 
For choose your font you have to way. 
Once is use a common family-font (one that with high probablity all of the user have on their machine.) called a
"web-safe" fonts. Or use a font-face rule. That's a new property that allow a designer to include font-family on
your server and refered to it. 
The second one it was a small revolution since gave to the designer the freedom to choose the font they more prefer
and now we have a huge choose.

By the way now we are going to use the "web-safe" font since is easier and fast. 
Tips: If you try to use a particular font that you download in your computer and it display correctly be carefull
because on the computer of users probably don't. The correct display doesn't dipends from the browser but from 
what's in your machine.

	h1, h2 {
		font-family: Georgia, serif;
	}	

	p {
		font-family: "Trebuchet MS", Helvetica, sans-serif;
		font-size: 0.9em;
	}

And here we can already see the other really important property. Font-size. As you already understood that's set 
the size font of your selector. Browser have a font-size set by default but is important for a good look change these.
However, you should not use font size adjustments to make paragraphs look like headings, or headings look like paragraphs.
The font-size can be set using px, em or %.
Your screen resolution specifies how many pixels your screen/display is made of. So when you specify: font-size: 
12px;, you're basically telling the browser that each letter should be 12 pixels high. That's is therefore
connected with your screen size.
Font-size: 50%; sets the font size of your element to 50% of the font size of its parent element and em is the 
width of the letter 'm' in the selected typeface, basically the same as percentage, except that 1em is 100% 
and 1.5em is 150%.
The size calculated from pixels to em using this formula: pixels/16=em.
For examples:

	h1 {font-size:2.5em;} /* 40px/16=2.5em */

Fact is, it's hard to tell you what you have to do with them because is hard to tell what you are to achieve 
in each of your layouts. Layouts are about creativity, and you can't just fix an approach to fit all of them.
For now we can say that is better to use em for a font in these days since the user has so many different 
device and screen size that this is the easier way to make the font-size automatical resizeble.

A good solution can be also setting a font-size: 100% in the body element and than use em for each different 
selector so you start in every browser with the same size.

Ok now is time for you to play, modify and create your font style.
If you want to try something more you also check your cheatsheet and discover other font- text- property.



