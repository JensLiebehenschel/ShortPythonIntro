Dies ist die Anleitung für das Bauen (oder Verändern) eines Jupyter-Books.
Ich habe ausschließlich unter Linux gearbeitet und weiß dementsprechend nicht wie oder ob man überhaupt unter z.B. Windows mit Jupyter-Books arbeitet.
Ich entschuldige mich, falls es zu Problemen führt.
Es folgen die benötigten Befehle in der Kommandozeile.

Alle Pfade, welche für Nutzer individuell sind, werden mit "..." markiert. Ich benutzte für die Beispiele absolute Pfade. Man kann auch relative Pfade nutzen, dann muss man jedoch aufpassen, welcher Ordner momentan als Working Directory gesetzt ist.

## Installieren von Jupyter-Book

```
pip install -U jupyter-book
```file:///home/edward/job/CommitFolder/Anleitung.md

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

## Bauen des Jupyter-Books

Der Befehl

```
jupyter-book build PATH/TO/BOOK
```

wird genutzt um das Buch zu bauen.

Weitere Informationen: https://jupyterbook.org/en/stable/start/build.html

Konkret im Falle von ShortPythonIntro:

```
jupyter-book build /home/<...>/ShortPythonIntro/
```

Als Argument erhält der Befehl, den Ordner wo der Inhalt als auch \_toc.yml und \_config.yml Dateien enthalten sind.
In diesem Fall als absoluter Pfad beginnend beim Root Directory.

Das Resultat des Bauens, ist der \_build Ordner, welcher sich im ShortPythonIntro Ordner befindet.

Wenn man das Buch ein weiteres mal baut, werden nur die Seiten neue gebaut, wessen source dateien verändert wurden.
Dies macht das Bauen zwar schneller, jedoch können dadurch Fehler entstehen:

Jede Seite hat ein eigenes Inhaltsverzeichnis am linken Bildschirmrand.
Wenn eine neue Seite hinzugefügt wurde, wird das Inhaltsverzeichnis bei Seiten wo es keine Veränderung gab, nicht neu gebaut.
Dementsprechend ist auf diesen Seiten die neue Seite nicht im Inhaltsverzeichnis enthalten.

Daher empfehle ich, vor dem pushen auf GitHub, dass man den \_build Ordner vollständig löscht und das Jupyter-Book nochmal baut. 
Somit wird die Seite von Anfang an gebaut und solche Fehler im Inhaltsverzeichnis sind behoben.


## Das gebaute Jupyter-Book lokal öffnen

Um die Webseite im Localhost zu öffnen, muss man nur die "index.html" Datei im Ordner ShortPythonIntro/\_build/html im Webbrowser öffnen. So kann man gucken, ob alles so ist wie man es sich wünscht, bevor man die eigentliche GitHub Pages Seite ändert/die Änderungen nach GitHub pusht.

## Die "&lt;!-- Google Analytics --&gt;" Kommentare entfernen

Bei &lt;!-- Google Analytics --&gt; handelt es sich um einen Kommentar in HTML. Diese Zeilen haben keine Bedeutung. Diese werden lediglich generiert um den generierten Code zu strukturieren und mit diesem Kommentar hinzuweisen, ab wo der Code für Google Analytics beginnt. Google Analytics ist jedoch deaktiviert und deshalb wird kein Code dazu generiert. Der Kommentar wird leider trotzdem generiert. Um alle Kommentare zu entfernen, kann man eine neue Datei mit der Endung ".sh" erstellen und folgendes Shell-Script einfügen:

```sh
#!/usr/bin/bash

regex="\w*\.html"
for file in $(find /home/.../ShortPythonIntro/_build/html -type f)
do
	if [[ "$file" =~ "$regex" ]]; then
		echo "$file"
		sed -i '/<!-- Google Analytics -->/d' "$file"
	fi
done
```

Je nachdem, welcher Shell Interpreter genutzt wird, muss die erste Zeile gegebenenfalls durch

```
#!/usr/bin/zsh
```
ersetzt werden, wenn man z.B. zsh als Shell Interpreter anstelle von Bash nutzt. (Die meisten nutzen Bash)

Nun führt man das Shell-Script mit 

```
./SKRIPTNAME.sh
```

aus. Eventuell muss man es erst exectuable machen. Entweder per GUI auf die Datei gehen und "ausführbar" akreuzen. 
Alternativ kann man die Privilegien auch durch den den Befehl 

```
chmod 777 SKRIPTNAME.sh
```

erteilen.

Dieses Shell-Script entfernt automatisch den Google Analytics Kommentar in allen HTML Dateien und gibt zur Kontrolle, die Namen aller HTML Dateien in der Konsole aus.


## Veränderungen auf der GitHub Pages sichtbar machen

Damit die Änderungen auf GitHub Pages ankommen, benutzt man das Kommandozeilentool <code>ghp-import</code>

Hier mehr Info: https://jupyterbook.org/en/stable/publish/gh-pages.html

## Repository auf GitHub pushen
Man setzt das Working Directory als den Ordner wo README.md, Potentiell_hinzufuegbar.md, usw. enthalten sind. Also den Ordner **über** dem ShortPythonIntro Ordner.

Dann führt man

```
git init
```

aus und fügt das Repository in Git hinzu:

```
git remote add origin https://github.com/JensLiebehenschel/ShortPythonIntro.git

```
Vor einigen Jahren hieß der Defaultbranch in Git "master". Nun wurde er jedoch zu "main" umgenannt.
Wahrscheinlich benutzt das Git System im Terminal immernoch master als Defaultbranch.
Das sollte mit diesem Befehl geändert werden können.
```
git config --global init.defaultBranch main
```

nun macht fügt man hinzu, welche Dateien betrachtet werden können und committed die Veränderungen. Beides ist auch in einem Befehl möglich.

```
git commit -am 'Commitnachricht hier'    
```
auf GitHub pushen:

```
git push origin main    
```

Den oberen Link erhält man auf der GitHub Seite des Repositories, wenn man auf Code geht und den HTTPS Link kopiert



### ghp-import installieren

```
pip install ghp-import
```

### Den Befehl nutzen

Mit dem Befehl werden die Ergebnisse auf den "gh-pages" Branch gepusht, womit GitHub Pages die aktuellste Version bekommt.
Der gh-pages Branch wird beim aufrufen dieses Befehls überschrieben. Es sollte also nicht manuell auf dem gh-pages branch gearbeitet werden.

Man muss sehr wahrscheinlich davor Git sagen, welches Repository genutzt werden soll.
Also muss man zumindest <code>git remote add origin</code> ausführen. (Beschrieben im Kapitel darüber.)

```
ghp-import -n -p -f /home/.../ShortPythonIntro/_build/html
```

Daraufhin wird man nach GitHub Benutzername und einem Access Token gefragt.

Git fragt hier zwar nach einem Passwort, jedoch darf man hier kein Passwort angeben. In dem Fall kriegt man eine Benachrichtigung:

```
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
```

in anderen Worten: Man darf seit 2021, keine Passwörter zur Authentifizierung mehr nutzen.
Deshalb benötigt man einen sogenannten Access Token. Falls nicht vorhanden, muss dieser auf GitHub generiert werden.

Einen Token generiert man in den Einstellungen. Diese URL (https://github.com/settings/tokens) sollte die korrekte Seite in den Einstellungen öffnen. Alternativ:

Oben auf das Profilbild klicken --> Settings --> Developer Settings --> Tokens (classic)

Dort geht man auf "Generate new token" und gibt u.a an wie lange der Token gültig sein soll.

Den generierten Token gibt man nun statt dem Passwort an, wenn man wieder <code>ghp-import</code> ausführt.

Wenn alles geklappt hat, sollte die Veränderungen in kürze auch auf der GitHub Pages Seite sichtbar werden.
Falls nicht, könnte es nützlich sein den Browser Cache für diese Webseite zu leeren und die Seite zu aktualisieren.
