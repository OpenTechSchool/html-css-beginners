---

layout: ots
title: Erstelle Dein persönliches Portfolio

---

Bisher haben wir die Grundstruktur unserer Webseite erstellt.
Es fehlt eine Startseite (Homepage) und eine Kontaktseite.
Folgend ein paar Grundlagen, danach kannst Du Deiner Kreativität ausdruck
verleihen und selbst Experimentieren.

## Homepage und Positionierung
Wir beginnen mit der Startseite.

**Das Ziel**

Die Startseite besteht aus:

* Navigationsmenü
* einem großen zentrierten und in der größe anpassbarem Bild
* zwei Einleitungssätze (auf dem Bild)

Erstelle eine neue Datei und beschreibe die Grundstruktur.
Um ein Navigationsmenü zu erstellen kopiere einfach deine Ergebnisse des ersten
Teils.
Suche Dir ein Bild aus das Du magst. Es sollte groß genug sein und mit einer guten
Auflösung.

Füge das Bild direkt nach dem **nav** Tag ein und gib diesem einen Klassennamen
(class). Setze die Breite (width) des Bildes auf die volle Seitenbreite, also 100%.

    .home-image {
        width: 100%
    }

Auf diese weise passt sich das Bild an die Breite des Browserfensters an.
Es kann sein, das weisse Ränder an der Unterseite des Bildes entstehen. Das kann
darurch verhindert das man die Höhe (height) auch auf 100% setzt. Jetzt musst Du
aber sicherstellen das dass Bild nicht gestreckt wird.

    .home-image {
        height: 100%
    }

Dem Bild muss jetzt ein weiterer header tag folgen gefüllt mit einem h1 und h2.
Dem header solltest Du noch eine Klasse geben, damit Du ihn gestalten kannst.
Verwechsle ihn nicht mit dem für das Bild. Wir benutzen hier "header-home".
In der CSS Datei fügen wir danach dies hinzu:

    .header-home {
        position: relative;
        top: -300px;
    }

Das ändert die Position des Elements dadurch, das es aus dem normalen Fluss (flow) genommen wird.
Seine Position ist orientiert sich jetzt am Elternelement. (In Deinem Fall div#wrap-centered).
Jetzt kannst Du das Element dort positionieren wo Du möchtest mittels der Eigenschaften
top (Position von Oben), right (Position von Rechts), bottom (Position von Unten)
und left (Position von Links).

**Was bedeutet diese Positionierung?**

Wenn ein Element aus dem normalen Fluss genommen wird, ignoriert jeder andere Inhalt der
weiterhin im normalen Fluss ist dieses Elment komplett und macht keinen Platz für dafür.
Wie bereits angedeutet kann das Elmenent mittels top, bottom, left und right positioniert werden.
Damit diese Eigenschaften wirken muss jedoch zuerst die Positionseigenschaft (position)
gesetzt werden. Die Wirkung dieser Eigenschaften ist verschieden, je nachdem welche
Positionierungsart gewählt wurde.

Es gibt insgesamt vier verschiedene Positionierungsarten.

**Statisch (position:static)**
Ein statisch positioniertes Element ist eines das im normalen Fluss liegt, von oben nach unten.

**Fixiert (position:fixed)**
Ein fixiertes Element wird relativ zum Browserfenster positioniert.
Nachdem Du diese gesetzt hast, kannst Du mit der Position etwas herumspielen.
Versuche verschiedene Pixelwerte für top, bottom, left oder right zu setzen.

**Relativ (position:relative)**
Ein realativ positioniertes Element wird wie es der name vermuten lässt relativ zu der
Positon verschoben an der es normalerweise stehen würde.
Elemente die danach folgen verhalten sich als wäre das Element weiterhin an der ursprünglichen
Stelle. Es wird also Platz dafür freigehalten.
Versuche auch hier mit den top, bottom, left und right zu experimentieren.

**Absolut (position:absolute)**
Ein absolut positioniertes Element wird komplett aus dem normalen Fluss entfernt.
Es ist aber abhängig ist von Elternelementen die entweder auch absolut oder relativ positioniert sind.  

**Überlappende Elemente (z-index Eigenschaft)**

Wenn Elemente ausserhalb des normalen Flusses liegen, können diese unter Umständen überlappen.
Der z-index (Quasi die Position auf einer gedachten z-Achse) definierte die Stapelreihenfolge
eines Elements. (Welche Element liegt vor oder hinter anderen).

Mit diesem Wissen kannst Du Deine Startseite vollenden.

## Kontaktseite
Zeit die Kontaktseite anzugehen.

**Das Ziel**

Erstelle eine Seite mit:
* einem kleinen Absatz über Dich selbst
* Einige Links über die Du erreicht werden kannst

Die Kontaktseite wird die gleich Struktur haben wie die Seite zuvor.
Kopiere einfach die Datei und bennene sie in `kontakt.html` um.

Entferne dann alles aus dem `#wrap-centered` *div* tag, denn dort sollen jetzt die
Inhalte der der Kontaktseite stehen.

Füge einen Absatz hinzu und erzählen dem Besucher wer Du bist. Dafür eignet sich der
`<p></p>`tag.

Innerhalb dieses tags kannst Du den Text hinzufügen, der sichtbar sein soll.

Zum Beispiel: `<p>Hallo ich bin Doctor Who. Ich freue mich von Dir zu hören.</p>`

Um einen Zeilenumbruch nach dem ersten Satz zu erzwingen kannst Du `<br/>` verwenden.
Vielleicht möchtest Du Deinen namen auch noch *kursiv* darstellen: `<i>Doctor Who</i>`.

Wenn Du den Absatz noch weiter gestalten willst, solltest Du dies über die CSS Datei tun.
Mittels einer Klasse am Abasatz `<p class="contact-info">` kannst Du in der CSS Datei
die Textgestaltung anpassen:

    .contact-intro {
        font-size: 20px;
        font-family: Arial;
        margin: 10px;
    }

Das reicht vorerst als kurze Vorstellung. Es geht weiter mit den Links über die Besucher
Deiner Seite dich erreichen können.

Füge eine Liste für die verschiedenen Kontaktwege ein mit dem `<ul> </ul>` tag (ul steht für ungeordnete Liste) und versehe auch diese mit einer Klasse `<ul class="contact-links">` um eine spätere Gestaltung zu ermöglichen.

Sagen wir also es sollen Links zu eMail, Twitter, Facebook und Github erscheinen.
Hierzu füge vier Listenelemente, also `<li></li>` tags zwischen den ul tag ein.

Schreibe in jedes dieser Elemente einen Link Tag ein auf den der Besucher klicken kann.
Diese sollten in etwa so aussehen `<a href="#"> </a>`. Das `href` Attribut kannst Du vorerst so belassen. Wir sorgen später dafür das diese Links auch funktionieren.

Prinzipiell kannst Du alles als Link benutzen. Ein Button, ein Bild, oder normalen Text.

Lass uns die Links vorerst etwas aufpeppen indem wir diese um den ersten Buchstaben des Textes setzen und jedem Link ein paar Klassen vergeben.
`contact-link` für die Eigenschaften die alle Links gemeinsam haben und für die anderen einzigartige (`email`, `twitter`, `facebook`, `github`).
Dadurch solltest Du zu folgendem Ergebnis gelangen:

    <ul class="contact-links">
        <li><a href="#" class="contact-link email">e</a>mail</li>
        <li><a href="#" class="contact-link twitter">t</a>witter</li>
        <li><a href="#" class="contact-link facebook">f</a>acebook</li>
        <li><a href="#" class="contact-link github">g</a>ithub</li>
    </ul>

Wenn Du möchtest kannst Du das `#` Zeichen oben bereits durch die URL Deines Kontos ersetzen.

**Zeit die Links mit CSS zu gestalten:**

Du kannst die Schriftart ändern, einen Rahmen um jeden Link in verschiedenen Farben und die Position für jeden ersten Buchstabens perfekt bestimmen.

Hier hier einmal ein einfaches Layout.

    .contact-links {
        padding: 0;
				list-style-type: none;
    }

    .contact-link {
        display: block;
        float: left;
        margin: 10px;
        text-decoration: none;
        color: white;
        font-family: Arial;
        font-weight: 900;
        font-size: 35px;
    }

    .email {
        background: #dd1812;
        width: 39px;
        height: 45px;
        padding: 1px 0 0 9px;
    }

    .twitter {
        background: #00acee;
        width: 30px;
        height: 42px;
        padding: 4px 0 0 18px;
    }

    .facebook {
        background: #3B5998;
        width: 30px;
        height: 42px;
        padding: 4px 0 0 18px;
    }

    .github {
        background: #171515;
        width: 35px;
        height: 46px;
        padding: 0 0 0 13px;
    }

Das war es bereits für diesen Bereich.
Probiere es aus und passe es dann an Deine Wünsche an.

## a tag

Sehr gut. Dein Portfolio ist so gut wie fertig.
Die einzelnen Seiten sollten miteinander verlinkt sein.
Dafür verwenden wir den *a* tag (Anker) der einen Hyperlink beschreibt.
Das wichtigste Attribut eines *a* elements ist dessen *href* (hypertext referenz) Attribut.
Es definiert das Ziel des Links.

Die HTML Syntax für einen Link sieht vollständig dann so aus:

    <a href="irgendeineUrl">Der Linktext</a>

Es gibt verschiedene Typen von Links. Es gibt **externe Links** die auf andere Webseiten zeigen.
Dieser Link ist absolut und entspricht dem was Du in der Adresszeile des Browsers siehst.
Ein Link auf die OpenTechSchool in Dortmund würde so aussehen:

     <a href="http://opentechschool.org/dortmund">OpenTechSchool Dortmund</a>

Auch sehr wichtig sind *interne Links* die auf andere Unterseiten Deiner eigenen Webseite zeigen.
Das wollen wir als nächstes tun indem Du Dein Portfolio im Navigationsmenü um einen *a* tag innerhalb der *li* elemente erweiterst:

    <li><a href="startseite.html" >Startseite |</a> </li>

Achte darauf die URL korrekt zu schreiben, ansonsten führt diese ins nichts.
Wenn die Seite auf die Du verlinken möchtest nicht ebenfalls am gleichen Ort wie die aktuelle Seite liegt, musst Du eventuelle Unterverzeichnisse ebenfalls miteinbeziehen.
Wenn die Kontaktseite z.b. in einem extra Kontaktverzeichnis liegen würde sähe dies so aus:

    <li><a href="kontakt/kontakt.html"> Kontakt </a> </li>

Prüfe es im Browser uuuuuuuuund.... Tadaaaaaaa ein Link von der Startseite zur Kontaktseite.

Erweitere den Rest des Navigationsmenüs und alle Kontaktlinks auf die gleiche Weise.

Standardmäßig wird ein Tag vom Browser folgendermaßen dargestellt:

* Ein unbesuchter Link ist unterstrichen und blau
* Ein besuchter Link ist unterstrichen aber lila
* Ein aktiver Link (also die aktuelle Seite) ist unterstrichen und rot

Das kannst Du ebenfalls anpassen.

Eine kleine Erklärung auch noch zum mailto link.
Schreibe mailto:ich@google.com um dem Browser zu sagen er soll das Emailprogramm des Benutzers öffnen und eine neue Email an die angegebene Adresse zu schreiben.
Praktisch oder?
Bei Deinem Email link füge also statt # also einen mailto mit Deiner Emailadresse ein.

**:hover**
Es ist auch möglich die Darstellung eines Links zu verändern, sobald die Maus sich darüber bewegt.
Dafür benötigst Du den `:hover` (hover=schweben/im Bereich) selector.

    a:hover {
        color: red;
    }

Super! Du bist ferig. Jetzt liegt es an Dir noch weitere Änderungen vorzunehmen. Mach die Seite hübscher und individueller. Verändere Farben, Schriftarten oder füge Bilder hinzu. Was immer Du möchtest und bereite es vor es am Ende des Workshops zu präsentieren.

Wir freuen uns auf Deine persönliche Webseite!
