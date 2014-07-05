---

layout: ots
title: Die Template-Struktur

---

## Präambel: Wie man ein HTML-Dokument schreibt

Das ist eigentlich recht einfach: HTML wird als eine einfache Textdatei
geschrieben. Eine HTML-Datei nutzt immer die Dateierweiterung **.html**, um die
Art der Datei anzuzeigen.

## Texteditor
Um HTML-Dateien zu editieren, wirst du einen reinen Texteditor benötigen.

Du kannst ausserdem komplett grafische WYSIWYG
(What You See Is What You Get) HTML-Editoren finden, die dich eine Website
grafisch editieren lassen. Dies ist vergleichbar mit einer Oberfläche wie von Word.

Solche Software kann nützlich sein, aber viele, die mit HTML & CSS arbeiten,
bevorzugen einen reinen Texteditor. Genau so einen nutzen wir heute.

Wenn du bereits einen Texteditor installiert hast (vielleicht von einem vorherigen
OTS-Workshop), dann kannst du diesen nutzen. Andernfalls sind hier einige Vorschläge:

### Windows

[Notepad++](http://www.notepad-plus-plus.org/) ist kostenlos und gut ausgestattet.
Du kannst aber auch [Sublime Text](http://www.sublimetext.com/) ausprobieren.


### OS X

[TextWrangler](http://www.barebones.com/products/textwrangler/) ist kostenlos und
gut ausgestattet. Weitere gute Optionen (mit einigen fortgeschrittenen Funktionen,
in die du hineinwachsen kannst) sind [Sublime Text](http://www.sublimetext.com/) or
[Text Mate](http://macromates.com/).

### Linux

GEdit ist auf den meisten Linux-Distributionen vorinstalliert.
Andernfalls kannst du es auch mit [Sublime Text](http://www.sublimetext.com/)
oder einem der zahlreichen anderen Linux-Texteditoren versuchen.

********

**Texteditor installiert und geöffnet? Grossartig! Zeit für das erste HTML-Dokument!**

## Doctype

Das erste Element einer HTML-Seite ist der **doctype**, welcher (wie du dir
vielleicht denken kannst) dem Browser den Typ des Dokuments anzeigt.
Dies ist wichtig, damit der Browser weiss, wie er das HTML-Dokument anzeigen und lesen soll.

Glücklicherweise ist der HTML5-Doctype extrem simpel - er ist einfach `html`.

Öffne eine neue Datei mit deinem Texteditor und schreibe dies in die erste
Zeile:

    <!DOCTYPE html>

Dann speichere die Textdatei mit der Datei-Erweiterung `.html`. Du editierst nun
ganz offiziell ein HTML Dokument.

## Strukturiere dein Projekt

Du kannst HTML-Dateien anlegen, wo du möchtest. Jedoch empfehlen wir dir,
dass du Verzeichnisse nutzt, um deine Dateien zu organisieren. So sind sie später
einfacher wiederzufinden.

* Erstelle an beliebiger Stelle ein Verzeichnis für diesen Workshop. Zum
  Beispiel auf dem Desktop oder in deinem Benutzer-Verzeichnis.
  Nenne das Verzeichnis *OTS_HTML_Workshop* oder ähnlich.

* Erstelle ein Verzeichnis innerhalb des Workshop-Verzeichnisses.
  Nenne es **exercise1** oder ähnlich.

* Vom Texteditor aus, speichere dein erstes HTML-Dokument in
  dem *exercise1*-Verzeichnis. Nenne die HTML Datei *page.html* oder ähnlich.

Mit der Zeit werden wir noch weitere Dateien zu diesem Verzeichnis hinzufügen und
später auch ganz neue Verzeichnisse, parallel zu *exercise1* anlegen.

## Elemente und Tags

Das sind die grundlegenden Bausteine von HTML.

**Elemente** *sind das*, was ein HTML-Dokument ausmacht. Weil man Elemente
ineinander verschachteln kann, entsteht eine *hierachische* Struktur im
HTML-Dokument. Ein Element kann drei Dinge beinhalten: ein Tag, ein Attribut
und Inhalt.

Ein **Tag** ist etwas, das den Zweck eines Elements angibt. Das `<p>` Tag zum
Beispiel gibt an, dass es sich bei dem Element um einen
Absatz (*P*aragraph) handelt. Das `<li>` Tag gibt an, dass hier ein Listen-Eintrag
(*L*ist *I*tem) stehen soll. Du wirst bereits festgestellt haben, dass Tags
immer von spitzen Klammern eingefasst sind. **Öffnende** und **schliessende** tags markiegen den Anfang und das Ende eines Elements. Ausserdem umschliessen sie dessen Inhalt:

    <p>This is a paragraph.</p>

Wie du siehst, beginnt das schließende Tag mit einem `/`. Andernfalls
wäre es ein weiteres öffnendes Tag!

Prüfe bitte **immer** doppelt, dass du alle deine öffnenden Elemente wieder
geschlossen hast. Andernfalls wird der Browser beim Anzeigen deines
HTML-Dokuments seltsame Dinge machen.

Es gibt eine Hand voll spezieller Elemente, die eine Auznahme zur Regel
darstellen. Wenn Elemente nichts anderes als den Tag-Namen beinhalten können,
brauchen sie auch nicht geschlossen werden. Zum Beispiel die folgenden Elemente
sind sogenannte 'selbst schliessende' Elemente:

    <hr>
    <input>
    <img>

Es gibt nicht viele dieser Elemente und du wirst schnell herausfinden, welche
Elemente selbstschliessend sind, indem du ein wenig mehr Code schreibst. :)

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

Im Beispiel findest du zum ersten Mal ein **Attribut**. Ein Attribut beginnt
mit einem Namen in Kleinbuchstaben und wird dann nahezu immer
mit `=` und einem 'Wert' weiter geführt. Der Wert ist von doppelten
Anführungszeichen umschlossen. In etwa wie `"das hier"`. Ein Element kann viele
Attribute haben. In so einem Fall werden die Attribute mit einem Leerzeichen von
einander getrennt. Dazu gleich mehr. Attribute geben bestimmte Informationen über
Elemente.

In diesem Fall, hat das `<div>`-Tag, welches genutzt wird um Elemente
zu gruppieren, ein `id`-Attribut mit dem Wert `first-heading`. Das sagt uns,
dass diese Sektion des HTML-Dokuments bestimmt wurde, um die erste Überschrift
der Website zu beinhalten. Du wirst später mehr über spezielle Attribute lernen.


## Html und Head-Elemente

Zurück zu unserer Datei (hoffentlich programmiert ihr bereits nebenher mit!).
Nach dem Doctype beginnen wir das HTML-Dokument, mit einem `html` Element:

    <html>
    </html>

Es umschliesst jedes weitere Element in unserem HTML-Dokument. Kein Element darf
ausserhalb des Elements `html` stehen. Als nächstes trennen wir jedes Dokument
in zwei wichtige Teile: einen **head** und einen **body**. Stellvertretend für
Dokumenten-Kopf und Dokumenten-Körper.

Der Kopf beinhaltet den Titel der Seite und Informationen **über** das Dokument.
Man nennt diese Informationen auch **Meta**-Informationen. Die meisten
Meta-Informationen sind für den Benutzer nicht sichtbar und haben dennoch
eine Menge Sinn. Zum Beispiel können Meta-Informationen den Suchmaschinen
mitteilen, wer der Autor einer Website und was in etwa der Inhalt der Seite
ist. Hier ist ein Beispiel:

    <head>
        <meta charset="UTF-8">
        <meta name="description" content="Free Web tutorials">
        <title>My first Portfolio</title>
    </head>

Wie du siehst, ist das Meta-Tag ein selbstschliessendes Element! Als erstes
steht dort ein `charset` Meta-Tag. Das ist das wichtigste Meta-Tag. Ohne dieses
könnte es sein, dass deine Website nicht korrekt angezeigt wird. Es wird als
empfohlene Vorgehensweise angesehen, dass es als erstes Folge-Element des
`head`-Elements eingesetzt wird. Es spezifiziert den Zeichensatz deines
HTML-Dokuments. Das bedeutet, dass der Browser in der Lage sein wird,
Sonderzeichen wie ä, ö, ü, €, è und so weiter, auch auf Systemen anderer
Sprache korrekt anzuzeigen. `UTF-8` ist üblicherweise das gängigste Zeichensatz-Encoding, das im Web eingesetzt wird.

Hier haben wir ausserdem ein weiteres Meta-Tag genutzt: die `description`
(Beschreibung). Wir definieren dieses Meta-Tag mit dem Attribut `name` und
setzen `description` als Wert zwischen die doppelten Anführungszeichen.

Innerhalb unseres `head`-Elements haben wir als letztes Element den Titel
unserer Website. Schreibe den oberen HTML Code aus dem Beispiel in dein eigenes
HTML-Dokument im Editor. Dann ändere den Inhalt zwischen dem `<title>`-Element.
Jetzt kannst du dein Dokument im Browser öffnen und schau dir mal an, was im Titel
des Browserfensters steht. Das ist ebenfalls der Titel, der genutzt wird, wenn
du eine Website als Lesezeichen hinzufügst.

Tags im `head`-Bereich können ebenfalls externe Resourcen wie CSS- oder JavaScript-Dateien beinhalten. Wir werden uns damit später noch beschäftigen.

## Der HTML-Body

Endlich kommen wir an die Stelle, wo unser Inhalt hinkommt.
Der `body` beinhaltet den eigentlichen Inhalt einer Seite. Alles innerhalb der
öffnenden und schließenden `body`-Tags ist für den Besucher der Website sichtbar.

Direkt nach dem schließendem `head`-Tag, aber noch innerhalb des `html`-Elements
fügen wir die `body`-Tags hinzu:

    <body>
    </body>

Alles innerhalb des `body`-Tags wird dem Besucher angezeigt werden.
Schreibe etwas einfachen Text zwischen die `body`-Tags und schau dir das Ergebnis
im Browser an.

**TIPP**: Benutze die "Seite aktualisieren"-Funktion (STRG+R oder F5), um das
gleiche HTML-Dokument im Browser neu zu laden.

## Inhalts-Typen

Es gibt verschiedene HTML-Elemente, die wir einsetzen können, um unterschiedliche
Inhaltes-Typen anzugeben. Beispielsweise das `p` Tag, das wir bereits kennen
gelernt haben. Versuchen wir zunächst eine Überschrift gefolgt von einem
Paragraphen:

    <body>
        <h1>I'm the title.</h1>
        <p>And I'm a paragraph!</p>
    </body>

Überschrifts-Elemente sind ziemlich einfach zu verstehen. Sie beginnen mit `h1`
stellvertretend für die größte Schrift und Wichtigkeit, bis hin zu `h6` mit der
kleinsten Schrift.

## Einrückung

Wunderst du dich, warum wir die `h1` und `p`-Tags innerhalb des `body`-Tags *eingerückt* haben?

Das wird in keinster Weise die Interpretation und Darstellung durch den Browser
beeinflussen, aber es gilt als guter Stil unter Programmierern, dass man Code
so formatiert. Damit soll gewährleistet bleiben, dass ein Dokument sauber
strukturiert und verständlich bleibt. Selbst wenn die Anzahl an Code-Zeilen wächst oder
man lange nichts mehr an dem Dokument gemacht hat. Ausserdem unterstreicht diese
Art der Formatierung sehr gut die hierachische Natur von HTML.

## Kommentare

Es ist ausserdem möglich "Kommentare" in dein HTML zu setzen. Kommentare in HTML
sind dazu da, dich oder andere Leute auf bestimmte Dinge zu hinzuweisen, ohne die
Darstellung deiner Website im Browser zu verändern.

Wie andere HTML-Elemente werden auch Kommentare als ein Tag geschrieben. Mit
dem einzigen Unterschied, dass ein Kommentar ein wenig anders aussieht:

    <!-- I am a comment -->

Das "Kommentar Start"-Tag ist `<!--` und das "Kommentar Ende"-Tag ist `-->`.

Kommentare können andere HTML-Elemente umschließen, um sie
"auszukommentieren". Das ist eine nützliche Vorgehensweise, wenn du mit einer
Website experimentieren möchtest um zu sehen, wie sich Dinge im Browser
verändern werden.

Versuche zum Beispiel mal die Überschrift `h1`, im `body` Teil des HTML Dokuments,
auszukommentieren.

    <body>
        <!-- <h1>I'm the title.</h1> -->
        <p>And I'm a paragraph!</p>
    </body>

Wenn du die Seite im Browser neu lädst, wirst du feststellen, dass die Überschrift
verschwunden ist.

Entferne die Kommentar-Tags (damit die Überschrift wieder erscheint) bevor du
zur nächsten Sektion übergehst.

## Bilder

Überschriften und Paragraphen geben dir die grundlegenden Elemente zur
ÜTextformatierung. Doch was ist mit Bildern?

Bilder werden in separaten Bild-Dateien ausserhalb des HTML Dokuments
gespeichert. Suche dir ein Lieblings-Bild aus dem Web und speichere es in das
gleiche Verzeichnis, wo auch deine HTML-Datei bereits liegt. Klicke dazu mit der
rechten Maustaste auf das entsprechende Bild und wähle "Bild speichern"
(oder ähnliches) aus dem Menü.

Falls dir spontan kein Bild einfällt, dann  [ist hier eine Website mit Fotos
von Katzen](http://www.flickr.com/photos/nengard/67501122/sizes/s/), die du
nutzen kannst. () (Süße Katzen im Internet? OMG!)

Nachdem du dir ein Bild ausgesucht hast, kannst du es in dein HTML-Dokument
einbauen, indem du das `img` Tag nutzt.

    <img src="kittens.jpg">

Füge das `img`-Tag irgendwo innerhalb des `body`-Tags hinzu. Am besten dort, wo
du es gerne anzeigen lassen würdest. Ersetze "kittens.jpg" mit dem Dateinamen
des Bildes, dass du in das gleiche Verzeichnis wie dein HTML-Dokument gespeichert
hast.

Beachte bitte, dass `img`-Tag ist eines der Tags, die kein separates,
schliessendes Tag benötigen. Du kannst zwar ein schliessendes "</img>"-Tag direkt
nach dem öffnendem "<img>"-Tag setzen, jedoch wird das nichts daran ändern, wie
der Browser die Website anzeigen wird.

**TIPP:** Die Bildquelle ("src") von `kittens.jpg` ist ein Pfad, relativ zur
HTML-Datei. In diesem Fall befindet sich `kittens.jpg` im selben Verzeichnis.
Du könntest ebenso eine Bildquelle wie `images/kittens.jpg` nutzen, solange du
das Bild in ein Unterverzeichnis namens "images" legst. Du kannst sogar komplette
URLs wie `http://myawesomesite.com/pictures/kittens.jpg` nutzen, aber es ist
(wenn möglich) besser, sowas zugunsten eines relativen Pfads zu vermeiden.

### Alternativer Text

Es ist eine gute Angewohnheit, sogenannten "alt text" zur textuellen
Beschreibung des Bild-Inhalts zu nutzen.

    <img src="kittens.jpg" alt="Some kittens">

Das ist wichtig für jeden Besucher, der keine Bilder anzeigen oder sehen kann.
Zum Beispiel  sehbehinderte Menschen, die einen Screenreader nutzen (auch
Braille-Zeile genannt). Jedes Bild, das nicht aus rein dekorativen Gründen im
HTML eingebettet wird, sollte eine Bild-Beschreibung über das "alt=" Attribut
bekommen.

## Nochmal alles zusammen

Bis hierhin sollte unser gesamtes HTML-Dokument in etwa wie folgt aussehen:

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

## Warum sollte man kein grafischen Editoren nutzen?

Grafische Editoren existieren und einige Leute benutzen diese auch.
Man spricht dann von "What You See Is What You Get"- oder WYSIWYG-Editoren.
Auf lange Sicht kann ein grafischer HTML Editor deine Möglichkeiten sehr
einschränken, da er ziemlich effektiv verhindert, dass du verstehst, was du tust.

## Warum sollte man kein Word nutzen?

Dein Browser möchte reine Text-Dateien verarbeiten. Wenn du Word zum
Programmieren benutzt, ist die Chance sehr hoch, dass Word automatisch
Formatierungen mit deinem Code speichert, die der Browser nicht verstehen
kann. Wenn du Word zum Erstellen von HTML verwendest, wird dein HTML
wahrscheinlich schwer lesbar und nicht standardkonform sein.

Zusätzlich haben Text-Editoren oftmals den Vorteil, dass sie Hinweise zu deinem
Code anzeigen. Man nennt sowas Syntax Highlighting.

It is like showing nouns in red and showing the verbs in blue in a sentence.

Das ist als <span style="color:blue;">hebe</span> man die
<span style="color:red">Nomen</span> eines
<span style="color:red;">Satzes</span> <span style="color:blue;">rot</span>
und die <span style="color:red;">Verben</span>
<span style="color:blue;">blau</span> hervor.

## Wie geht es weiter?

Du magst deine HTML-Seite in diesem Stadium etwas farblos und fade finden.
Wie kann man sie ein bisschen aufpeppen?

Lese in der folgenden Sektion weiter,
[Hallo Welt mit Style!](style.html).
