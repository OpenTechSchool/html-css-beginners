---

layout: ots
title: Hallo Welt mit Style!

---

## Wie man CSS schreibt

Es gibt zwei Wege, um CSS in einem Dokument einzubauen.

CSS kann direkt in den `<head>` des Codes eingebunden werden, indem es vom
style-Tag umschlossen wird. Es sollte direkt vor dem Ende des `</head>`-Tags
eingebunden werden.

    <style type="text/css">
        ....
    </style>

Diese Möglichkeit ("inline") bietet sich an, wenn es nur wenig Inhalt im
`<style>`-Tag gibt. In diesem Fall muss auf keine andere Datei verlinkt werden
und der Browser muss keine Dateien nachladen.

Die zweite Möglichkeit ist, den CSS-Code in eine externe Datei auszulagern.

Erstelle ein externes Stylesheet, indem ihr in eurem Editor eine neue Datei
mit der Endung ".css" im gleichen Verzeichnis eures HTML-Dokuments anlegt.
(Nenne sie z.B. `styles.css`.)

Danach kann die Datei im HTML-Dokument mit folgender Syntax (wieder vorm Ende
des `</head>`-Tags) eingebunden werden:

    <link href="styles.css" rel="stylesheet">

Wenn deine CSS-Datei mehr als ein paar Zeilen hat, empfehlen wir, sie extern
einzubinden. Du hast dann einfach bessere Übersicht.

**TIPP:** Der Verweis ("href") zu `"styles.css"` erwartet einen relativen
Pfad vom HTML-Dokument ausgehend, ebenso wie "src" es für das `<img>`-Tag
erwartet.

## Machen wir's bunt!

CSS hat eine sehr einfache Syntax. Die Datei besteht aus einer Liste von
Regeln. Jede Regel besteht aus einem oder mehreren *Selektoren* und dem
*Beschreibungsblock*.

**Selektoren** werden verwendet, um festzulegen, auf welche Teile des HTML-
Codes sich der Style bezieht. Um dies direkt für unseren erstellten Quelltext
anzuwenden, ändern wir über das Überschrifts-Tag `<h1>` die Schriftfarbe auf
rot.

    h1 {
        color: red;
    }

h1 ist hierbei der Selektor, also der Elementtyp aus unserem HTML-Quelltext,
den wir verändern möchten. *color* ist die Eigenschaft, die wir verändern
möchten and *red* ist der vergebene Eigenschaftswert. Die Syntax ist somit:

    Selektor {
        Eigenschaft: Wert; /* Bitte denkt daran, dass immer ein abschließendes ; hinter den Wert gehört */
        Eigenschaft: Wert;
    }

Ladet nun eure Seite neu und ihr seht, dass sich die Farbe der Überschrift
geändert hat.

War das nicht leicht? Um unserem Paragraphen eine Hintergrundfarbe zu geben,
fügen wir nun folgendes hinzu:

    p {
        background-color: #ddd;
    }

## Fehlersuche

Hat sich die Farbe der Überschrift nicht verändert, nachdem die Seite neu
geladen wurde?

Prüft den Dateinamen im `<link>`-Tag und schaut nach, ob die CSS-Datei auch
wirklich im gleichen Ordner wie die HTML-Datei liegt.

******

Die sogenannten Web-Farben sind Farben, die beim Gestalten von Websites
verwendet werden. Farben können entweder im 3-stelligen RGB-Format definiert
werden (256 Werte für jeden Wert, also rot, grün und blau) oder als
hexadezimaler Wert (z.B. #ddd). Hexadezimale Farbwerte beginnen mit einer
Raute (#). Diese Farben können der Einfachheit halber mit einem Werkzeug wie
dem [Color picker](http://www.colorpicker.com/), gewählt werden. Sobald die
gewünschte Farbe ausgesucht ist, kopiert diese einfach in eure CSS-Datei.
Vergesst die führende Raute (`#`) nicht.

Gut zu wissen: #000 ist schwarz und #fff ist weiß.

******

Lasst uns nun für unser im [ersten Kapitel](structure.md) eingebundenes Bild
einen Rahmen erstellen.

    img {
        border: 1px solid #000;
    }

Somit haben wir für alle eingebundenen Bilder die folgenden Werte des Rahmens
vergeben: Ein durchgängiger (`solid`), ein Pixel breiter (`1px`) Strich in
Schwarz (`#000`). Dieser Rahmen wird um alle vier Ränder des Bildes gezogen.
Wenn wir den Rahmen nur an einem der 4 Ränder haben möchten, so könnten wir
das wie nachfolgend angegeben z.B. für den oberen Rand erstellen:

    img {
        border-top: 2px dotted red;
    }

**Zusätzlich hilft auch ein [CSS cheat sheet](http://coding.smashingmagazine.com/2009/07/13/css-3-cheat-sheet-pdf/) für eine Eigenschaftsübersicht weiter.**
