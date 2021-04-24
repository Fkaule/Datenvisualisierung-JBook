# Jupyter Book erstellen

[Offizielle JupyterBook Dokumentation](https://jupyterbook.org/intro.html)

**Installation + initiales Einrichten:**
1. `Jupyter Book` installieren mit `pip install -U jupyter-book` (Unter Windows10 funktioniet dies nur mit Python 3.7, deswegen benutze ich Ubuntu 20.04 welches einwandfrei mit der aktuellen Pythonversion funktioniert)
2. Verzeichnis erstellen (in diesem Beispiel `Datenvisualisierung`) und `_config.yml` und `_toc.yml` ins Verzeichnis kopieren (hier z.B. welche die ich verwende [_config.yml](_config.yml) / [_toc.yml](_toc.yml) )
3. Einstellungen in `_config.yml` bearbeiten
    - [Hinweise zu _config.yml von der offiziellen Webseite](https://jupyterbook.org/customize/config.html)
4. Inhaltsverzeichnis (Notebooks+Markdown Dateien) in `_config.yml` bearbeiten
    - [Hinweise zu _toc.yml von der offiziellen Webseite](https://jupyterbook.org/customize/toc.html)

**Jupyter Book erstellen**

5. Zum erstellen des Jupyter Books im übergeordneten Verzeichnis: `jupyter-book build Datenvisualisierung` (also über dem Verzeichnis "Datenvisualierung" welches im Punkt 2. erstellt wurde)
    - unter `_build/html/index.html` kann das JupyterBook nun lokal betrachtet werden

**Jupyter Book auf GitHub veröffentlichen**

**Inhalte dem `main` Branch hinzufügen (dort liegen z.B. nur die Jupyter Notebooks und nicht die html Seiten des JupyterBooks (das kommt im Punkt X))**

6. Auf Github ein Online repo erstellen
7. Anweisungen folgen unterhalb von **…or create a new repository on the command line**
8. Danach mit `git add filename` alle Dateien hochladen die zum bearbeiten verfügbar sein sollen (also vermutlich die JupyterNotebooks)

**JupterBook mit `ghp-import` dem Git repo unter dem Branch  `gh-pages`  hinzufügen (dort liegen die html Seiten des JupyterBooks)**

9. ghp-import installieren mit `pip install ghp-import` (das läuft auch wieder auf Windows10)
10. `ghp-import -n -p -f _build/html` im Arbeitsverzeichnis (also hier im Ordner Datenvisualisierung) ausführen
    - Dadurch werden die Inhalte des JupyterBooks automatisch in den Branch `gh-pages` des Git-repo hochgeladen
11. Auf Github in den Einstellungen des Repo den Branch `gh-pages` als Standard setzen
12. Unter `https://<user>.github.io/<myonlinebook>/` ist das Jupyter Book nun abrufbar
    
**Für Änderungen**
- neue Jupyter Notebooks (oder Markdown Files) in `_toc.yml` eintragen
- mit `jupyter-book build Datenvisualisierung` Jupyter Book erstellen (ggf. vorher lokal prüfen ob alles stimmt)
- mit `ghp-import -n -p -f _build/html` das JupyterBook auf Github pushen
- lokal können die Dateien wenn gewünscht auch dem main branch hinzugefügt und gepushed werden (wenn gewollt)