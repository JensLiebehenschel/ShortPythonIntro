# Anleitung

Dies ist die Anleitung für das Bauen (oder Verändern) eines Jupyter-Books.
Ich habe ausschließlich unter Linux gearbeitet und weiß dementsprechend nicht wie oder ob man überhaupt unter z.B. Windows mit Jupyter-Books arbeitet.
Ich entschuldige mich, falls es zu Problemen führt.
Es folgen die benötigten Befehle in der Kommandozeile.

Alle Pfade, welche für Nutzer individuell sind, werden mit "..." markiert. Ich benutzte für die Beispiele absolute Pfade. Man kann auch relative Pfade nutzen, dann muss man jedoch aufpassen, welcher Ordner momentan als Working Directory gesetzt ist.

## Installieren von Jupyter-Book

```
pip install -U jupyter-book
```

## Benötigte Dateien

Da die Dateien für das Jupyter-Book für ShortPythonIntro bereits im GitHub existieren, muss kein neues Buch erstellt werden. Es gibt zwei wichtige Dateien für ein Jupyter-Book

### \_config.yml

Wahrscheinlich uninteressant, wenn es um Veränderungen geht.

Hier sind Daten über das Jupyter-Book. Zum Beispiel gibt man hier an, welches Bild als Logo oder Name für das Jupyter-Book genutzt werden soll. Das Jahr bei "copyright" ist auch egal, da die Copyright Anzeige deaktiviert ist.
Hier sind wichtige Konfigurationen, damit etwa die Interaktivität mit Thebe (https://jupyterbook.org/en/stable/interactive/thebe.html) funktioniert 

Abgesehen vom Logo oder Namen, wüsste ich spontan nicht was man hier sonst verändern möchte.
Eine Referenz über die möglichen Konfigurationen: https://jupyterbook.org/en/stable/customize/config.html


### \_toc.yml

In dieser Datei gibt man an, welche Dateien zu einem Buch gemacht werden sollen.

Dafür da, wenn man den Dateinamen einer Seite (z.B. einer Markdown-file) verändert hat oder neue Seiten hinzufügen/Reihenfolge der Seiten verändern möchte.
In der Reihenfolge wie die Seiten in dieser Datei definiert sind, werden sie auch im Jupyter-Book umgesetzt.

Zum einfügen einer neuen Seite,

```
- file: FILENAME
```

an das Ende hinzufügen. Dateiendungen (.md oder .ipynb) werden **weggelassen**.

### Inhalte selbst

Sollten im gleichen Ordner wie die \_toc.yml und \_config.yml Dateien sein und sind entweder Markdown-files oder Jupyter-Notebooks (.md oder .ipynb).

Der erste Header mit heading level 1 (eine Raute --> #) wird von Jupyter-Book als Überschrift der Seite interpretiert. Sowohl bei Markdown als auch bei Jupyter-Notebooks

## Bauen des Jupyter-Books

Der Befehl

```
jupyter-book build PATH/TO/BOOK
```

wird genutzt um das Buch zu bauen.

Weitere Informationen: https://jupyterbook.org/en/stable/start/build.html

Konkret im Falle von ShortPythonIntro soll sowohl die deutsche als auch die englische Version gebaut werden:

```
jupyter-book build .../ShortPythonIntro/src/de
jupyter-book build .../ShortPythonIntro/src/en
```

Als Argument erhält der Befehl, den Ordner wo der Inhalt als auch \_toc.yml und \_config.yml Dateien enthalten sind.
In diesem Fall als absoluter Pfad beginnend beim Root Directory.

Das Resultat des Bauens, sind die \_build Ordner `.../ShortPythonIntro/src/de/_build` bzw. `.../ShortPythonIntro/src/en/_build`.

Wenn man das Buch ein weiteres mal baut, werden nur die Seiten neue gebaut, wessen Quelldateien verändert wurden.
Dies macht das Bauen zwar schneller, jedoch können dadurch Fehler entstehen:

Jede Seite hat ein eigenes Inhaltsverzeichnis am linken Bildschirmrand.
Wenn eine neue Seite hinzugefügt wurde, wird das Inhaltsverzeichnis bei Seiten wo es keine Veränderung gab, nicht neu gebaut. Gleiches gilt auch für umbenennung, etc.
Dementsprechend ist auf diesen Seiten die neue Seite nicht im Inhaltsverzeichnis enthalten.

Daher empfehle ich besonders vor dem Pushen auf GitHub, die `_build` Ordner zu reinigen. Damit stellt man sicher, dass es keine Probleme mit dem Inhaltsvereichnis gibt. Fehlende Referenzen im \_toc.yml werden dann etwa mit einem Warning gekennzeichnet. 
Das kann man wie folgt machen:
```
jupyter-book clean .../ShortPythonIntro/src/de --all
jupyter-book clean .../ShortPythonIntro/src/en --all
```

## Das gebaute Jupyter-Book lokal öffnen

Um die Webseite lokal zu öffnen, muss man nur die "index.html" Datei im Ordner .../ShortPythonIntro/src/de/\_build/html im Webbrowser öffnen. So kann man gucken, ob alles so ist wie man es sich wünscht, bevor man die eigentliche GitHub Pages Seite ändert/die Änderungen nach GitHub pusht. Gleiches gilt für die Englische Version. Da die links, welche auf die jeweils andere Sprache verweisen, direkt die gewollten Links auf GitHub Pages öffnet, werden diese lokal ggf. nicht aktuell sein. Daher sichergehen, dass diese Links auch angepasst werden wenn man z.B. Dateinamen ändert. 

## Repository auf GitHub pushen
Änderungen an den Quelldateien sollen bitte gepusht werden. Die \_build Ordner werden vom .gitignore jeweils ignoriert und sollen nicht mitgepusht werden.

## GitHub Pages aktualisieren
Damit die Änderungen sichtbar werden, muss der `gh-pages` Branch aktualisiert werden. Dieser Branch wird automatisch als Quelle für GitHub Pages genutzt, womit das dann am Ende im Internet erreichbar ist.

Dafür muss der Inhalt von `.../ShortPythonIntro/src/de/\_build/html` von dem **main** Branch in den Ordner `.../ShortPythonIntro/de` auf den **gh-pages** Branch kopiert werden. Das gleiche gilt für `.../ShortPythonIntro/src/en/\_build/html` von dem **main** Branch zu `.../ShortPythonIntro/en` auf dem **gh-pages** Branch.

Zusätzlich wäre es gut einen Redirect einzurichten, da https://jensliebehenschel.github.io/ShortPythonIntro (weder .../de noch .../en) ungültig ist. Mit einem Redirect kann man sagen, dass man in dem Fall standardmäßig z.B. auf die englische Version kommt.

Der Redirect wäre eine index.html auf der gleichen Eben wie die Ordner `en/` und `de/` auf dem **gh-pages** branch. Der Inhalt der HTMl Datei wäre dieser (wenn standardmäßig auf die englische Version verwiesen werden soll):
```html
<meta http-equiv="refresh" content="0; URL=https://jensliebehenschel.github.io/ShortPythonIntro/en/" />
```

Hier die einzelnen Schritte:

Die zwei \_build/html Ordner irgendwo außerhalb des Repositories kopieren.

Branch wechseln
```
git checkout gh-pages
```

Die zwei \_build/html Ordner in `de/` bzw. `en/` auf dem gh-pages Branch kopieren.

Ggf. den Redirect einrichten (siehe oben)

Änderungen in Git hinzufügen, committen und pushen
```
git add .
git commit -m "Commit-Nachricht hier"
git push origin gh-pages
```

Wenn alles geklappt hat, sollten die Veränderungen in kürze auch auf der GitHub Pages Seite sichtbar werden.
Falls nicht, könnte es nützlich sein den Browser Cache für die Webseite zu leeren und die Seite zu aktualisieren.

