# Daten haendisch eingeben


# Vorlauf zum Datenerzeugen

### Federkonstanten

c1 = 0.55 # N/mm
c2 = 0.6 # N/mmh
c3 = 0.9 # N/mm

### Daten erzeugen

import numpy as np

#Weg
Weglaenge = 10 # mm
Wegschritt = 2.5 # mm
Weg = np.arange(0, Weglaenge+Wegschritt, Wegschritt)
Weg

#Kraft
mu, sigma = 0, 0.1 # Mittelwert und Standardabweichung für Rauschen
Kraft = np.linspace(0, Weglaenge*c1, int(Weglaenge/Wegschritt)+1)

#Messung 1
noise = np.random.normal(mu, sigma, int(Weglaenge/Wegschritt)+1)
Kraftmessung1 = Kraft + noise
Kraftmessung1[0] = 0 # ersten Wert Null setzen
Kraftmessung1 = np.around(Kraftmessung1, 1) # Werte runden
Kraftmessung1

#Messung 2
noise = np.random.normal(mu, sigma, int(Weglaenge/Wegschritt)+1)
Kraftmessung2 = Kraft + noise
Kraftmessung2[0] = 0 # ersten Wert Null setzen
Kraftmessung2 = np.around(Kraftmessung2, 1) # Werte runden
Kraftmessung2

# Eine Messung plotten

### Bibliotheken Import und Daten haendisch eingeben

- Einladen der `Matplotlib` Bibliothek
- Daten als Liste einlesen

# Bilbiothek importieren
from matplotlib import pyplot as plt

# Daten eingeben
Weg = [ 0 ,  2.5,  5 ,  7.5, 10 ]
Kraftmessung1 = [0. , 1.3, 2.8, 4.1, 5.5]



### Erster Plot

# Plotten
plt.plot(Weg, Kraftmessung1);

print("test2")

### Beschriftung hinzufügen

#Beschriftung
plt.xlabel("Weg [mm]") 
plt.ylabel("Kraft [N]")
plt.title("Erste Messung von Feder 1")
plt.plot(Weg, Kraftmessung1);

### Gitter / Linie mit Punkten / Beginn x/y-Achse

#Beschriftung
plt.xlabel("Weg [mm]")
plt.ylabel("Kraft [N]")
plt.title("Erste Messung von Feder 1")

#Gitter + Linienanpassung
plt.grid()
plt.plot(Weg, Kraftmessung1,"o-"); #Linie mit Markierungen

#Änderung des Anzeigebereichs muss nach dem plotten erfolgen
plt.ylim(bottom=0) # y-Achse soll ganz unten beginnen
plt.xlim(left=0) # x-Achse soll ganz links beginnen



### Bildgröße und Schriftgroesse

#Bildgroesse (muss zuerst kommen)
plt.figure(figsize=(8,5)) # Größe in inces (Default: 6,4)

#Schriftgroesse
plt.rcParams.update({'font.size': 20}) 

#Beschriftung
plt.xlabel("Weg [mm]")
plt.ylabel("Kraft [N]")
plt.title("Erste Messung von Feder 1")

#Gitter + Linienanpassung
plt.grid()
plt.plot(Weg, Kraftmessung1,"o-") #Linie mit Markierungen

#Änderung des Anzeigebereichs muss nach dem plotten erfolgen
plt.ylim(bottom=0) # y-Achse soll ganz unten beginnen
plt.xlim(left=0) # x-Achse soll ganz links beginnen

### Bild speichern

#Bildgroesse (muss zuerst kommen)
plt.figure(figsize=(8,5)) # Größe in inces (Default: 6,4)

#Schriftgroesse
plt.rcParams.update({'font.size': 20}) 

#Beschriftung
plt.xlabel("Weg [mm]")
plt.ylabel("Kraft [N]")
plt.title("Erste Messung von Feder 1")

#Gitter + Linienanpassung
plt.grid()
plt.plot(Weg, Kraftmessung1,"o-") #Linie mit Markierungen

#Änderung des Anzeigebereichs muss nach dem plotten erfolgen
plt.ylim(bottom=0) # y-Achse soll ganz unten beginnen
plt.xlim(left=0) # x-Achse soll ganz links beginnen

plt.savefig('01-Messung1_Feder1.png')

Wird die png wie in unserem Beispiel beschnitten, weil z.B. wie in unserem Fall die Schriftgröße verändert wurde, so kann über den Parameter `bbox_inches='tight'` dies behoben werden 

#Bildgroesse (muss zuerst kommen)
plt.figure(figsize=(8,5)) # Größe in inces (Default: 6,4)

#Schriftgroesse
plt.rcParams.update({'font.size': 20}) 

#Beschriftung
plt.xlabel("Weg [mm]")
plt.ylabel("Kraft [N]")
plt.title("Erste Messung von Feder 1")

#Gitter + Linienanpassung
plt.grid()
plt.plot(Weg, Kraftmessung1,"o-") #Linie mit Markierungen

#Änderung des Anzeigebereichs muss nach dem plotten erfolgen
plt.ylim(bottom=0) # y-Achse soll ganz unten beginnen
plt.xlim(left=0) # x-Achse soll ganz links beginnen

plt.savefig('01-Messung1_Feder1_tight.png', bbox_inches='tight')

Weiterhin kann durch die Änderung der Endung auch als svg gespeichert werden

#Bildgroesse (muss zuerst kommen)
plt.figure(figsize=(8,5)) # Größe in inces (Default: 6,4)

#Schriftgroesse
plt.rcParams.update({'font.size': 20}) 

#Beschriftung
plt.xlabel("Weg [mm]")
plt.ylabel("Kraft [N]")
plt.title("Erste Messung von Feder 1")

#Gitter + Linienanpassung
plt.grid()
plt.plot(Weg, Kraftmessung1,"o-") #Linie mit Markierungen

#Änderung des Anzeigebereichs muss nach dem plotten erfolgen
plt.ylim(bottom=0) # y-Achse soll ganz unten beginnen
plt.xlim(left=0) # x-Achse soll ganz links beginnen

plt.savefig('01-Messung1_Feder1_tight.svg', bbox_inches='tight')

Zuletzt empfiehlt es sich noch die dpi Anzahl auf 200 zu erhöhen um die Bildqualität zu verbessern. Dies geschieht mit der Option `dpi=200` im Befehl `savefig`

#Bildgroesse (muss zuerst kommen)
plt.figure(figsize=(8,5)) # Größe in inces (Default: 6,4)

#Schriftgroesse
plt.rcParams.update({'font.size': 20}) 

#Beschriftung
plt.xlabel("Weg [mm]")
plt.ylabel("Kraft [N]")
plt.title("Erste Messung von Feder 1")

#Gitter + Linienanpassung
plt.grid()
plt.plot(Weg, Kraftmessung1,"o-") #Linie mit Markierungen

#Änderung des Anzeigebereichs muss nach dem plotten erfolgen
plt.ylim(bottom=0) # y-Achse soll ganz unten beginnen
plt.xlim(left=0) # x-Achse soll ganz links beginnen

plt.savefig('01-Messung1_Feder1_tight_200dpi.png', bbox_inches='tight', dpi=200)

# zwei Messungen plotten

**Hinweis**: Den Import der Matplotlib Bibliothek sowie die Daten sind in Jupyter Notebook bereits hinterlegt, wenn Sie diese vorher bereits aufgerufen haben. Damit die Skripte aber auch alleine ohne die vorherigen Zellen funktionieren wurde dies hier hinzugefügt.

# Bilbiothek importieren
from matplotlib import pyplot as plt

# Daten eingeben
Weg = [ 0 ,  2.5,  5 ,  7.5, 10 ]
Kraftmessung1 = [0. , 1.3, 2.8, 4.1, 5.5]
Kraftmessung2 = [0. , 1.3, 2.6, 4.2, 5.7]

#Bildgroesse (muss zuerst kommen)
plt.figure(figsize=(8,5)) # Größe in inces (Default: 6,4)

#Schriftgroesse
plt.rcParams.update({'font.size': 20}) 

#Beschriftung
plt.xlabel("Weg [mm]")
plt.ylabel("Kraft [N]")
plt.title("Erste und zweite Messung von Feder 1")

#Plots
plt.grid()
plt.plot(Weg, Kraftmessung1,"o-", label="1. Messung") #Plot 1. Messung mit Label für Legende
plt.plot(Weg, Kraftmessung2,"x-", label="2. Messung") #Plot 2. Messung mit Label für Legende
plt.legend() # muss nach plot kommen


#Änderung des Anzeigebereichs muss nach dem plotten erfolgen
plt.ylim(bottom=0) # y-Achse soll ganz unten beginnen
plt.xlim(left=0) # x-Achse soll ganz links beginnen

plt.savefig('02-Messung1-2_Feder1.png', bbox_inches='tight', dpi=200)


Anpassung Linienfarbe und Linienbreite und Symbolgröße

# Bilbiothek importieren
from matplotlib import pyplot as plt

# Daten eingeben
Weg = [ 0 ,  2.5,  5 ,  7.5, 10 ]
Kraftmessung1 = [0. , 1.3, 2.8, 4.1, 5.5]
Kraftmessung2 = [0. , 1.3, 2.6, 4.2, 5.7]

#Bildgroesse (muss zuerst kommen)
plt.figure(figsize=(8,5)) # Größe in inces (Default: 6,4)

#Schriftgroesse
plt.rcParams.update({'font.size': 20}) 

#Beschriftung
plt.xlabel("Weg [mm]")
plt.ylabel("Kraft [N]")
plt.title("Erste und zweite Messung von Feder 1")

#Plots
plt.grid()
plt.plot(Weg, Kraftmessung1, marker="o", label="1. Messung", ls="-", lw=3, c="r", ms=10) #Plot 1. Messung mit Label für Legende
plt.plot(Weg, Kraftmessung2, marker="s", label="2. Messung", ls="-", lw=3, c="b", ms=10) #Plot 2. Messung mit Label für Legende
plt.legend() # muss nach plot kommen


#Änderung des Anzeigebereichs muss nach dem plotten erfolgen
plt.ylim(bottom=0) # y-Achse soll ganz unten beginnen
plt.xlim(left=0) # x-Achse soll ganz links beginnen

plt.savefig('02-Messung1-2_Feder1_Linienanpassung.png', bbox_inches='tight', dpi=200)


Als nächstes verwenden wir die Kurzform die Markertyp, Linientyp und Farbe zusammenfasst

# Bilbiothek importieren
from matplotlib import pyplot as plt

# Daten eingeben
Weg = [ 0 ,  2.5,  5 ,  7.5, 10 ]
Kraftmessung1 = [0. , 1.3, 2.8, 4.1, 5.5]
Kraftmessung2 = [0. , 1.3, 2.6, 4.2, 5.7]

#Bildgroesse (muss zuerst kommen)
plt.figure(figsize=(8,5)) # Größe in inces (Default: 6,4)

#Schriftgroesse
plt.rcParams.update({'font.size': 20}) 

#Beschriftung
plt.xlabel("Weg [mm]")
plt.ylabel("Kraft [N]")
plt.title("Erste und zweite Messung von Feder 1")

#Plots
plt.grid()
plt.plot(Weg, Kraftmessung1, "o-r", label="1. Messung", lw=3, ms=10) #Plot 1. Messung mit Label für Legende
plt.plot(Weg, Kraftmessung2, "s-b", label="2. Messung", lw=3, ms=10) #Plot 2. Messung mit Label für Legende
plt.legend() # muss nach plot kommen


#Änderung des Anzeigebereichs muss nach dem plotten erfolgen
plt.ylim(bottom=0) # y-Achse soll ganz unten beginnen
plt.xlim(left=0) # x-Achse soll ganz links beginnen

plt.savefig('02-Messung1-2_Feder1_Linienanpassung.png', bbox_inches='tight', dpi=200)


# Messung und Funktion plotten

# Bilbiothek importieren
from matplotlib import pyplot as plt
import numpy as np

# Daten eingeben
Weg = [ 0 ,  2.5,  5 ,  7.5, 10 ]
Kraftmessung1 = [0. , 1.3, 2.8, 4.1, 5.5]

# Funktion
c = 0.55 # N/mm
s = np.linspace(0,10,100) # 100 Datenpunkte im Bereich von 0 bis 10
F = c * s

#Bildgroesse (muss zuerst kommen)
plt.figure(figsize=(8,5)) # Größe in inces (Default: 6,4)

#Schriftgroesse
plt.rcParams.update({'font.size': 20}) 

#Beschriftung
plt.xlabel("Weg [mm]")
plt.ylabel("Kraft [N]")
plt.title("Erste und Messung von erwartete Steifigkeit von Feder 1", fontsize = 16)

#Plots
plt.grid()
plt.plot(Weg, Kraftmessung1, "or", label="1. Messung", lw=3, ms=10, zorder=2) #Plot 1. Messung mit Label für Legende
plt.plot(s, F, "-b", label="erwartete Steifigkeit", lw=3, ms=10, zorder=1) #Plot Funktion
plt.legend() # muss nach plot kommen

#Änderung des Anzeigebereichs muss nach dem plotten erfolgen
plt.ylim(bottom=0) # y-Achse soll ganz unten beginnen
plt.xlim(left=0) # x-Achse soll ganz links beginnen

plt.savefig('03-Messung1-Funktion_Feder1.png', bbox_inches='tight', dpi=200)


