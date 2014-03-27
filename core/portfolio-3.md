---

layout: ots
title: Erweitere dein persönliches Portfolio

---


Um den Umfang der Seite noch zu erweitern und einen echten Lebenslauf zu erstellen bieten sich verschiedene Wege an. Im folgenden Abschnitt gehen wir auf die Gestaltung eines Lebenslaufs und einer simplen Tabelle zur übersichtlichen Darstellung von Fertigkeiten ein.

## Euer Ausbildungsweg als übersichtliche Liste

**Das Ziel**

Euer Lebenslauf sollte die folgenden Abschnitte enthalten:

* Personendaten (Name, Wohnort, etc.)
* Schullaufbahn (chronologisch)
* weitere, freie Angaben wie z.B. Ausbildungsweg oder aber Interessen

Euer Lebenslauf sollte übersichtlich sein und ansprechend wirken. Mit Hilfe der bereits erlernten Design-Elemente bauen wir eine simple Auflistung der oben genannten Punkte auf.

Erstelle eine neue Datei und beschreibe die Grundstruktur und gebt der Seite einen Titel. Erstellt im **body**-Tag eures Dokuments folgenden **div**-Tag:

	<div id="vita">
	</div>

Innerhalb dieses Containers legen wir den Lebenslauf fest und erstellen ein einmaliges Design speziell für euren Lebenslauf über die ID "vita".

Um eurem Lebenslauf eine feste Breite und Abstände zu den anderen Inhalten der Seite zu geben, sowie eine Schriftart und -Größe festzulegen weisen wir der ID "vita" noch folgende Eigenschaften in der bereits erstellten CSS-Datei zu:

	#vita {
		width: 800px;
		margin: 50px auto 50px;
		font: 14px Helvetica, Sans-Serif;
	}

Anschließend beginnen wir mit der Überschrift eures Lebenslaufs: Eurem Namen.

	<h1>Vorname Nachname</h1>

Da euer Name die größte Überschrift im Dokument sein sollte, könnt ihr diese über das **<h1>**-Tag durch CSS im Design ändern.

	#vita h1 {
		margin: 0 0 16px 0;
		padding: 0 0 16px 0;
		font-size: 40px;
		font-weight: bold;
		letter-spacing: -2px;
		border-bottom: 2px solid #999;
	}

Das Attribut "letter-spacing" ist hierbei der Abstand zwischen den Buchstaben, der durch den Wert um 2 Pixel reduziert wird.
	
Der nächste Punkt im Lebenslauf sollten eure Kontaktdaten sein, die ihr wie folgt in einem Paragraphen auflistet und eure E-Mail-Adresse direkt als Link einfügt:

	<p>
		Telefon: 0231-9876555<br />
		E-Mail: <a href="mailto:my@mail.com">my@mail.com</a>
	</p>

Die Links in eurem Lebenslauf können ebenfalls anders gestaltet werden und statt blau z.B. grau dargestellt werden. Ebenfalls kann durch die Zustandsangabe "hover" die Linkfarbe verändert werden, wenn ihr mit der Maus auf diesen zeigt.

	#vita a {
		color: #999;
		text-decoration: none;
		border-bottom: 1px dotted #999;
	}
	
	#vita a:hover {
		border-bottom-style: solid;
		color: black;
	}

Diese Eigenschaften beziehen sich durch die vorangestellte ID lediglich auf die Links in eurem Lebenslauf. Eine kurze Beschreibung zu eurer Person könnt ihr unter euren Kontaktdaten einfügen:

    <p id="introduction">
		Hier könnt ihr eine kurze Beschreibung von euch einfügen. 
	</p>

Über die angegebene ID legen wir den Stil des Textes fest.

	#introduction {
		width: 500px;
		float: left;
		font-family: Georgia, Serif;
		font-style: italic;
		color: #666;
	}

Der längste Abschnitt eures Lebenslaufs wird durch Beschreibungslisten **<dl>** umgesetzt. Eine Beschreibungsliste wird mit dem **<dl>**-Tag umschlossen und kann folgendes beinhalten:

* **<dt>**: Beschreibungsname (in unserem Fall der Abschnitt des Lebenslaufs)
* **<dd>**: Inhalt der Auflistung (in unserem Fall die Informationen zum jeweiligen Lebensabschnitt)

Beginnen wir mit der Schullaufbahn:

	<dl>
		<dt>Schulbildung</dt>
		<dd>
			<h2>Name der Schule</h2>
			<p>
				Zeitraum: August 2000 - Juli 2008<br />
				Abschluss: Euer erreichter Abschluss
			</p>
		</dd>
	</dl>
	
Unserer Auflistung geben wir nun noch ein passendes Design für die beiden verschiedenen Elemente mit.

	dt {
		font-style: italic;
		font-weight: bold;
		font-size: 18px;
		text-align: right;
		padding: 0 25px 0 0;
		width: 150px;
		float: left;
		height: 100px;
		border-right: 1px solid #999;
	}
	
	dd {
		width: 600px;
		float: right;
		margin: 0;
		padding: 0;
	}

Damit der Name der Schule noch hervorgehoben wird, definieren wir noch einen neuen Stil für die Überschrift **<h2>**:

	#vita h2 {
		font-size: 20px;
		margin: 0 0 6px 0;
		position: relative;
	}
	
Da wir den Elementfluss durch float ändern, damit die Elemente auf einer horizontalen Ebene dargestellt werden, müssen wir diesen nach dem jeweiligen **<dt>**-Element wieder zurücksetzen. Hierfür haben wir eine Klasse angelegt, mit deren Hilfe ein leeres **<dd>**-Element erzeugt wird, um den Elementfluss zurückzusetzen.
	
	<dd class="clear"></dd>

Der dazu gehörige CSS-Code sieht wie folgt aus:

	dd.clear {
		clear: both;
		float: none;
		margin: 0;
		height: 15px;
	}

Durch die Höhenangabe wird zudem ein Abstand zum nachfolgenden Element hergestellt.


Zusätzlich zu eurer Schullaufbahn könnt ihr noch euren Ausbildungsweg, eure Interessen oder Sprachkenntnisse durch weitere Einträge (**<dt>** und **<dd>**-Elemente) hinzufügen. Orientiert euch hierfür einfach an der obigen Anleitung.

Passt anschließend das Design durch Verändern der Werte oder das Erweitern der CSS-Datei euren Vorstellungen an. Selbstverständlich könnt ihr auch gezielt neue Klassen für das Design einführen - speziell falls ihr neue Elemente in der HTML-Datei einfügt und diese erweitert. Probiert es aus!


## Ergänzend: Eure Kenntnisse, Schwerpunktbereiche oder Sprachen als Tabelle

Als Erweiterung zu eurer Laufbahn, euren Abschlüssen und Interessen bieten sich noch Fertigkeiten, z.B. in Programmiersprachen oder mit gängiger Software an. Als sehr einfache Methode zur Darstellung zeigen wir euch, wie ihr Tabellen erstellt.

Erstellt zuerst einn **<div>**-Container unterhalb eures Lebenslaufs.

		<div id="skills">	
		</div>
		
Innerhalb dieses Containers erstellen wir die Tabelle und definieren im Stylesheet das Aussehen/Verhalten der Tabelle, die wir aufbauen.

Eine Tabelle wird mittels des **<table>**-Tags geöffnet und wie gewohnt wieder geschlossen. Innerhalb der Tabelle sollten die Beschriftungszeilen/-Spalten und die einzelnen Inhaltszellen definiert werden.

	<table>
		<thead>
			<tr>
				<th>Bereich</th>
				<th>Erfahrung</th>
				<th>Kenntnisse</th>
			</tr>
		</thead>
	</table>

Das Tag **<thead>** steht für den Kopf-Bereich der Tabelle. Innerhalb des Kopfbereichs, welcher so noch keine Zellen beinhaltet wird eine Zeile der Tabelle mit **<tr>** erstellt. Die Zeile muss anschließend mit einzelnen Zellen gefüllt werden. **<th>** steht hierbei für eine Zelle, die speziell als Kopf-Zelle gedacht ist. Wir erstellen in der ersten Zeile 3 Zellen und arbeiten somit mit 3 Spalten, die nach und nach gefüllt werden sollen.

Jede Tabellenzeile muss einzeln erstellt werden und in jeder Zeile sollten genau so viele Zellen enthalten sein, wie es Spalten gibt. Hier sollten somit immer 3 Zellen pro Zeile erstellt werden.

Um die Tabelle nach dem Tabellenkopf mit Inhalt zu füllen, erstellen wir hinter dem geschlossenen (!) Kopfbereich (**</thead>**) den Body ("Körper") der Tabelle:

	<tbody>
		<tr>
			<th>Tabellenkalkulation</th>
			<td>Sehr gut</td>
			<td>Komplexe Tabellen, Szenarien, Formeln</td>
		</tr>
	</tbody>
	
Wie bereits erwähnt sollen es drei Zellen pro Zeile sein. Ergänzt bitte noch weitere Zeilen, wie z.B. eure Kenntnisse zur Textverarbeitung, Datenbanken oder vollkommen anderen Bereichen. Wie im eigentlichen Header können hier zur Zeilenbeschreibung auch **<th>**-Tags verwendet werden.

Kommen wir zum Aussehen der Tabelle. Zuerst sorgen wir für die zum Lebenslauf passende Ausrichtung.


	#skills table {
		margin: 50px auto 50px;
	}

	
Wenn ihr die Seite neu ladet werdet ihr feststellen, dass die Tabelle noch immer sehr gedrungen und dadurch nicht übersichtlich wirkt. Fügt den Zellen (Inhalt, als auch den Kopfzellen) einen Innenabstand hinzu:


	#skills table td, table th {
		padding: 5px;
	}

	
Um die Beschriftungen der Zellen hervorzuheben und den Text der Zeilenbeschriftungen rechtsbündig zu machen, setzen wir noch Hintergrundfarben und die Textausrichtung.

	#skills table thead th {
		background-color: #4488FF;
	}

	#skills table tbody th {
		text-align: right;
		background-color: #0066AA;
	}			

Wie immer könnt ihr gerne die Darstellung nach eurem Geschmack anpassen.


## Mein Lebenslauf sieht gut aus - was ist, wenn er gedruckt wird?

Auch wenn Webseiten-Ausdrucken ein unnötiger Volkssport ist, kann es besonders bei Lebensläufen natürlich vorkommen, dass diese ausgedruckt werden.


**Farbenfrohe Webseite? Kein Problem!**

Für den Fall, dass ihr euren Lebenslauf in einer anderen Darstellung auch ansehnlich druckbar machen wollt - ihr aber eure Darstellung auf der Webseite nicht speziell auf den Druck auslegen wollt, könnt ihr in eurem HTML-Dokument einfach auf eine andere CSS-Datei verweisen, die mit einem bestimmten Schlüsselwort speziell für Druckausgaben verwendet wird.

Erstellt eine Kopie eurer CSS-Datei im gleichen Ordner und benennt diese in "print.css" um. Den Inhalt könnt ihr später nach und nach anpassen.

Bindet nun in eurem HTML-Dokument die neu erstellte CSS-Datei im **<head>**-Bereich mit folgender Zeile ein:

	<link rel="stylesheet" type="text/css"; media="print" href="print.css">

Durch die Medienangabe "print" wird festgelegt, dass dieses Stylesheet speziell zum Druck verwendet wird.

Entfernt für einen einfachen Test einmal die Farbangaben der Tabellenhintergründe oder ändert diese in eine andere Farbe (z.B. Grau) ab. In der Druckvorschau eures Browsers ist diese Tabelle nun nicht mehr so farbenfroh wie vorher.
	
	