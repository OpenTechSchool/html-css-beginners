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

Die Werte werden also folgendermaßen gelesen:

    text-shadow: horizontal vertikal unschärfe farbwert;

Möchten wir also einen dunkelgrauen Schatten der 2 Pixel nach rechts und nach unten versetzt ist erzielen müssen wir
dies so definieren. Um keinen harten Schatten zu haben setzen wir auch eine Unschärfe von 3 Pixeln.

    text-shadow: 2px 2px 3px #777777;

Wende diesen Effekt auf alle Überschriften **`<h1>`** an und überprüfe das Ergebnis im Browser.

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

In der Webseite setzen wir dazu einen Effekt auf die `<li>` Elemente des Menü:

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

Formulare müssen mit einem **`<form>`** Tag umgeben sein. Dieser sorgt dafür, das der Browser später alle Daten aus den Formularelementen nimmt und mittels eines Senden Buttons **submit** verschickt. Innerhalb des Form Elements können aber jegliche anderen HTML Elemente auftauchen. Nur ineinander verschachtelte Forms sind zu vermeiden.

    <form action="mailto:ich@opentechschool.org">
    </form>

Das Form ist definiert aber leider noch leer. Das Attribut **action** definiert wohin das Formular geschickt werden soll. Hier wird entweder eine URL angeben oder wie in unserem Fall mit **mailto:** eine Emailadresse. Da die meisten Browser nicht in der Lage sind direkt selbst Emails zu versenden, wird beim klick auf die **submit** Schaltfläche daher das  Emailprogramm des Besuchers geöffnet und die Zieladresse sowie die Feldinhalte entsprechend vorausgefüllt.

Beginne also jetzt ein Betreffeld mit einer Beschriftung innerhalb des **`<Form>`** hinzuzufügen. 

    <label for="subject">Betreff</label>
    <input name="subject" type="text"/>

Hierdurch wird die Beschriftung "Betreff" und ein Texteingabefeld hinzugefügt. Wichtig sind hier vor allem der Name des Feldes *subject* und der Typ des Felds. Das **for** Attribut am **`<label>`** sagt dem Browser nur zu welchem Formelement die Beschriftung gehört. Eine wichtige Information speziell für Blinde und fehlsichtige Menschen.

Der Name wird beim Absenden vom Browser mit übertragen. Da wir die Eingabe als Email versenden wurde hier **subject** verwendet um den Inhalt im Betreffsfeld der Email einzufügen.

Bei unserem Betreff handelte es sich um den Feldtyp **text**. Es gibt noch eine Reihe weiterer Feldtypen wie Ankreuzfelder (Multiple Choice), Optionsfelder, Datumsfelder oder Zahlenfelder. Jede dieser Typen ermöglicht es die Eingabemöglichkeiten einzuschränken um Fehleingaben zu vermeiden und dem Benutzer eine bessere Bedienung zu ermöglichen.
Wie der jeweilige Browser das genau anzeigt kann sich jedoch unterscheiden. Eine Übersicht mit Erklärung gibt es im Internet beispielsweise [hier](http://webkompetenz.wikidot.com/html-handbuch:feldtypen-kontrollierte-eingabe).

Was fehlt ist ein Freitextfeld, wo der Besucher einen Text verfassen kann. Wir nennen es **body** um am Ende die Daten in den Text der Email zu bekommen.

    <label for="body">Ihre Nachricht an mich:</label>
    <textarea name="body" cols="50" rows="20"></textarea>

Die Textarea ist ein großes Eingabefeld das in der Länge nicht limitiert ist. Die Attribute **cols** und **rows** sagen lediglich aus das der Browser es mit 50 Zeichen Breit und 20 Zeilen höhe darstellen soll.

Kurze Kontrolle im Browser? Das Formular steht. Super! Gleich mal ausfüllen und ... ooops da fehlt ja was. Ein Knopf zum Absenden fehlt. In aktuellen Browsern erreicht man das mit dem **`<Button>`** Element.

    <button type="submit">Senden</button>

Der Type **submit** (Senden) bewirkt das der Browser beim Klick auf den Knopf, das umgebende Formular an den in der Action definierten Ort sendet. In unserem Falle eine Emailadresse.

Versuch mal ob jetzt alle klappt und der Benutzer Dir darüber eine Email senden kann.





