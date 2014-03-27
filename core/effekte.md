---

layout: ots
title: Effekte und Formulare

---

Viele Grundelemente haben wir bereits kennengelernt. Mit CSS kann man jedoch noch einiges mehr erreichen.
Einen kleinen Ausblick darauf soll dieser Abschnitt bieten.

## Effekte

**Das Ziel**

* Die Seite mit ein paar visuellen Effekten aufpeppen.
* Das Menü wird aufgepeppt um die Seite interessanter zu machen

### Schatten

Eine Seite kann hübscher aussehen wenn sie raffinierter gestaltet wird. Wichtig ist es mit Effekten nicht zu
übertreiben und zu versuchen einzelne wichtige Elemente herauszustellen.

Nehmen wir uns als erstes vor die Überschriften auf der Seite noch deutlicher sichtbar zu machen.
Dazu werden wir die Texte mit einem Schatten versehen. Sparsam verwendet kann der Einsatz eines
Textschattens die z.b. die Übersicht über die Seite verbessern oder etwas auflockern.

Der Schatten wird in CSS über die Eigenschaft "text-shadow" definiert. Der Wert setzt sich zusammen aus dem
horizontalem und vertikalem Versatz, einer Unschärfe und eines Farbwertes zusammen.

    text-shadow: horizontal vertikal unschärfe farbwert;

Möchten wir also einen dunkelgrauen Schatten der 2 Pixel nach rechts und nach unten versetzt ist erzielen müssen wir
dies so definieren. Um keinen harten Schatten zu haben setzen wir auch eine Unschärfe von 3 Pixeln.

    text-shadow: 2px 2px 3px #777777;

Wende diesen Effekt auf alle Überschriften (h1) an und überprüfe das Ergebnis im Browser.

Ist es geglückt dann probiere mit den Einstellungen ein wenig herum. Durch ändern der Farben und Werte
lassen sich auch andere spannende Effekte erzielen. Selbst mehrere Schatten auf einem Elemente sind möglich.

Hier noch eine kleine [Effektsammlung](http://www.onlinecasinodemar.com/webdesign/xhtml-css/beeindruckende-effekte-mit-der-css-eigenschaft-text-shadow/)
zur Inspiration und zum weiterspielen. Versuche doch mal den ein oder anderen Effekt nachzubauen der besonders gut
zu Deiner Seite und Dir passt.

### Runde Ecken

Wenn Du auf Deiner Seite einen Absatz oder ein anderes Element hast das besonders wichtig ist, kannst Du dies
z.b. mit Farben und einem Rahmen hervorheben. Da wir bisher aber nur eckige Boxen erzielt haben, möchten wir
diese etwas schöner gestalten indem wir die Ecken rund machen.

Angenommen wir haben ein Element mit der Klasse *info-box* auf der Seite. Können wir diese z.b. Orange einfärben.
Die Runden Ecken erreichen wir mit der Eigenschaft "border-radius". Der angegebene Wert entspricht dabei der Intensität
der Rundung.

    .info-box {
        background-color: orange;
        border-radius: 10px;
    }

Hierduch kann es passieren das Inhalte innerhalb der Box durch die Rundung "abgeschnitten" werden. Um dem entgegenzuwirken
muss man ggf. mit einem padding dafür sorgen das der Abstand zum Rand ausreichend ist.

Um nur einzelne Ecken abzurunden kann für jede Ecke ein eigener Wert angegebn werden.

      .info-box {
            background-color: orange;
            border-radius: 30px 0 30px 0;
      }

Dieses Beispiel rundet z.b. nur die obere linke und untere rechte Ecke ab. Verändere die Werte ein wenig um eine
interessante Form zu bilden. Zusammen mit der Bordereigenschaft kann man auf diese Weise Elemente gut herausarbeiten.

### Hovereffekte

Das nächste Ziel soll sein das Menü interaktiver zu machen. Bewegt der Besucher die Maus über die Menüpunkte,
so soll der Menüpunkt hervorgehoben werden. Dazu bietet sich der sogenannte Pseudoselektor ":hover" an.
"Hover" zu deutsch "schweben" wird immer dann auf Element angewendet, wenn die Maus sich gerade über dem Element
befindet.

In der Webseite setzen wir dazu einen Effekt auf die <li> Elemente des Menü:

    nav li:hover {
        border: 1px solid green;
        color: green;
        background-color: lime;
    }

Hier wird ein grüner Rand und Textfarbe gesetzt und die Hintergrundfarbe auf einen helleren Grünton verändert.
Speichere die Änderung am CSS ab und prüfe das Ergebnis im Browser.

Jede CSS Eigenschaft kann beim "hovern" verändert werden z.b. Textgrößen oder Schatten.
Der Fantasie sind dabei kaum Grenzen gesetzt.

### Formulare

Das Internet ist nicht nur Konsummedium. Es bietet auch Möglichkeiten die Inhalte zu bearbeiten (z.b. Wikipedia),
Kommunikation über Emails (z.b. googlemail) oder Nachrichten z.b. in Foren.
All das ist auch über Webseiten realisierbar. Um diese Eingaben möglich zu machen, verwendet man Formulare.

Formular bestehen aus verschiedenen Feldern.

