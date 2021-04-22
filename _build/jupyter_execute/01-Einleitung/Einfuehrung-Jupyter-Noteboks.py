# Einführung in Jupyter Notebooks

## Ausführen von Zellen und deren Reihenfolge

Klicken Sie in die darunterliegende Zeile und drücken Sie `Shift` + `Enter` um diese auszuführen

1+1

Sie haben nun eine Zelle ausgeführt. Sie können auch den `Pfeil` oben benutzen **um eine Zelle auszuführen**

Neben der Zelle steht in eckigen Klammern die Nummer die angibt in welcher Reihenfolge die Zellen ausgeführt wurden. Die Reihenfolge ist wichtig, weil diese bestimmt wie die Daten in den Speicher gelesen werden.

Führen Sie dazu die drei nachfolgenden Zeilen aus:

i = 1

i = 2

print(i)

Da die Definition mit i=2 zuletzt gegeben wurde, wird nun durch print(i) auch der letzte Wert ausgegeben

## neue Zelle hinzufügen

Drücken Sie das `+` Symbol um eine neue Zeile hinzuzufügen

klicken Sie links neben den Zeileinput (da wo In []: steht) so das diese `blau` markiert ist und drücken Sie dann `a` (insert **`a`**bove = fügt **darüber** eine Zeile ein)

klicken Sie links neben den Zeileinput (da wo In []: steht) so das diese `blau` markiert ist und drücken Sie dann `b` (insert **`b`**elow = fügt **darunter** eine Zeile ein)

## Zelle löschen

Durch das markieren der Zelle und das drücken von `d` + `d` wird die Zelle gelöscht

Lösch mich !

## Textfeld formatieren (Markdown Syntax)

[Jupyter Notebook Markdown Syntax](https://sourceforge.net/p/jupiter/wiki/markdown_syntax/)

klicken Sie links neben den Zeileinput (da wo In []: steht) so das diese `blau` markiert ist und drücken Sie dann `m`. Alternativ können Sie nach dem markieren der Zelle auch oben (wo `Code` steht) den Typ `Markdown` auswählen.

Sie haben nun eine Zelle erstellt in der Sie den `Markdown` Syntax verwenden können:

Durch das Ausführen der Zelle (`Shift` + `Enter`) wird der Text dann angezeigt

**Überschriften**: (alternativ können Sie die markierte Zelle durch drücken der Tasten `1` , `2` oder `3` eine Überschriftsebene erstellen):

`# Überschrift 1. Test` 

`## Überschrift 1. Test`

`### Überschrift 1. Test`




**Textformatierung**: 

`* Kursiv *` * Kursiv * 

`** Fett **` ** Fett ** 

`*** Fett+Kursiv ***` *** Fett+Kursiv *** 





**Nummerierung + Listen**: 

`- Liste `

`- Liste `

- Liste
- Liste


`1. Nummerierung `

`2. Nummerierung`

1. Nummerierung
2. Nummerierung

`[ ] Checkbox` [ ] Checkbox

`[x] Checkbox` [x] Checkbox





**Tabellen**
```
First Header  | Second Header`
  ------------- | -------------`
  Content Cell  | Content Cell`
  Content Cell  | Content Cell`
```


  First Header  | Second Header
  ------------- | -------------
  Content Cell  | Content Cell
  Content Cell  | Content Cell



** Bilder ** 

`![Alternativtext](https://jupyter.org/assets/nav_logo.svg)`

![Alternativtext](https://jupyter.org/assets/nav_logo.svg)





** Links **

`[HTWK Leipzig](http://www.htwk-leipzig.de)`

[HTWK Leipzig](http://www.htwk-leipzig.de)


```
Das ist ein Beispieltext mit Referenzen[Ref1][1] . Das ist ein Beispieltext mit Referenzen [Ref1][2].
Die Links können dann darunter stehen

   [1]: http://www.jupyter.org
   [2]: http://www.htwk-leipzig.de
```

Das ist ein Beispieltext mit Referenzen[Ref1][1] . Das ist ein Beispieltext mit Referenzen [Ref1][2].
Die Links können dann darunter stehen

   [1]: http://www.jupyter.org
   [2]: http://www.htwk-leipzig.de




**Code**: 

```
Ein Codeelement mit dem Einschluss von Anführungszeichen: also so `Code` dargestellt werden

```

Ein `Codeelement` der Rest ist Text


```
Mehrere Codezeilen werden durch drei Anführungszeichen zu Beginn und drei zum Ende definiert
```

 

