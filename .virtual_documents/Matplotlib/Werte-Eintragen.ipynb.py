# Bilbiothek importieren
from matplotlib import pyplot as plt

# Daten eingeben
Weg = [ 0 ,  2.5,  5 ,  7.5, 10 ]
Kraftmessung1 = [0. , 1.3, 2.8, 4.1, 5.5]




# Plotten
plt.plot(Weg, Kraftmessung1);


#Beschriftung
plt.xlabel("Weg [mm]") 
plt.ylabel("Kraft [N]")
plt.title("Erste Messung von Feder 1")
plt.plot(Weg, Kraftmessung1);


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

