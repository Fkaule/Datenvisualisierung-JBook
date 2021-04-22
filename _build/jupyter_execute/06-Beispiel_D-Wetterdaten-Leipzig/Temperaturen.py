# Einlesen der Wetterdaten vom DWD
Leipzig: https://www.dwd.de/DE/leistungen/klimadatendeutschland/klarchivtagmonat.html;jsessionid=2BEE8FAF8E83A9A4984BE516FA2EFE0C.live21073?nn=16102

- historische Daten (`produkt_klima_tag_19340101_20181231_02932.txt`) (von **01.01.1934** bis **31.12.2018**)
- aktuelle Daten (`produkt_klima_tag_19340101_20181231_02932.txt`) (von **19.07.2019** bis **heute**)

- **Daten fehlen von 01.01.2019 bis 18.07.2019**

# Bibliotheken
import pandas as pd

## historische Wetterdaten einlesen

### Daten einlesen

data_hist = pd.read_csv("produkt_klima_tag_19340101_20181231_02932.txt", sep=";")
data_hist

#### Spaltenbedeutung 
aus `Metadaten_Parameter_klima_tag_02932.txt`

- TGK;Minimum der Lufttemperatur am Erdboden in 5cm Hoehe;°C
- TMK;Tagesmittel der Temperatur;°C
- TXK;Tagesmaximum der Lufttemperatur in 2m Höhe;°C


# Daten aufbereiten

## Aufgabe 1: benötigte Spalten rausziehen 

data_hist.columns

data_hist = data_hist.loc[:,("MESS_DATUM"," TMK")]
data_hist

## Aufgabe 2: aus Datumsspalte Jahr/Monat/Tag rausziehen

data_hist.info()

`MESS_DATUM` ist `int64` . Es gibt aber auch ein Typ `datetime` der einige Vorteile hat:
1. Datum/Uhrzeit wird meistens automatisch erkannt
2. Aus diesem Format können wir dann einzellene Komponenten (wie Monat oder Jahr) einfach extrahieren

data_hist['Datum'] = pd.to_datetime(data_hist['MESS_DATUM'],format='%Y%m%d')
data_hist.info()

data_hist.sample(10)

data_hist["Jahr"] = pd.DatetimeIndex(data_hist['Datum']).year
data_hist["Monat"] = pd.DatetimeIndex(data_hist['Datum']).month
data_hist["Tag"] = pd.DatetimeIndex(data_hist['Datum']).day
data_hist

## Aufgabe 3: Spalten umbennen und unbenötigte Spalten löschen

data_hist = data_hist.drop(["MESS_DATUM"],axis=1)

data_hist

data_hist.rename(columns={" TMK":"Tagesmitteltemperatur [°C]"}, inplace=True)
data_hist


## Aktuelle Werte einlesen (ab 2019)

### Datenaufbereitung analog `data_hist`

# Einlesen
data_aktuell = pd.read_csv("produkt_klima_tag_20190719_20210118_02932.txt", sep=";")

# Spalten rausziehen
data_aktuell = data_aktuell.loc[:,("MESS_DATUM"," TMK")]

# Datumspalte in Datumsformat ändern
data_aktuell['Datum'] = pd.to_datetime(data_aktuell['MESS_DATUM'],format='%Y%m%d')

# Spalten für Jahr Monat und Tag hinzufuegen
data_aktuell["Jahr"] = pd.DatetimeIndex(data_aktuell['Datum']).year
data_aktuell["Monat"] = pd.DatetimeIndex(data_aktuell['Datum']).month
data_aktuell["Tag"] = pd.DatetimeIndex(data_aktuell['Datum']).day

# alte Datumsspalte entfernen
data_aktuell = data_aktuell.drop(["MESS_DATUM"],axis=1)

# Temperaturspalte umbennnen
data_aktuell.rename(columns={" TMK":"Tagesmitteltemperatur [°C]"}, inplace=True)

data_aktuell

## Historische und aktuelle Daten zusammenfuegen

df = pd.concat([data_hist, data_aktuell])
df

### Aufgabe 1:  fehlerhafte Daten aussortieren

Einige Werten erscheinen als -999 und sind somit fehlerhaft. Diese wollen wir aussortieren

df.describe()

df.sort_values(by=["Tagesmitteltemperatur [°C]"]).head(10)

# rausfiltern
df = df.loc[df["Tagesmitteltemperatur [°C]"] > -999]

# pruefen
df.sort_values(by=["Tagesmitteltemperatur [°C]"]).head(20)

### Aufgabe 2: Anzahl der Einträge pro Jahr sichtbar machen 

Mit `.unqiue()` können wir die verschiedenen Einträge sichtbar machen

df["Jahr"].unique()

mit `value_counts()` können wir die Einträge pro Jahr zählen

df["Jahr"].value_counts()

Der einfachste Weg es grafisch sichtbar zu machen ist den `Seaborn` `countplot` zu verwenden

import seaborn as sns
sns.set(rc={'figure.figsize':(10,25)})
sns.countplot(data=df, y="Jahr")


### Aufgabe 3: fehlende Jahre sichtbar machen

Um die fehlenden Jahre sichtbar zu machen fügen wir einen neuen DataFrame ein mit allen Jahreszahlen und fügen den dann mit dem alten DataFrame zusammen

import numpy as np 
Jahre = np.linspace(1934,2021,2021-1934+1)
df_Jahre = pd.DataFrame(Jahre, dtype="int") # als Integer eingefügt, da andere Jahreszahlen auch integer sind
df_Jahre.columns=["Jahr"]
df_Jahre.info()

# neuen dataframe aus alten kopieren 
df_test = df
df_test.info()

# in Schleife abfragen ob Jahr vorhanden, wenn Zeile leer ist Jahr hinzufuegen
count = 0
for i in Jahre:
    if df_test.loc[df_test["Jahr"]==i].empty:
        print(int(i))
        count=count+1
        df_test = df_test.append({'Jahr': int(i)},ignore_index=True,sort=True)

print("Es wurden "+str(count)+" Jahre hinzugefuegt")

df_test.info()

Aus den Spalten mit integer sind nun float geworden, dies änder wir zurück

df_test["Jahr"] = df_test["Jahr"].astype(int)

import seaborn as sns
sns.set(rc={'figure.figsize':(10,25)})
sns.countplot(data=df_test, y="Jahr")

### Aufgabe 4:  Aussortieren von Jahren mit zu wenigen Werten

Diese würden sonst keinen richtigen Jahresmittelwert ergeben

df_2 = df.groupby(by=["Jahr"]).filter(lambda x: len(x) > 360)
import seaborn as sns
sns.set(rc={'figure.figsize':(10,25)})
sns.countplot(data=df_2, y="Jahr")

### Aufgabe 4: Daten als csv exportieren (Zwischenspeichern)

df_2.to_csv("Leipzig_Tageswerte_volle_Jahre.csv",index=False)

# Plot 1: Mittelwert über die Jahre plotten

## Mittelwerte bestimmen

Jahresmittelwerte = df_2.groupby(by=["Jahr"]).mean().reset_index()
Jahresmittelwerte

## Spalte umbennnen

Jahresmittelwerte.rename(columns={"Tagesmitteltemperatur [°C]":"Jahresmitteltemperatur [°C]"},inplace=True)
Jahresmittelwerte

## nicht benötigte Spalten entfernen
da wir mit `.groupby()` und `.mean()`den Mittelwert aller Spalten bestimmt haben, schmeißen wir nun die Spalten `Monat` und `Tag` raus, da diese keine Sinn ergeben

Jahresmittelwerte.drop(["Monat","Tag"],axis=1,inplace=True)
Jahresmittelwerte

## Daten als csv exportieren

Jahresmittelwerte.to_csv("Leipzig_Jahreswerte_volle_Jahre.csv",index=False)

## die 10 Jahre mit den höchsten Mittelwerten anzeigen

Jahresmittelwerte.sort_values(by=["Jahresmitteltemperatur [°C]"],ascending=False).head(10)

# Plot 1a: Jahresmittelwerte absolut

# import
import matplotlib.pyplot as plt

# Mittelwerte bestimmen

plt.figure(figsize=(10,4))
plt.ylabel("Jahresmitteltemperatur [°C]")
plt.xlabel("Jahr")
plt.plot(Jahresmittelwerte["Jahr"],Jahresmittelwerte["Jahresmitteltemperatur [°C]"],marker="s",markersize=4)


# Plot 1b: Jahresmittelwerte absolut mit rollendem Mittelwert

## Rollenden Mittelwert hinzufügen

Jahresmittelwerte["Jahresmitteltemperatur_RM5 [°C]"] = Jahresmittelwerte["Jahresmitteltemperatur [°C]"].rolling(5).mean()
Jahresmittelwerte

## Plot

# import
import matplotlib.pyplot as plt

# Mittelwerte bestimmen

plt.figure(figsize=(10,4))
plt.ylabel("Jahresmitteltemperatur [°C]")
plt.xlabel("Jahr")
plt.plot(Jahresmittelwerte["Jahr"],Jahresmittelwerte["Jahresmitteltemperatur [°C]"],marker="s",markersize=4, label="Jahresmittel")
plt.plot(Jahresmittelwerte["Jahr"],Jahresmittelwerte["Jahresmitteltemperatur_RM5 [°C]"], lw=3, label="Glättung über 5 Jahre")
plt.legend()



# Plot 1c: Temperaturdifferenz mit rollendem Mittelwert

Um die Temperaturdifferenz zu bekommen, ziehen wir den Mittelwert über alle Jahre von den Jahreswerten ab

# Mittelwert bestimmen der abgezogen wird um Temperaturdifferenz zu bekommen
Mittelwert = Jahresmittelwerte["Jahresmitteltemperatur [°C]"].mean()

# import
import matplotlib.pyplot as plt

# Mittelwerte bestimmen

plt.figure(figsize=(10,4))
plt.ylabel("Jahresmitteltemperaturabweichung [°C]")
plt.xlabel("Jahr")
plt.title("DWD Daten Station: Halle/Leipzig")
plt.plot(Jahresmittelwerte["Jahr"],Jahresmittelwerte["Jahresmitteltemperatur [°C]"]-Mittelwert,marker="s",markersize=4, label="Jahresmittel Differenz")
plt.plot(Jahresmittelwerte["Jahr"],Jahresmittelwerte["Jahresmitteltemperatur_RM5 [°C]"]-Mittelwert, lw=3, label="Glättung über 5 Jahre")
plt.legend()



# Plot 1d: NASA Daten plotten

Wir wollen nur die NASA Daten (nur Landflächen) dazu plotten:
https://data.giss.nasa.gov/gistemp/graphs_v4/graph_data/Temperature_Anomalies_over_Land_and_over_Ocean/graph.csv

## Einlesen

# Daten einlesen
NASA = pd.read_csv("graph.csv", header=1)
NASA

***Anmerkung*** : Ich habe nicht rausgekriegt wie die Glättung der NASA Daten erfolgte. Den Weg den ich oben mit dem gleitenden Mittelwert verwendet habe ist es nicht

## Plot

# import
import matplotlib.pyplot as plt

# Mittelwerte bestimmen

plt.figure(figsize=(10,4))
plt.ylabel("Temperatur [°C]")
plt.ylabel("Jahresmitteltemperaturabweichung [°C]")
plt.title("NASA Daten")
plt.plot(NASA["Year"],NASA["Land_Annual"],lw=1, marker="s",markersize=4,c="salmon", label="Land Surface Air Temperature")
plt.plot(NASA["Year"],NASA["Lowess(5)"], lw=3, c="red", label="Land Lowess Smoothing")
plt.plot(NASA["Year"],NASA["Ocean_Annual"],lw=1, marker="s",markersize=4,c="skyblue", label="Sea Surface Water Temperature")
plt.plot(NASA["Year"],NASA["Lowess(5).1"], lw=3, c="blue", label="Sea Lowess Smoothing")
plt.legend()



# Plot 1d: Temperaturdifferenz mit rollendem Mittelwert + NASA Daten

Mittelwert = Jahresmittelwerte["Jahresmitteltemperatur [°C]"].mean()

# import
import matplotlib.pyplot as plt

# Mittelwerte bestimmen

plt.figure(figsize=(10,4))
plt.ylabel("Jahresmitteltemperaturabweichung [°C]")
plt.xlabel("Jahr")
plt.title("DWD Daten Station: Halle/Leipzig")
plt.plot(Jahresmittelwerte["Jahr"],Jahresmittelwerte["Jahresmitteltemperatur [°C]"]-Mittelwert,marker="s",markersize=4, label="Jahresmittel Differenz")
plt.plot(Jahresmittelwerte["Jahr"],Jahresmittelwerte["Jahresmitteltemperatur_RM5 [°C]"]-Mittelwert, lw=3, label="Glättung über 5 Jahre")
plt.plot(NASA["Year"],NASA["Lowess(5)"], lw=3, label="NASA Glättung (Landflächen)")
plt.legend()



# Plot 1e: Temperaturdifferenz mit Konfidenzintervalle (mit `Seaborn`) und rollendem Mittelwert

Bei der Darstellung mit dem Konfidenzintervall verwenden wir wieder den DataFrame mit den Tageswerten (df2)!

import seaborn as sns

sns.set(rc={'figure.figsize':(10,6)})


fig, ax = plt.subplots()

ax = sns.lineplot(x=df_2["Jahr"],y=df_2["Tagesmitteltemperatur [°C]"]-Mittelwert, label="Leipzig", color="royalblue")
ax.plot(Jahresmittelwerte["Jahr"],Jahresmittelwerte["Jahresmitteltemperatur_RM5 [°C]"]-Mittelwert, lw=2,color="red", label="Leipzig (Glättung 5 Jahre)")
ax.plot(NASA["Year"],NASA["Lowess(5)"], lw=2,ls="--",color="black", label="NASA Glättung (Landflächen)")
plt.ylabel("Jahresmitteltemperaturabweichung [°C]")
plt.legend(loc="upper left")


# Plot 2: Temperaturverlauf über die Monate

## Monatsmittelwerte bestimmen

Monatsmittelwerte = df_2.groupby(by=["Jahr","Monat"]).mean().reset_index()
Monatsmittelwerte


#### Spalten entfernen


Monatsmittelwerte.drop(["Tag"],axis=1,inplace=True)
Monatsmittelwerte

#### Spalte umbennen

Monatsmittelwerte.rename(columns={"Tagesmitteltemperatur [°C]":"Monatsmitteltemperatur [°C]"},inplace=True)
Monatsmittelwerte

#### Export als CSV

Monatsmittelwerte.to_csv("Leipzig_Monatswerte_volle_Jahre.csv",index=False)

## Plot 2a: Monatsverlauf mit allen Jahren farblich codiert `Seaborn`

import seaborn as sns
Anzahl_Jahre=Monatsmittelwerte["Jahr"].nunique()
sns.set(rc={'figure.figsize':(10,6)})
ax = sns.lineplot(x=Monatsmittelwerte["Monat"],y=Monatsmittelwerte["Monatsmitteltemperatur [°C]"], hue=Monatsmittelwerte["Jahr"], palette=sns.color_palette('coolwarm', n_colors=Anzahl_Jahre))

#Extra Schritt um Titel der Legende zu entfernen und neu zu setzen (taucht sonst als Eintrag mit auf)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles[1:], labels=labels[1:])
ax.legend(handles=handles[1:], labels=labels[1:], ncol=3,bbox_to_anchor=(1.0, 1.0), loc='upper left', title="Jahr")



# Plot 2b: Monatsverlauf mit Standardabweichung `Seaborn`

import seaborn as sns
sns.set(rc={'figure.figsize':(10,6)})
sns.lineplot(x=Monatsmittelwerte["Monat"],y=Monatsmittelwerte["Monatsmitteltemperatur [°C]"],ci="sd")

# Plot 2c: letzten 4 Jahre im Vergleich zum Monatsverlauf mit Standardabweichung `Seaborn` 

import seaborn as sns
import calendar
sns.set(rc={'figure.figsize':(12,8)})

# Monatswerte für jedes Jahr
Jahr2020=Monatsmittelwerte.loc[(Monatsmittelwerte["Jahr"]==2020)]
Jahr2018=Monatsmittelwerte.loc[(Monatsmittelwerte["Jahr"]==2018)]
Jahr2017=Monatsmittelwerte.loc[(Monatsmittelwerte["Jahr"]==2017)]
Jahr2016=Monatsmittelwerte.loc[(Monatsmittelwerte["Jahr"]==2016)]

# Funktion zum Darstellen der Min/Max Werte fuer ein Jahr
def print_min_max(df,ax):

    min=df["Monatsmitteltemperatur [°C]"].min().round(1)
    minMonat=df.loc[df["Monatsmitteltemperatur [°C]"].idxmin(),"Monat"]
    max=df["Monatsmitteltemperatur [°C]"].max().round(1)
    maxMonat=df.loc[df["Monatsmitteltemperatur [°C]"].idxmax(),"Monat"]
    
    Month_name_min=calendar.month_name[minMonat]
    Month_name_max=calendar.month_name[maxMonat]

    ax.text(4,1,"Min ("+Month_name_min+"):"+str(min)+"°C",color="gray", horizontalalignment='left')
    ax.text(4,-2,"Max ("+Month_name_max+"):"+str(max)+"°C",color="gray", horizontalalignment='left')
    return
    

# Figure mit 2 x 2 "subplots=ax" 
fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)

# Links oben : 2020
sns.lineplot(x=Monatsmittelwerte["Monat"],y=Monatsmittelwerte["Monatsmitteltemperatur [°C]"],ci="sd", ax=ax[0,0])
ax[0,0].plot(Jahr2020["Monat"],Jahr2020["Monatsmitteltemperatur [°C]"], color="red")
ax[0,0].set_title("2020")
print_min_max(Jahr2020,ax[0,0])

# Rechts oben : 2018
sns.lineplot(x=Monatsmittelwerte["Monat"],y=Monatsmittelwerte["Monatsmitteltemperatur [°C]"],ci="sd", ax=ax[0,1])
ax[0,1].plot(Jahr2018["Monat"],Jahr2018["Monatsmitteltemperatur [°C]"], color="red")
ax[0,1].set_title("2018")
print_min_max(Jahr2018,ax[0,1])

# Links unten : 2017
sns.lineplot(x=Monatsmittelwerte["Monat"],y=Monatsmittelwerte["Monatsmitteltemperatur [°C]"],ci="sd", ax=ax[1,0])
ax[1,0].plot(Jahr2017["Monat"],Jahr2017["Monatsmitteltemperatur [°C]"], color="red")
ax[1,0].set_title("2017")
print_min_max(Jahr2017,ax[1,0])

# Rechts unten : 2016
sns.lineplot(x=Monatsmittelwerte["Monat"],y=Monatsmittelwerte["Monatsmitteltemperatur [°C]"],ci="sd", ax=ax[1,1])
ax[1,1].plot(Jahr2016["Monat"],Jahr2016["Monatsmitteltemperatur [°C]"], color="red")
ax[1,1].set_title("2016")
print_min_max(Jahr2016,ax[1,1])


fig.tight_layout()

# Plot 3: Mittlere Jahrestemperatur im Vergleich zur minimalen Jahrestemperatur (Scatter mit `Seaborn`)

Wir wollen nun die Frage klären ob Jahre mit einer hohen Jahresdurchschnittstemperatur auch im Winter zu hohen Temperaturen führen

**Hintergrund**: Auslegung von Heizungssystemen in Zeiten des Klimawandels

## Werte erzeugen
Statt wie vorher mit `.groupby()`und `.mean()`zu arbeiten verwenden wir nun `.NamedAgg` (Sonderformat von `.agg()`)

**Vorteil**: Wir erzeugen nur Werte von Spalten die wir brauchen und können dafür auch jeweils verschiedene Funktionen (also min/mean/max usw.) verwenden

Min_Max_Mean_Jahreswerte = df_2.groupby("Jahr").agg(
    max=pd.NamedAgg(column='Tagesmitteltemperatur [°C]', aggfunc='max'), 
    min=pd.NamedAgg(column='Tagesmitteltemperatur [°C]', aggfunc='min'), 
    mean=pd.NamedAgg(column='Tagesmitteltemperatur [°C]', aggfunc='mean')
).reset_index()
Min_Max_Mean_Jahreswerte.columns=["Jahr","maximale Jahresmitteltemperatur [°C]","minimale Jahresmitteltemperatur [°C]","mittlere Jahresmitteltemperatur [°C]"]
Min_Max_Mean_Jahreswerte

## csv speichern

Min_Max_Mean_Jahreswerte.to_csv("Leipzig_Min_Max_Mean_Jahreswerte_volle_Jahre.csv",index=False)

colormap: https://stackoverflow.com/questions/49761221/make-seaborn-show-a-colorbar-instead-of-a-legend-when-using-hue-in-a-bar-plot

## Plot

Diesmal haben wir eine Colorbar statt der Legende mit den vielen Jahren. Da zwischendurch jedoch Jahre fehlen ist die Colorbar nicht ganz korrekt

import seaborn as sns
import matplotlib.pyplot as plt

# Funktion um Jahr als Text darzustellen
def label_year(year):

    xpos=Min_Max_Mean_Jahreswerte.loc[Min_Max_Mean_Jahreswerte["Jahr"]==year,"mittlere Jahresmitteltemperatur [°C]"].values[0]
    ypos=Min_Max_Mean_Jahreswerte.loc[Min_Max_Mean_Jahreswerte["Jahr"]==year,"minimale Jahresmitteltemperatur [°C]"].values[0]
    xoff=1
    yoff=0
    ax.text(xpos,ypos,str(year),horizontalalignment='center',ha='left', va='top', color="gray",rotation=-45,fontsize=10)

    return

# Anzahl der Jahre für palette Parameter im scatterplot
Anzahl_Jahre=Min_Max_Mean_Jahreswerte["Jahr"].nunique()

# color palette
cpalette = "coolwarm"

# colormap erstellen
norm = plt.Normalize(Min_Max_Mean_Jahreswerte["Jahr"].min(), Min_Max_Mean_Jahreswerte["Jahr"].max())
sm = plt.cm.ScalarMappable(cmap=cpalette, norm=norm)
sm.set_array([])

# plot
ax = sns.scatterplot(data=Min_Max_Mean_Jahreswerte, x="mittlere Jahresmitteltemperatur [°C]",y="minimale Jahresmitteltemperatur [°C]", s=100, hue="Jahr", palette=sns.color_palette(cpalette, n_colors=Anzahl_Jahre))

# jahre "labeln"
label_year(2020)
label_year(2018)
label_year(2017)
label_year(2016)
label_year(2015)
label_year(2014)
label_year(2013)
label_year(2012)
label_year(2011)
label_year(2010)

# legende entfernen
ax.get_legend().remove()

# color bar hinzufuegen
ax.figure.colorbar(sm)

plt.show()


# Plot 3b: Mittlere Jahrestemperatur im Vergleich zur minimalen Jahresmindesttemperatur (Scatter mit `Seaborn`)

Bisher haben wir die gegenüber der minimalen Jahrestemperatur dargestellt. Diese wird aus dem den `Tagesmittelwerte` bestimmt. Für die Heizung ist aber nicht der `Tagesmittelwert`, sondern die `Tagesminimaltemperatur` interessant. Dafür müssen wir noch mal die Rohdaten vom DWD anschauen und uns dafür die richtige Spalte raussuchen.

- **TGK**;Minimum der Lufttemperatur am Erdboden in 5cm Hoehe;°C

Wir wiederholen also alle unsere Schritte davor und nutzen jetzt die Spalte **TGK** statt **TMK**


## Daten einlesen und verarbeiten

Diesmal ist die Reihenfolge etwas vertauscht, das Ergebnis ist das gleiche

# historische Daten einlesen
data_hist = pd.read_csv("produkt_klima_tag_19340101_20181231_02932.txt", sep=";")
data_hist = data_hist.loc[:,("MESS_DATUM"," TGK")]

# aktuelle Daten einlesen
data_aktuell = pd.read_csv("produkt_klima_tag_20190719_20210118_02932.txt", sep=";")
data_aktuell = data_aktuell.loc[:,("MESS_DATUM"," TGK")]

# Daten zusammenfuehren
df = pd.concat([data_hist, data_aktuell]).reset_index()

# Spalte umbennnen
df.rename(columns={" TGK":"Tagesminimumstemperatur [°C]"}, inplace=True)

# Datumsformat einführen
df['Datum'] = pd.to_datetime(df['MESS_DATUM'],format='%Y%m%d')

# Tag/Monat/Jahr Spalte hinzufuegen
df["Jahr"] = pd.DatetimeIndex(df['Datum']).year
df["Monat"] = pd.DatetimeIndex(df['Datum']).month
df["Tag"] = pd.DatetimeIndex(df['Datum']).day

# Spalte MESS_DATUM entfernen
df = df.drop(["MESS_DATUM"],axis=1)

# Werte "-999" rausfiltern 
df = df.loc[df["Tagesminimumstemperatur [°C]"] > -999]

# Jahre entfernen die weniger als 360 Tage enthalten
df = df.groupby(by=["Jahr"]).filter(lambda x: len(x) > 360)

# Mininmale und mittlere Jahresmitteltemperatur
TempMin_Min_Mean_Jahreswerte = df.groupby("Jahr").agg(
    min=pd.NamedAgg(column='Tagesminimumstemperatur [°C]', aggfunc='min'), 
    mean=pd.NamedAgg(column='Tagesminimumstemperatur [°C]', aggfunc='mean')
).reset_index()
TempMin_Min_Mean_Jahreswerte.columns=["Jahr","minimale Jahresmindesttemperatur [°C]","mittlere Jahresmindesttemperatur [°C]"]
TempMin_Min_Mean_Jahreswerte.head()

Bei der `mittleren Jahresmindesttemperatur` wäre vor allem interessant nur die `Hauptheizmonate` **Dezember+Januar+Februar** auszuwerten. Dafür müssen wir erneut filtern

df_Heizmonate = df.loc[(df["Monat"]==1) | (df["Monat"]==2) | (df["Monat"]==12)  ]
df_Heizmonate["Monat"].unique()


TempMinJanFebDez_Mean_Jahreswerte = df_Heizmonate.groupby("Jahr").agg(
    mean=pd.NamedAgg(column='Tagesminimumstemperatur [°C]', aggfunc='mean')
).reset_index()
TempMinJanFebDez_Mean_Jahreswerte.columns=["Jahr","mittlere Mindesttemperatur (Jan+Feb+Dez) [°C]"]
TempMinJanFebDez_Mean_Jahreswerte.head()

### Plotten

import matplotlib.pyplot as plt

plt.figure(figsize=(10,4))

plt.xlabel("Jahr")
plt.ylabel("Temperatur [°C]")
plt.plot(TempMin_Min_Mean_Jahreswerte["Jahr"],TempMin_Min_Mean_Jahreswerte["minimale Jahresmindesttemperatur [°C]"],marker="s", ms=4, label="minimale Jahresmindesttemperatur [°C]")
plt.plot(TempMin_Min_Mean_Jahreswerte["Jahr"],TempMin_Min_Mean_Jahreswerte["mittlere Jahresmindesttemperatur [°C]"],marker="s", ms=4, label="mittlere Jahresmindesttemperatur [°C]")
plt.plot(TempMinJanFebDez_Mean_Jahreswerte["Jahr"],TempMinJanFebDez_Mean_Jahreswerte["mittlere Mindesttemperatur (Jan+Feb+Dez) [°C]"],marker="s", ms=4, label="mittlere Mindesttemperatur (Jan+Feb+Dez) [°C]")
plt.legend(bbox_to_anchor=(1, 1), loc='upper left',)

## DataFrame zusammenführen

Wir haben jetzt drei DataFrames

1. `Min_Max_Mean_Jahreswerte` mit den **minimalen** und **mittleren Jahrestemperaturen**
2. `TempMin_Min_Mean_Jahreswerte` mit den **minimalen** und **mittleren Jahresmindesttemperaturen**
3. `TempMinJanFebDez_Mean_Jahreswerte` mit den **mittleren Mindesttemperatur (Jan+Feb+Dez)**

Diese drei wollen wir jetzt zu einem zusammenführen

### ersten beiden DataFrames anzeigen

Min_Max_Mean_Jahreswerte.head(3)

TempMin_Min_Mean_Jahreswerte.head(3)

### Ersten beiden DataFrames zusammenführen

MinMean_total = Min_Max_Mean_Jahreswerte.join(TempMin_Min_Mean_Jahreswerte.set_index("Jahr"), on="Jahr")
MinMean_total.head(3)

Für **1934** gab es keinen Eintrag in `Min_Max_Mean_Jahreswerte`. In unserem zusammengeführten neuen DataFrame steht dort deshalb **NaN**

### dritten DataFrame hinzufuegen

MinMean_total = MinMean_total.join(TempMinJanFebDez_Mean_Jahreswerte.set_index("Jahr"), on="Jahr")
MinMean_total.head(3)

### als csv exportieren

MinMean_total.to_csv("Leipzig_Min_Max_Mean_Gesamt_Jahreswerte_volle_Jahre.csv", index=False)

## Plot 


import seaborn as sns
import matplotlib.pyplot as plt

# Bildgröße

plt.figure(figsize=(10,8))


# Funktion um Jahr als Text darzustellen
def label_year(year):

    xpos=MinMean_total.loc[MinMean_total["Jahr"]==year,"mittlere Jahresmitteltemperatur [°C]"].values[0]
    ypos=MinMean_total.loc[MinMean_total["Jahr"]==year,"minimale Jahresmindesttemperatur [°C]"].values[0]
    xoff=1
    yoff=0
    ax.text(xpos,ypos,str(year),horizontalalignment='center',ha='left', va='top', color="gray",rotation=-45,fontsize=10)

    return

# Anzahl der Jahre für palette Parameter im scatterplot
Anzahl_Jahre=Min_Max_Mean_Jahreswerte["Jahr"].nunique()

# color palette
cpalette = "coolwarm"

# colormap erstellen
norm = plt.Normalize(Min_Max_Mean_Jahreswerte["Jahr"].min(), Min_Max_Mean_Jahreswerte["Jahr"].max())
sm = plt.cm.ScalarMappable(cmap=cpalette, norm=norm)
sm.set_array([])

# plot
ax = sns.scatterplot(data=MinMean_total, x="mittlere Jahresmitteltemperatur [°C]",y="minimale Jahresmindesttemperatur [°C]", s=100, hue="Jahr", palette=sns.color_palette(cpalette, n_colors=Anzahl_Jahre))

# jahre "labeln"
label_year(2020)
label_year(2018)
label_year(2017)
label_year(2016)
label_year(2015)
label_year(2014)
label_year(2013)
label_year(2012)
label_year(2011)
label_year(2010)

# legende entfernen
ax.get_legend().remove()

# color bar hinzufuegen
ax.figure.colorbar(sm)

plt.show()


# Plot 3c: Mittlere Jahrestemperatur im Vergleich zur mittleren Mindesttemperatur (Jan+Feb+Dez) (Scatter mit `Seaborn`)


import seaborn as sns
import matplotlib.pyplot as plt

# Bildgröße

plt.figure(figsize=(10,8))


# Funktion um Jahr als Text darzustellen
def label_year(year):

    xpos=MinMean_total.loc[MinMean_total["Jahr"]==year,"mittlere Jahresmitteltemperatur [°C]"].values[0]
    ypos=MinMean_total.loc[MinMean_total["Jahr"]==year,"mittlere Mindesttemperatur (Jan+Feb+Dez) [°C]"].values[0]
    xoff=1
    yoff=0
    ax.text(xpos,ypos,str(year),horizontalalignment='center',ha='left', va='top', color="gray",rotation=-45,fontsize=10)

    return

# Anzahl der Jahre für palette Parameter im scatterplot
Anzahl_Jahre=Min_Max_Mean_Jahreswerte["Jahr"].nunique()

# color palette
cpalette = "coolwarm"

# colormap erstellen
norm = plt.Normalize(Min_Max_Mean_Jahreswerte["Jahr"].min(), Min_Max_Mean_Jahreswerte["Jahr"].max())
sm = plt.cm.ScalarMappable(cmap=cpalette, norm=norm)
sm.set_array([])

# plot
ax = sns.scatterplot(data=MinMean_total, x="mittlere Jahresmitteltemperatur [°C]",y="mittlere Mindesttemperatur (Jan+Feb+Dez) [°C]", s=100, hue="Jahr", palette=sns.color_palette(cpalette, n_colors=Anzahl_Jahre))

# jahre "labeln"
label_year(2020)
label_year(2018)
label_year(2017)
label_year(2016)
label_year(2015)
label_year(2014)
label_year(2013)
label_year(2012)
label_year(2011)
label_year(2010)

# legende entfernen
ax.get_legend().remove()

# color bar hinzufuegen
ax.figure.colorbar(sm)

plt.show()


# Plot 4: Regression für Jahre seit 2010

## Daten Filtern

MinMean_total_since2010=MinMean_total.loc[MinMean_total["Jahr"]>=2010]
MinMean_total_since2010

## Plot 4a: Regression (`mittlere Jahrestemp` vs. `mittlere Mindesttemperatur (Jan+Feb+Dez)`) 

import seaborn as sns

sns.reset_defaults()
sns.set_style("darkgrid")

sns.regplot(data=MinMean_total_since2010, x="mittlere Jahresmitteltemperatur [°C]",y="mittlere Mindesttemperatur (Jan+Feb+Dez) [°C]")
plt.show()

## Plot 4b: Multiplot Regression  (`mittlere Jahrestemp` vs. `minimale Jahrestemperatur [°C]`) + (`mittlere Jahrestemp` vs. `minimale Jahresmindesttemperatur [°C]`) + (`mittlere Jahrestemp` vs. `mittlere Mindesttemperatur (Jan+Feb+Dez)`) 

import seaborn as sns

sns.reset_defaults()
sns.set_style("darkgrid")


fig, (ax1,ax2,ax3) = plt.subplots(3, sharex=True, figsize=(6,10))

# plot 1
sns.regplot(ax=ax1, data=MinMean_total_since2010, x="mittlere Jahresmitteltemperatur [°C]",y="minimale Jahresmitteltemperatur [°C]", color="red")
ax1.yaxis.label.set_color('red')
ax1.tick_params(axis='y', colors='red')

# plot 2
sns.regplot(ax=ax2, data=MinMean_total_since2010, x="mittlere Jahresmitteltemperatur [°C]",y="minimale Jahresmindesttemperatur [°C]", color="blue")
ax2.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', colors='blue')

# plot 3
sns.regplot(ax=ax3, data=MinMean_total_since2010, x="mittlere Jahresmitteltemperatur [°C]",y="mittlere Mindesttemperatur (Jan+Feb+Dez) [°C]", color="green")
ax3.yaxis.label.set_color('green')
ax3.tick_params(axis='y', colors='green')

fig.tight_layout()
plt.show()

