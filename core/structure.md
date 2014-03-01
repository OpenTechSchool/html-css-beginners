---

layout: ots
title: Die Template Struktur

---

## Preamble: Wie man ein HTML Dokument schreibt

Das ist eignetlich recht einfach: HTML wird als eine einfache Text Datei 
geschrieben. Eine HTML Datei nutzt immer die Dateierweiterung **.html** um die 
Art der Datei anzuzeigen.

## Text editor
You will need a plain text editor in order to edit HTML files.

## Text Editor
Um HTML Dateien zu editieren, wirst du einen reinen Texteditor benötigen.

Du kannst ausserdem komplett grafische WYSIWYG 
(What You See Is What You Get) HTML Editoren finden, die dich eine Webpage 
grafisch editieren lassen. Vergleichbar mit einer Oberfläche wie von Word.

Das kann nuetzlich sein, aber viele Leute, die mit HTML & CSS arbeiten, 
bevorzugen einen reinen Text Editor. Genau so einen nutzen wir heute.

Wenn du bereits einen Texteditor installiert hast (vielleicht von einem vorherigen
OTS Workshop) dann kannst du diesen nutzen. Andernfalls sind hier einige Vorschläge:

### Windows

[Notepad++](http://www.notepad-plus-plus.org/) ist kostenlos und nützlich. 
Du kannst aber auch [Sublime Text](http://www.sublimetext.com/) ausprobieren.


### OS X

[TextWrangler](http://www.barebones.com/products/textwrangler/) ist kostenlos und 
nützlich. Weitere gute Optionen (mit einigen fortgeschrittenen Funktionen,
in die du hineinwachsen kannst) sind [Sublime Text](http://www.sublimetext.com/) or 
[Text Mate](http://macromates.com/).

### Linux

GEdit ist auf den meisten Linux Distributionen vorinstalliert. 
Andernfalls kannst du es auch mit [Sublime Text](http://www.sublimetext.com/) 
oder einem der zahlreichen anderen Linux Text Editoren versuchen.

********

**Text Editor installiert und geöffnet? Gtossartig! Zeit für das erste HTML Dokument!**

## Doctype

Das erste Element einer HTML Seite ist der **doctype**, welcher wie du dir 
vielleicht denken kannst, dem Browser den Typ des Dokuments anzeigt. 
Das ist wichtig damit der browser weiss wie er das HTML Dokument anzeigen und lesen soll.

Gluecklicher Weise ist der HTML5 Doctype extrem simpel - er ist einfach `html`.

Oeffne eine neue Datei in mit deinem Text Editor und schreibe dies in die erste 
Zeile:

    <!DOCTYPE html>

Dann speicher die Text-Datei mit der Datei-Erweiterung `.html`. Du editierst nun
ganz offiziell ein HTML Dokument.

## Strukturiere dein Projekt

Du kannst überall wo du willst HTML dateien anlegen. Jedoch empfehlen wir dir,
dass du verzeichnisse nutzt um deine Dateien zu organisieren. So sind sie später
einfacher wieder zu finden.

* Erstelle an beliebiger Stelle eine Verzeichnis für diesen Workshop. Zum 
  Beispiel auf dem Desktop oder in deinem Benutzer-Verzeichnis. 
  Nenne das Verzeichnis *OTS_HTML_Workshop* oder ähnlich.

* Erstelle ein Verzeichnis innerhalb des deines Workshop Verzeichnis. 
  Nenne es **exercise1** oder ähnlich.

* Vom Text-Editor aus, speichere dein erstes HTML Dokument in 
  dem *exercise1* Verzeichnis. Nenne die HTML Datei *page.html* oder ähnlich.

Mit der Zeit werden wir noch weitere Dateien zu diesem Verzeichnis hinzufügen.
Vielleicht sogar ganz neue Verzeichnisse, parallel zu exercise1 anlegen.

## Elemente und Tags

Das sind die grundlegenden Bausteine von HTML.

**Elemente** *sind das*, was ein HTML Dokument ausmacht. Weil man keine, 
eines oder mehr Elemente ineinander schachteln kann, entsteht eine 
*hierachische* Struktur im HTML Dokument. Ein Element kann drei 
Dinge beinhalten: ein Tag, ein Attribut und Inhalt.

Ein **Tag** ist etwas, dass den Nutzen eines Elements angibt. Das `<p>` Tag zum
Beispiel gibt an, dass es sich, bei dem Element um einen 
Paragraphen-Text handelt. Das `<li>` Tag gibt an, dass hier ein Listen-Eintrag 
stehen soll. Du wirst bereits festgestellt haben, dass Tags immer von spitzen
Klammern eingefasst sind. **Öffnende** und **schliessende** tags markiegen den
Anfang und das Ende eines Elements. Ausserdem umschliessen sie dessen Inhalt:

    <p>This is a paragraph.</p>

Wie du siehst, beinhaltet das schließende Tag ein `/` vor dem Namen. Andernfalls
wäre es ein weiteres öffnendes Tag!

Prüfe bitte **immer** doppelt, dass du alle deine öffnenden Elemente wieder 
geschlossen hast. Andernfalls wird der Browser, beim anzeigen deines 
HTML Dokuments, seltsame Dinge machen.

Es gibt eine Hand voll spezieller Elemente, die eine Auznahme zur Regel 
darstellen. Wenn Elemente nichts anderes als den Tag-Namen beinhalten können, 
brauchen sie auch nicht geschlossen werden. Zum Beispiel die folgenden Elemente 
sind sogenannte 'selbst schliessende' Elemente:

    <hr>
    <input>
    <img>

Es gibt nicht viele dieser Elemente und du wirst schnell heraus finden, welche
Elemente selbst schliessend sind, indem du ein wenig mehr Code schreibst. :)

Zu guter letzt, Elemente **verschachteln**. Das ist gar nicht so schwer, aber 
fundamental für die Funktionsweise von HTML. Verschachteln sieht wie folgt aus:

    <p>This is a sentence, with a <span>span</span> element inside it.</p>

oder so:

    <div id="first-heading">
        <h1>The h1 tags indicates the primary header of the document</h1>
    </div>

Du wirst festgestellt haben, dass HTML sich um Leerzeichen oder Zeilenumbrüche 
**zwischen** Tags nicht kümmert. Wenn das obige Beispiel in eine einzige Zeile 
zusammen gerückt würde, käme im Browser das gleiche Ergebnis heraus.

Im Beispiel, findest du zum ersten mal ein **attribut**. Ein Attribut beginnt 
mit einem Namen in Kleinbuchstaben und wird dann nahezu immer 
mit `=` und einem 'Wert' weiter geführt. Der Wert ist von doppelten 
Anführungszeichen umschlossen. In etwa wie `"das hier"`. Ein Element kann viele
Attribute haben. In so einem Fall werden die Attribute mit einem Leerzeichen von
einander getrennt. Dazu gleich mehr. Attribute geben bestimmte Informationen über
Elemente.

In diesem Fall, hat das `<div>` Tag, welches genutzt wird um Elemente 
zu gruppieren, ein `id` Attribut mit dem Wert `first-heading`. Das sagt uns, 
dass diese Sektion des HTML Dokuments bestimmt wurde, um die erste Überschrift
der Website zu beinhalten. Du wirst später mehr über spezielle Attribute lernen.


## Html and Head Elements

Coming back to our file (hope you're coding along!), after the doctype we 
begin our document with a root `html` element, just like so:

    <html>
    </html>

It encompasses every other element in our HTML document, nothing should go 
outside it! Next, the document is broken up into two important parts: 
The **head** and **body**.

The head contains the title of the page & information **about** the page 
(*meta* information). Most meta information isn't visible to the user, 
but it has many purposes. For example, meta elements can tell search engines 
information about your page, such as who created it and a description of 
your page's content. Here's an example `head` element:

    <head>
        <meta charset="UTF-8"> 
        <meta name="description" content="Free Web tutorials">
        <title>My first Portfolio</title>
    </head>

You can see meta tags are one of the self-closing elements! 
First off, there is a charset meta tag. 
This is the most important meta tag. Without it your website might not display 
properly. It is best practice to include it as the first element inside the 
head element. Basically, it specifies to the browser the character encoding 
for the HTML document. That means your browser will be able to read and 
correctly display all the special characters such as €, $, è and so on. `UTF-8` 
is usually the best general encoding to use.

Here we've also written another type of a meta tag, the description. 
We define what kind of meta tag it is with the `name` attribute and put our 
description in the *value* of the content attribute.

Inside our head element, we have lastly written a title of our website. Chuck 
the above code in your file (inside your `html` element), and change the 
content of the `<title>`. Then you can check your document by opening your 
file in a browser and looking at what is written in your browser toolbar. 
That also provides a title for the page when it is added to favorites.

Head tags can also include external files or resources, such as CSS or 
JavaScript files. We will see later how to do this.

## The Body

Finally, we are at the place where our content goes. 
The body contains the actual content of the page. Everything that is 
contained in the body is visible to the user.

Just after the closing head tag but still inside the html element, 
let's add the body tags.

    <body>
    </body>

Everything that is written inside this tag will be displayed to the user. 
Add a `<body>` to your existing HTML document and then write some 
plain text between the body tags and view it in your browser.

**TIP**: To reload the same HTML document in the browser, use the Reload 
Current Page function (Ctrl-R or F5)

## Types of content

There are different HTML elements that we can use to indicate different types 
of content in our document, like the <p></p> tags which we have already met.
Let's try writing a title, followed by a paragraph.

    <body>
        <h1>I'm the title.</h1>
        <p>And I'm a paragraph!</p>
    </body>

Heading elements are straightforward to understand. They start from h1 with the 
biggest font and importance, going to h6 with the smallest font.

## Indentation

Are you wondering why we wrote the h1 and p tags *indented* inside 
the body tags?

That will not change at all how the browser reads or interpretates the 
document, but it is a good practice among developers to write code like that 
in order to have a more clear document and still be able to work with it 
even after a long time or when there is a lot of lines of code. It also shows 
the heircharcical nature of HTML pretty well.

## Comments

It is also possible to put "comments" in your HTML. Comments in HTML are there 
to remind you (or other people editing the HTML file) without changing the way 
the page displays in a browser.

Like other HTML elements, comments are written by using a tag. Although comment 
tags look a little different:

    <!-- I am a comment -->

The "start comment" tag is `<!--` and the "end comment" tag is `-->`.

Comments can also enclose other HTML elements, to "comment them out". This is a 
useful technique when you're experimenting with a page to see how it looks when 
you change things around.

For example, try commenting out the `h1` heading in your current page:

    <body>
        <!-- <h1>I'm the title.</h1> -->
        <p>And I'm a paragraph!</p>
    </body>

If you reload the page in your browser, you'll notice the heading has vanished.

Remove the comment tags (so the heading appears again) before moving on to the 
next section.

## Images

Headings and paragraphs give you the basics of text. What about images?

Images have to kept in separate image files, outside the HTML file. Find a 
favourite image on the web and save it in the same directory as your HTML 
file (right-click the image in your browser and "Save Image...").

If you don't have a picture in mind then
[here's a page with a photo of some kittens that you can use](http://www.flickr.com/photos/nengard/67501122/sizes/s/)
(Cute cats on the internet? Egad!)

After you have your image, you can include it in your HTML page by using an 
`<img>` tag.

    <img src="kittens.jpg">

Add the `<img>` tag anywhere inside the "body" of your HTML document where 
you'd like the image to appear. Replace "kittens.jpg" with the file name 
of the image that you saved in the same directory as the HTML file.

Notice that `<img>` is one of the tags that doesn't need a sepaate closing 
tag. You could put `</img>` after the tag if you like, it doesn't change 
the way the browser views the page.

**TIP:** The image source name ("src") of `kittens.jpg` is a path relative 
to the HTML document. So in this case `kittens.jpg` is located in the same 
directory, but you could use a name like `"images/kittens.jpg"` if you 
put the image file into a subdirectory called "images". You can even 
use full URLs like  `"http://myawesomesite.com/pictures/kittens.jpg"`, 
but it's best to avoid this if you can use a relative path instead.

### Alt Text

A good habit to get into is using "alt text" to describe the contents of 
an image:

    <img src="kittens.jpg" alt="Some kittens">

The alt text is a textual description of what's in the image. This is important 
for anyone who can't see the images (for instance vision impaired people using 
a screenreader.) Any image that isn't purely decorative should have a description 
set with the "alt=" attribute.

## Putting it all together

So far, our entire document might look like this:

    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8"> 
            <meta name="description" content="Free Web tutorials">
            <title>My first Portfolio</title>
        </head>
        <body>
            <h1>I'm the title.</h1>
            <p>And I'm a paragraph!</p>
            <p>
                 <img src="kittens.jpg" alt="All the kittens are shown here">
            </p>
            <h3>This is a sub-heading...</h3>
            <p>Well now we're just blathering on.</p>
        </body>
    </html>


Notice that the kitten image is part of its own paragraph here, so it is
shown on a new line in the browser.

Hopefully the document in your file looks similar, but not exactly the same. 
You might have changed some of the text... does it all work in your browser?

## Why not use Word?

You might wonder why you're writing all these elements by hand, 
when you could make up the same stuff in a Word document.

Well, think about some of the cooler websites around that you've seen on the 
web, and their complex layouts. Do you think you could replicate them 
using Word? How long might it take? That's the power of manual control that 
HTML (and CSS, and Javascript) gives to the web and web developers. You can 
learn it too!

## What's next?

You may be thinking at this stage that your HTML page looks pretty bland. 
How can you spice it up a little?

Read on to find out in the next section, 
[your first styled Hello World!](style.html).
