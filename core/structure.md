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


## Html und Head Elemente

Zurück zu unserer Datei (hoffentlich programmiert ihr bereits nebenher mit!).
Nach dem Doctype beginnen wir das HTML Dokument, mit einem `html` Element:

    <html>
    </html>

Es umschliesst jedes weitere Element in unserem HTML Dokument. Kein Element darf
ausserhalb des Elements `html` stehen. Als nächstes trennen wir jedes Dokument
in zwei wichtige Teile: einen **head** und einen **body**. Stellvertretend für 
Dokumenten Kopf und Dokument Körper.

Der Kopf beinhaltet den Titel der Seite und Informationen **über** das Dokument.
Man nennt diese Informationen auf **meta** Informationen. Die meisten 
Meta-Informationen sind für den Benutzer nicht sichtbar und haben dennoch 
eine Menge Sinn. Zum Beispiel können Meta-Informationen den Suchmaschinen 
mitteilen, wer der Autor einer Website und was in etwa der Inhalt der Seite 
ist. Hier ist ein Beispiel:

    <head>
        <meta charset="UTF-8"> 
        <meta name="description" content="Free Web tutorials">
        <title>My first Portfolio</title>
    </head>

Wie du siehst, ist das Meta-Tag ein selbst schliessendes Element! Als erstes
steht dort ein `charset` Meta-Tag. Das ist das wichtigste Meta-Tag. Ohne dieses
könnte es sein, dass deine Website nicht korrekt angezeigt wird. Es wird als 
empfohlene Vorgehensweise angesehen, dass es als erstes Folge-Element des 
`head` Elements eingesetzt wird. Es spezifiziert den Zeichensatz deines 
HTML Dokuments. Das bedeutet, dass der Browser in der Lage sein wird, 
Sonderzeichen wie ä, ö, ü, €, è und so weiter, auch auf Systemen anderer
Sprache korrekt anzuzeigen. `UTF-8` ist üblicher Weise das gängigste Zeichensatz
Encoding, dass im Web eingesetzt wird.

Hier haben wir ausserdem ein weiteres Meta-Tag genutzt: die `description` 
(Beschreibung). Wir definieren dieses Meta-Tag mit dem Attribut `name` und
setzen `description` als Wert zwischen die doppelten Anführungszeichen.

Innerhalb unseres `head` Elements, haben wir als letztes Element den Titel
unserer Website. Schreibe den oberen HTML code aus dem Beispiel in dein eigenes
HTML Dokument im Editor. Dann änder den Inhalt zwischen dem `<title>` Element.
Jetzt kannst du dein Dokument im Browser öffnen und schau dir mal an, was im Titel
des Browserfensters steht. Das ist ebenfalls der Titel, der genutzt wird, wenn
du eine Website als Bookmark hinzufügst.

Tags im `head` Bereich, können ebenfalls externe Resourcen wie CSS oder JavaScript
Dateien beinhalten. Wir werden uns damit später noch beschäftigen.

## Der HTML Body

Endlich kommen wir an die Stelle wo unser Inhalt hinkommt.
Der `body` beinhaltet den eigentlichen Inhalt einer Seite. Alles innerhalb der 
öffnenden und schließenden `body` Tags, ist für den Besucher der Website sichtbar.

Direkt nach dem schließendem `head` Tag aber noch innerhalb des `html` Elements,
fügen wir die `body` Tags hinzu:

    <body>
    </body>

Alles innerhalb des `body` Tags, wird dem Besucher angezeigt werden.
Schreibe etwas einfachen Text zwischen die `body` Tags und schau dir das Ergebnis
im Browser an.

**TIP**: Benutze die "Seite aktualisieren" Funktion (STRG+R oder F5) um das 
gleiche HTML Dokument im Browser neu zu laden.

## Inhalts Typen

Es gibt verschiedene HTML Elemente, die wir einsetzen können, um unterschiedliche
Inhaltes-Typen anzugeben. Beispielsweise das `p` Tag, dass wir bereits kennen 
gelernt haben. Versuchen wir zunächst eine Überschrift, gefolgt von einem 
Paragraphen:

    <body>
        <h1>I'm the title.</h1>
        <p>And I'm a paragraph!</p>
    </body>

Überschrift Elemente sind ziemlich einfach zu verstehen. Sie beginnen mit `h1` 
stellvertretend für die größte Schrift und wichtigkeit, bis hin zu `h6` mit der 
kleinsten Schrift.

## Einrückung

Wunderst du dich, warum wir die `h1` und `p` Tags innerhalb des `body` 
Tags *eingerückt* haben?

Das wird in keinster Weise die Interpretation und Darstellung durch den Browser 
beeinflussen, aber es gilt als guter Stiel unter Programmierern, dass man Code
so formatiert. Damit soll gewährleistet bleiben, dass ein Dokument sauber 
strukturiert und verständlich bleibt. Selbst wenn die Anzahl Code-Zeilen wächst oder 
man lange nichts mehr an dem Dokument gemacht hat. Ausserdem unterstreicht diese
Art der Formatierung sehr gut, die hierachische Natur von HTML.

## Kommentare

Es ist ausserdem möglich "Kommentare" in dein HTML zu setzen. Kommentare in HTML
sind dazu da, dich oder andere Leute an bestimmte Dinge zu hinzuweisen, ohne die 
Darstellung deiner Website im Browser zu verändern.

Wie andere HTML Elements, werden auch Kommentare als ein Tag geschrieben. Mit 
dem einzigen Unterschied, dass ein Kommentar ein wenig anders aussieht:

    <!-- I am a comment -->

Das "Kommentar Start" Tag ist `<!--` und das "Kommentar Ende" Tag ist `-->`.

Kommentare können andere HTML Elemente umschließen, um sie 
"aus zu kommentieren". Das ist eine nützliche Vorgehensweise, wenn du mit einer
Website herum experimentieren möchtest, um zu sehen wie sich Dinge im Browser 
verändern werden.

Versuch zum Beispiel mal die Überschrift `h1`, im `body` Teil des HTML Dokuments,
aus zu kommentieren.

    <body>
        <!-- <h1>I'm the title.</h1> -->
        <p>And I'm a paragraph!</p>
    </body>

Wenn du die Seite im Browser neu lädst, wirst du feststelle, dass die Überschrift
verschwunden ist.

Entferne die Kommentar-Tags (damit die Überschrift wieder erscheint) bevor du
zur nächsten Sektion über gehst.

## Bilder

Überschriften und Paragraphen geben dir die Grundlegenden Textformatierungs 
Elemente. Doch was ist mit Bildern?

Bilder werden in separaten Bild-Dateien, ausserhalb des HTML Dokuments 
gespeichert. Suche dir ein Lieblings-Bild aus dem Web und speicher es in das 
gleiche Verzeichnis, wo auch deine HTML Datei bereits liegt. Klicke dazu mit der
Rechten Maustaste auf das entsprechende Bild und wähle "Bild speichern" 
(oder ähnlich) aus dem Menü.

Falls dir spontan kein Bild einfällt, dann 
[ist hier eine Website mit Fotos von Katzen](http://www.flickr.com/photos/nengard/67501122/sizes/s/), die du nutzen kannst. ()
(Süße Katzen im Internet? Bei Gott!)

Nachdem du dir ein Bild ausgesucht hast, kannst du es in dein HTML Dokument 
einbauen, indem du das `img` Tag nutzt.

    <img src="kittens.jpg">

Füge das `img` Tag irgendwo innerhalb des `body` Tags hinzu. Am besten dort, wo 
du es gerne anzeigen lassen würdest. Ersetze "kittens.jpg" mit dem Dateinamen
des Bilds, dass du in das gleiche Verzeichnis wie dein HTML Dokument gespeichert
hast.

Beachte bitte, dass `img` Tag ist eines der Tags, die kein separates, 
schliessendes Tag benötigen. Du kannst zwar ein schliessendes "</img>" Tag direkt 
nach dem öffnendem "<img>" Tag setzen, jedoch wird das nichts daran ändern, wie
der Browser die Website anzeigen wird.

**TIP:** Die Bildquelle ("src") von `kittens.jpg` ist ein Pfad, relativ zur
HTML Datei. In diesem Fall befindet sich `kittens.jpg` im selben Verzeichnis.
Du könntest ebenso ein Bildquelle wie `images/kittens.jpg` nutzen, solange du
das Bild in ein Unterverzeichnis namens "images" legst. Du kannst sogar komplette
URLs wie `http://myawesomesite.com/pictures/kittens.jpg` nutzen, aber es ist 
(wenn möglich) besser sowas zu gunsten eines relativen Pfads zu vermeiden.

### Alternativer Text 

Es ist eine gute Angewohnheit, sogenannten "alt text" zur textuellen 
Beschreibung des Bild-Inhalts zu nutzen.

    <img src="kittens.jpg" alt="Some kittens">

Das ist wichtig für jeden Besucher, der keine Bilder sehen kann. Zum Beispiel 
sehbehinderte Menschen, die einen Screenreader nutzen (auch Braile-Zeile genannt).
Jedes Bild, dass nicht aus dekorativen Gründen im HTML eingebettet wird, sollte
eine Bild-Beschreibung über das "alt=" Attribut bekommen.

## Nochmal alles zusammen

Bis hierhin sollte unser gesamtes HTML Dokument in etwa wie folgt aussehen:

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


Bitte beachte, dass das Katzen-Bild hier in einem eigenen Paragraphen steht,
so dass es im Browser in einer eigenen neuen Zeile dargestellt wird.

Hoffentlich schaut das Dokument in deiner Datei vergleichbar aber nicht
identisch aus. Vermutlich unterscheiden sich einige der Texte. Funktioniert 
alles in deinem Browser?

## Warum sollte man kein Word nutzen?

Du magst dich wundern, warum wir alle diese Elemente händisch schreiben,
wenn wir genauso gut Programme wie Word dafür nutzen könnten.

Nunja, denke mal an die coolen Websites im Internet und die komplexen Layouts,
die sie haben. Denkst du, du kannst diese mit einem Programm wie Word nachbauen?
Wie lang würde das wohl dauern? Das ist nur durch die manuelle Kontrolle von
HTML (und CSS und JavaScript) möglich, die Entwicklern durch Webtechnologie 
in die Hände gelegt wird. Das kannst *du* auch lernen!

## Wie geht es weiter?

Du magst deine deine HTML Seite in diesem Stadium etwas farblos und fade finden.
Wie kann man sie ein bisschen mehr aufpeppen?

Lese in der folgenden Sektion weiter, 
[your first styled Hello World!](style.html).
