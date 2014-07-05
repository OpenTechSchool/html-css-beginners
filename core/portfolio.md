---

layout: ots
title: Erstellt euer eigenes Portfolio

---

# HTML5-Struktur und CSS

## Das Ziel

Wir werden eine persönliche Website mit einem Hauptmenü, dem
Inhaltsbereich und einer Fußzeile erstellen. Den Inhalt werden wir mit einem
Bild und etwas Text füllen.

In diesem Abschnitt arbeiten wir speziell mit HTML5-Elementen, die ihr in diesem
[HTML5 cheat sheet](http://www.smashingmagazine.com/2009/07/06/html-5-cheat-sheet-pdf/) finden könnt.

## Hauptinhalt

Wir werden mit der Hauptseite unserer Website beginnen, da diese überwiegend
das Design un den Aufbau der gesamten Website vorgibt.

## Projektaufbau

Erstellt ein neues Verzeichnis (z.B. namens *portfolio*) für eure Website und
kopiert alle Dateien aus dem Verzeichnis *example1* hinein. Somit müsst ihr
nicht komplett von vorn anfangen und habe eine Basis, auf der ihr aufbauen
könnt.

Nachdem ihr die Dateien in *portfolio* kopiert habt könnt ihr mit dem
Bearbeiten der HTML-Datei beginnen. Bitte entfernt alle Inhalte des
`<body>`-Tags, um eine leere Seite zu erhalten. Die Meta-Informationen und der
Link zur CSS-Datei bleiben hierbei erhalten.

## Erstellen der Seite

Fangen wir damit an, den Inhalt unserer Seite mit einem `<div>`-Tag zu
umgeben, um den Inhalt zentriert darstellen zu können.
*"Ein `<div>`-Tag
definiert einen Abschnitt innerhalb eines HTML-Dokuments und wird verwendet,
um Elemente zu gruppieren und gemeinsam mit CSS zu formatieren, um eine
Website zu gestalten."*

Um `<div>`-Elemente sinnvoll zur Gruppierung verwenden zu können, müssen wir
diesen einen Namen geben, da wir diese sonst nicht einzeln ansprechen können.
Es gibt zwei Möglichkeiten, ihnen einen Namen zu geben: Anhand einer ID (id)
oder einer Klasse (class). Unter der ID ist dabei etwas einzigartiges zu
verstehen, das pro Seite nur ein Mal verwendet wird. Eine ID wird somit nur
verwendet, wenn man ihr ein einzigartiges Design, das nur für dieses eine
Element gültig ist, geben möchte.  Klassen hingegen werden verwendet, um
gleichartige Dinge zu gruppieren, die mehrmals in einem Dokument auftreten
können.

Wir können nun mit dem Inhalt unserer Seite anfangen:

    <div id="wrap-centered">
    </div>

Dieses Element soll den Hauptinhalt unserer Seite beinhalten. Da wir nur einen
Hauptinhalt haben, arbeiten wir mit dem ID-Selektor.

In der Datei styles.css können wir nun festlegen, dass der Inhalt dieses Div-
Elements immer zentriert dargestellt wird. Um eine Klasse via CSS aufzurufen,
wird diese mit einem vorangestellten Punkt (.Klassenname) aufgerufen. IDs
hingegen werden mit einer vorangestellten Raute (#) aufgerufen.

    #wrap-centered {
        width: 100%;
        margin: 0 auto;
    }

Hier legen wir fest, dass das Element eine Breite von 100% hat und mit dem
Abstand (margin) wird festgelegt, dass das Element zentriert ist. Wir
verwenden Prozentangaben bei der Breite, damit die Website sich automatisch
der Bildschirmauflösung oder der Größe des Browser-Fensters anpasst.

Am Anfang der `styles.css` fügen wir nun eine Beschreibung für alle Elemente (*) ein:

    * {
        padding: 0;
        margin: 0;
        border: 0;
    }

Damit wird für alle Elemente kein Innen- und Außenabstand, sowie kein Rahmen
vorgegeben. Das setzen dieser Ausgangswerte ist besonders wichtig, da jeder
Browser für verschiedene Elemente andere Ausgangswerte verwendet und die
Positionierung von Elementen somit unwahrscheinlich schwierig werden kann.

## Navigationsmenü

Nun wird es Zeit für unsere Navigation.
Innerhalb unseres div-Elements erstellen wir nun unser erstes HTML5-Element.

    <nav>
        <ul>
            <li>Home</li>
            <li>|</li>
            <li>Contact</li>
        </ul>
    </nav>

Hier haben wir 3 neue Elemente: Zu allererst haben wir das `<nav>`-Tag,
welches die Hauptnavigation einer Website beinhaltet. das `<ul>`-Tag
beinhaltet eine Auflistung und jeder Eintrag, der mit `<li>` gekennzeichnet
ist, wird in dieser Liste dargestellt. `<ul>` steht im übrigen für  eine
unsortierte Liste ("unordered list").

Eure styles.css:

    nav {
        width: 100%;
        margin-top: 20px;
    }

    nav ul {
        list-style-type: none;
        float: right;
        margin-right: 20px;
    }

    nav li {
        display: inline;
        color: #08c;
    }

`nav ul` ist eine Methode, um nicht alle unsortieren Listen zu beschreiben,
sondern nur die, die sich innerhalb des `<nav>`-Elements befinden. Die meisten
hier verwendeten Elemente kennt ihr entweder bereits oder könnt sie einfach
nachschlagen.

Jetzt möchten wir um über eine bestimmte Eigenschaft reden, welche sehr
mächtig ist: `float: right;`.

Diese Eigenschaft sorgt dafür, dass das Element sich nicht nach dem üblichen
Textfluss der Seite richtet (normalerweise sind HTML-Elemente Block-Elemente,
welche nacheinander vertikal (wie Absätze in der Zeitung) dargestellt werden).
Stattdessen wird es zum weitestgehend rechten Rand des `<div>`-Tags, in dem es
sich befindet, gesetzt.

Wenn ihr euch das in eurem Browser anseht, ist das nav ul auf der rechten
Seite platziert.  Float kann die Werte left oder right haben. Man sollte bei
der Verwendung von float immer bedenken, dass es die Orientierung aller
(nachfolgender) HTML-Elemente ändert und nicht nur des Elements, in dem man es
setzt.

Durch float kann somit der vorgegebene vertikale Text- und Objektfluss von
HTML verändert werden.

Eine weitere Eigenschaft, die den Textfluss verändert ist: `display: inline.`
Tatsächlich handelt es sich hier um keine Änderung des gesamten Textflusses,
sondern sorgt lediglich dafür, dass dieses Element in der gleichen Zeile mit
anderen inline-Elementen angezeigt werden kann. Schaut es euch in eurem
Hauptmenü einmal an. Da mit float auch das Verhalten der nachfolgenden
Elemente verändert wird, müssen wir dies für die kommenden Elemente wieder
zurücksetzen. Dafür erstellen wir im HTML-Quelltext einen neuen Abschnitt.

    <div class="clear"></div>

Und in der CSS-Datei legen wir folgendes an:

    .clear {
        clear: both;
    }

Hiermit entfernen wir die float-Eigenschaften sowohl für `float: right` als
auch für `float: left`. (Es kann auch nur eine Eigenschaft mit `clear: left`
oder `clear: right` zurückgesetzt werden. Wenn man mit `float` experimentiert
empfiehlt und Probleme mit nachfolgenden Elementen hat empfiehlt es sich
immer, zu Testzwecken `clear: both;` in den entsprechenden Abschnitt
einzufügen, um sicher zu gehen, dass es nicht am float liegt.

## Die Fußzeile (Footer)

Der Footer befindet sich immer ganz am Ende einer Seite und enthält
zusätzliche Informationen. Einen Footer legt man wie folgt an:

    <footer>
        <p></p>
    </footer>

Innerhalb des `<p>`-Tags könnt ihr schreiben was immer ihr mögt, zum Beispiel
wer diese Website erstellt hat oder eure E-Mail-Adresse.

In der CSS-Datei legt ihr dann folgendes an:

    footer {
        margin-top: 50px;
    }

    footer p {
        text-align: center;
    }

Man muss natürlich nicht zwingend ein Design für den footer angeben, aber um
es optisch ein wenig vom Rest der Seite zu trennen empfiehlt sich ein Abstand
zu Elementen darüber via: `margin-top: 50px`.  Abschließend zentrieren wir den
Text im footer noch via `text-align: center`. Mehr gibt es hier nicht zu tun.

## Box Model und Schriftarten

Jetzt können wir endlich mit dem eigentlichen Inhalt unserer Seite beginnen.
Zuallererst legen wir eine Struktur fest. Es soll ein 2-Spalten-Design werden:
Eine Spalte ist schmaler (auch sidebar genannt) und wird durch das
`<aside>`-Tag beschrieben. Die andere Spalte beinhaltet unseren Hauptinhalt,
welche durch das `<section>`-Tag umfasst wird. Innerhalb der section lässt
sich der Inhalt noch in verschiedene Einträge/Beiträge, sogenannte articles,
unterscheiden.  Um über den eigentlichen Inhalt unserer Seite mehr Kontrolle
zu haben, schachteln wir diesen ebenfalls in ein weiteres div-Element namens
"content".

Tipp: Wenn ihr euch bei der Größe oder genauen Anordnung eurer Elemente nicht
sicher seid, so ändert einfach mal die Hintergrundfarbe, damit ihr besser
sehen könnt, wo das Element anfängt und wo es aufhört.

    <div class="content">
        <aside>
        </aside>
        <section>
        </section>
    </div>

Und in der styles.css:

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

Zuerst haben wir dem Inhalt der Seite eine relative Breite gegeben und es in
der Mitte der Seite platziert. Anschließend haben wir dem aside-Block eine
Minimalgröße und Abstand zu anderen Elementen gegeben. Zusätzlich haben wir
den Rand zur rechten durch einen dünnen Rahmen hervorgehoben. Zu guter letzt
haben wir den Textfluss wie float: left geändert, um den Hauptinhalt der Seite
direkt rechts von der sidebar anzuzeigen. Es ist wichtig, dass auch display:
inline-block für die `<section>` gesetzt wird.

Im aside-Block fügen wir nun ein Profilbild von uns ein, um die Seite persönlicher zu gestalten.

    <aside>
        <img src="me.jpg"/>
    </aside>

    img {
        width: 272px;
        margin-top: 10px;
    }

Wenn ihr die Größe des Bildes nicht kennt, schaut am besten in den
Dateieigenschaften nach der Größe und passt die Bildgröße im Code entsprechend
an.

Jetzt wird es Zeit für eure persönliche Vorstellung!

    <section>
        <article>
            <header>
                <h1>Title</h1>
                <h2>Second title</h2>
                <p>Hello hello hello</p>
            </header>
        </article>
    </section>

In diesem Beispiel haben wir innerhalb der section noch einen article
eingeschoben. Jeder article hat eine Überschrift und einen Untertitel. Danach
folgt der eigentliche Inhalt im `<p>`-Tag. Füll die Einträge bitte mit etwas
Inhalt, da wir hiermit noch weiterarbeiten werden.

Bevor wir das Design anpassen, gilt es etwas über das Box Model zu lernen.

Warum ist das Box Model eigentlich so wichtig?

Jedes Element im Webdesign ist (für den Browswer) eine rechteckige Box mit Innen-
und Außenabständen. Diese Abstraktion wird "Box Model" genannt. Eine graphische Darstellung seht ihr hier:

<img src="../images/css-box-model.gif" />

Was genau machen diese Elemente?

* Margin: Außenabstand außerhalb des Rahmens. Eine Hintergrundfarbe kann nicht angegeben werden. Der Abstand ist immer transparent.
* Borders: Der Rahmen wird außerhalb des Innenabstandes (padding) gezeichnet. Ein Rahmen wird meist mit einer Farbe und der Rahmenstärke beschrieben.
* Padding: Dies ist der Innenabstand vom Inhalt der Box zum Rahmen. Der Innenabstand hat immer die Hintergrundfarbe des Boxinhaltes selbst.
* Content: Dies ist der Inhalt der Box, inklusive Texten, Bildern, etc.

Margin beeinflusst nicht die Größe der Box selbst, aber ggf. die Größe anderer Boxen auf der Seite.

Die größe einer Box berechnet sich wie folgt:

**Breite:** width + padding-left + padding-right + border-left + border-right

**Höhe:** height + padding-top + padding-bottom + border-top + border-bottom

Tipp: Wie bereits erwähnt sollte man alle Abstände zu Beginn des Stylesheets
auf 0px setzen. Da wir jetzt wissen, wie man die Boxgröße berechnet, sollten
wir mit der Box um unseren `<article>` arbeiten.


**Textdarstellung**

Da unser Text noch ziemlich langweilig aussieht, sollten wir diesen etwas
aufstylen. Bisher haben wir nur mit der Textfarbe und Textausrichtung
gearbeitet. Andere Werte für die Textausrichtung (`text-align`) sind `left`,
`right` and `justified` (Blocksatz). Der Standardwert für die Textausrichtung
ist left.

Blocksatz bietet sich an, damit der Text ein wenig aufgeräumter aussieht und die Zeilen komplett ausfüllt - wie in Tageszeitungen und Zeitschriften. Eine weitere wichtige Frage ist die nach dem Schrifttyp. Mittels der Eigenschaft `font-family` legt man die Schriftart fest.

Es gibt zwei Typen von Schriftarten:

* generic family: Hierbei handelt es sich nicht um eine genaue Schriftart, sondern um eine Gruppe von Schriftarten (z.B. `Serif` oder `Monospace`, wobei es sich um Serifen-Schriftarten oder Schriftarten mit gleichbleibender Buchstabenbreite handelt)

* font family: Hierbei handelt es sich um eine konkrete Schriftart (wie z.B. `Times New Roman` oder `Arial`)

Eine Möglichkeit ist es, eine häufige font-family zu wählen (damit die meisten Browser diese ähnlich darstellen können). Diese nennt man "web-safe".

Tipp: Falls ihr eigene Schriftarten herunterladet und diese verwendet, bedeutet das nicht, dass andere Besucher der Website diese auch zur Verfügung haben. Daher empfiehlt es sich, auf Standard-Schriftarten zurückzugreifen.

    h1, h2 {
        font-family: Georgia, serif;
    }

    p {
        font-family: "Trebuchet MS", Helvetica, sans-serif;
        font-size: 0.9em;
    }

Hier sehen wir direkt eine sehr wichtige Eigenschaft: font-size (die
Schriftgröße). Wie ihr bereits wisst bezieht sich die Schriftgröße ebenfalls
auf den gesamten Selektor. Jeder Browser verwendet eine Standard-Schriftgröße,
aber um ein möglichst gutes Aussehen zu erreichen, solltet ihr diese selbst
setzen. Man sollte allerdings niemals Schriftgrößen verwenden, um Texte wie
Überschriften aussehen zu lassen oder umgekehrt. Verwendet hierfür immer die
dafür vorgesehenen Tags.

Die Schriftgröße kann in `px`, `em` oder `%` angegeben werden. Eure
Bildschirmauflösung legt fest, wie viele Pixel ihr auf eurem Bildschirm seht.
Ihr könnt also eine Schriftgröße von 12 Pixeln (`font-size: 12px;`) festlegen.
Hierbei hat die Schrift dann eine Höhe von 12 Pixeln. Mit `font-size: 50%;`
setzen wir die Schriftgröße auf 50% der Schriftgröße des übergeordneten
Elements. `em` ist ebenfalls eine relative Größenangabe, allerdings wird diese
anders angegeben. 150% wären hierbei 1.5em.

Um von der Schriftgröße in Pixeln zu em umzurechnen, rechnet man meist: `Pixel
/ 16 = em`.

Zum Beispiel:

    h1 {
        font-size: 2.5em;  /* 40px / 16 = 2.5em */
    }

Es ist schwierig zu sagen, wie man Größen wählen sollte, da dies sehr stark
abhängig vom allgemeinen Design der Website abhängig ist. Derzeit lässt sich
sagen, dass die Schriftgrößenangabe in em am praktischsten ist. Die meisten
Anwender haben verschiedenste Endgeräte mit mehreren Auflösungen, Pixeldichte
und Formaten. Hierbei sind relative Größenangaben am besten und am leichtesten
anpassbar.

Eine gute Lösung kann auch sein, die Schriftgröße im body-Element auf 100% zu
setzen (font-size: 100%) und in jedem weiteren Selektor mit em zu arbeiten.

So, jetzt ist es Zeit, die Seite nach euren Vorlieben anzupassen und zu
experimentieren. Wenn ihr mehr als die angesprochenen Eigenschaften
ausprobieren wollt, könnt ihr auf den verlinkten Seiten nachschauen oder uns
ansprechen.
