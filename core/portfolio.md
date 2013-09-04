---

layout: ots
title: Create your personal Portfolio

---

# Html5 structure and Css starter
## Main Content

We will start building the main page, our personal presentation since is the one that will give the 
main structure to the whole web site design.


**GOAL**
We are going to design a page with the main menu, the content and footer.
We fill in the content with an image next to some text.
We are going to do all of this with the Html5 elements so keep open your Html cheatsheet.

Taken file like the one we just wrote but without any content. (Head with meta-tag, title and 
style.css linked and body but comletely empty.)

Let's start wrapping all our page in a div for give a centered design to our page.
 *"Div tag defines a section in an Html file and is used to group element to format 
 them with Css, to layout a web page."*

Div is a general tag and can be used in many different situation just to wrap up others html
elements and style them. For this reason we need to give to it a name, otherwise we can't style each one 
in different way.
There are two way to give a name to a div tag. With a id or with a class.
Think about at id as a pesonal and UNIC name as your surname/name and about the class is like personal 
characteristics as color of your hares or your age. 
Id, the unique one, is used just when need to write specific style valid only for this element. 
Class are more common and used for group different Html elements and give them the same style and characteristics.

We can now start to write our main page content:

	<div class="wrap-centered">
	</div>

Here we use class since we are giving quite general style. Until now we use it just for this div
but maybe in future we can use again.

In style.css we make this div always centered in the middle. 
In css for call the class we need to write "." and the class name just after it. 
For the Id is the same but with "#" instead if "."

	.wrap-centered {
		width: 100%;
		margin: 0 auto;
	}

Defined the width of an element and than give to it "margin: 0 auto" is a common rules for make
the element centered.
We use 100% instead of 100px for the easily fact that we wont our page responsive or in other worlds we want 
that the page resize when the browser windows change dimensions.
Now everything will stay inside this div will be centered.

In the css style, at the beginning of the file let's write also somehting like that:

	* { padding: 0; margin: 0; border: 0; }

That's set all the elements "\*", with default padding, margin and border equal to 0px. 
This is really important to do because everybrowser set a default size for some tags and without 
set all of them again to 0px will be impossible to calculate the  position of Html elements and to
positioning them in the space, since every browser will interpeter that in a different way.	

## Menu
Time to write our menu.
Inside of the div we are going to write our first Html5 element.

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

In style.css:

	nav {
		width: 100%;
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

That's tell to the selector selected to get out from the normal flow of the Html element (usually Html element are block element, that's mean that they are displayed one after the other vertically in the page as a block.) and move to the most 
right side of the div where is wrap up.

If you check in your browser, the nav ul is displayed on the right. 
Float can be set on the right or on the left. Always be carefull with that because this will change the flow of all the html
elements, not just the one that you are going to modify.

We just said that usually the Html element are like a block displayed in a vertical flow. And we can change this flow 
thanks to float property. Another propery that allow us to change the flow is display: inline. 
Actually thsi property don't change the flow, rather make an element inline (so will stay on one line instead folling down) 
instead as a block.
Check your menu navigation.

/////// Positioning: relative? (lo spiego dopo e ora dico solo che c'è sempre da metterlo cn flow?)+

//// check everything in a browser. Wrap 100%, nav ul font-decoration? float without positioning? 



