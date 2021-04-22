# Daten Einlesen

## Basics (Pandas + Matplotlib)

### Plotten

import pandas as pd
import glob # Zur Bestimmung der Liste an Dateien nach Suchschema
from matplotlib import pyplot as plt

Files_Feder1 = glob.glob("Feder_1-Messung*.csv")

plt.xlabel("Weg [mm]")
plt.ylabel("Kraft [N]")
plt.grid()

plt.title("Alle Messungen von Feder 1")
for filename in Files_Feder1:

    # Daten einlesen
    df = pd.read_csv(filename, index_col=None, header=0)

    # plotten
    plt.plot(df["Weg (mm)"], df["Kraft (N)"], label=filename) 


plt.legend() # muss nach plot kommen
plt.savefig('03-Feder1_Alle-Messungen.png', bbox_inches='tight', dpi=200)


### Was ist ein Pandas Dataframe?

- Indexierung startet bei 0
- Vorteil des Pandas DataFrame kommt zum tragen, wenn alle Daten in einem DataFrame vereinigt sind und über Kategorien getrennt werden

Oft wird als Name für Dataframes `df` verwendet, es geht aber natuerlich auch jeder andere Name

Zur Darstellung gibt es verschiedene Möglichkeiten (Hier Beispielhaft mit dem Dataframe mit dem Namen `df`)

-  `df` gesamten Dataframe anzeigen
-  `df.head()` ersten 5 Datenpunkte anzeigen (5 ist Standardwert)
-  `df.head(10)` ersten 10 Datenpunkte anzeigen
-  `df.tail()` letzten 5 Datenpunkte anzeigen (5 ist Standardwert)
-  `df.tail(10)` letzten 10 Datenpunkte anzeigen
-  `df.describe()` Zusammenfassung für jede Spalte (Anzahl, Mittelwert, usw.)
-  `df.info()` Zeigt Datentypen und Anzahl der Werte je Spalten an

df

df.head()

df.describe()

### Mehrere Messungen mit `Matplotlib` plotten

- wollen wir nun von 3 verschiedenen Federn jeweils 5 Messungen plotten so wird der Code schon recht lang und bezüglich der Beschriftung muss auch etwas getricks werden

import pandas as pd
from matplotlib import pyplot as plt
import glob # Zur Bestimmung der Liste an Dateien nach Suchschema


plt.xlabel("Weg [mm]")
plt.ylabel("Kraft [N]")
plt.grid()

plt.title("Alle Messungen von Feder 1 bis 3")

# Messung 1
Files_Feder1 = glob.glob("Feder_1-Messung*.csv")
Messung=0 # Laufvariable um zu prüfen was die erste Messung ist (Für Labelabfrage)
label="Feder1" 
color="r"
for filename in Files_Feder1:
    Messung  = Messung + 1

    # Daten einlesen
    df = pd.read_csv(filename, index_col=None, header=0)

    # plotten
    if Messung == 1:
        plt.plot(df["Weg (mm)"], df["Kraft (N)"], label=label, c=color) 
    else:
        plt.plot(df["Weg (mm)"], df["Kraft (N)"], label='', c=color) 

# Messung 2
Files_Feder1 = glob.glob("Feder_2-Messung*.csv")
Messung=0 # Laufvariable um zu prüfen was die erste Messung ist (Für Labelabfrage)
label="Feder2" 
color="b"
for filename in Files_Feder1:
    Messung  = Messung + 1

    # Daten einlesen
    df = pd.read_csv(filename, index_col=None, header=0)

    # plotten
    if Messung == 1:
        plt.plot(df["Weg (mm)"], df["Kraft (N)"], label=label, c=color) 
    else:
        plt.plot(df["Weg (mm)"], df["Kraft (N)"], label='', c=color) 

# Messung 3
Files_Feder1 = glob.glob("Feder_3-Messung*.csv")
Messung=0 # Laufvariable um zu prüfen was die erste Messung ist (Für Labelabfrage)
label="Feder3" 
color="g"
for filename in Files_Feder1:
    Messung  = Messung + 1

    # Daten einlesen
    df = pd.read_csv(filename, index_col=None, header=0)

    # plotten
    if Messung == 1:
        plt.plot(df["Weg (mm)"], df["Kraft (N)"], label=label, c=color) 
    else:
        plt.plot(df["Weg (mm)"], df["Kraft (N)"], label='', c=color) 



plt.legend() # muss nach plot kommen
plt.savefig('03-Feder1bis3_Alle-Messungen_Matplotlib.png', bbox_inches='tight', dpi=200)


### Alle Messungen einlesen in einem DataFrame überführen (Parameter aus Dateinamen auslesen)

- Wir wollen nun schauen wie wir mit nur wenigen Zeilen Code viel effektiver mit der Bibliothek `seaborn` plotten können
- Bisher haben jetzt für **jede Messung einen eigenen DataFrame** erstellt. 
- Damit wir jedoch den **DataFrame effektiv nutzen** können, müssen wir **alle Messungen in einen DataFrame** zusammenführen.

import pandas as pd
import glob # Zur Bestimmung der Liste an Dateien nach Suchschema

all_files = glob.glob("Feder*-Messung*.csv") # Liste aller Dateien die eingelesen werden sollen

li = [] # dummy array um Dataframes zu sammeln

# Funktion die Parameter aus Dateinamen liest 
def get_file_parameter(filename,start_indicator,end_indicator):
    start = filename.find(start_indicator) + len(start_indicator)
    end = filename.find(end_indicator)
    substring = filename[start:end]
    return substring

for filename in all_files:

    # Datei einlesen
    df = pd.read_csv(filename, index_col=None, header=0)

    # Feder aus Namen lesen
    Feder = get_file_parameter(filename,"Feder_","-")
    df['Feder'] = Feder

    # Messnummer aus Namen lesen
    Messung = get_file_parameter(filename,"Messung_",".csv")
    df['Messung'] = Messung

    # Dataframes anfügen
    li.append(df)

# Dataframe zusammenführen
Messungen = pd.concat(li, axis=0, ignore_index=True)

Messungen.describe()

Messungen

### Plotten des neuen DataFrames mit `Seaborn`

- Zunächst wollen wir eine ähnliche Grafik wie vorhin erzeugen

import seaborn as sns

sns.set_style("whitegrid")
sns.lineplot(data=Messungen, x="Weg (mm)", y="Kraft (N)", hue="Feder", style="Messung", palette="tab10")

# da Seaborn auf Matplotlib aufbaut können diese Befehle weiterhin verwendet werden
plt.title("Alle Messungen von Feder 1 bis 3") 
plt.savefig('03-Feder1bis3_Alle-Messungen_Seaborn_whitegrid.png', bbox_inches='tight', dpi=200)


- Man beachte die Anzahl an Codezeilen die notwendig waren um eine ähnliche Grafik zu erzeugen. 
- Weiterhin werden Beschriftungen aus Achsen und Legenden aus dem Dataframe übernommen



Als nächstes werden wir den Lineplot so verwenden, wie er standardmäßig von Seaborn erstellt wird. Dabei wird der Mittelwert über alle Messungen (jeweils für jede Feder) ermittelt und das mittels `Bootstrapping` ermittelte Konfidenzintervall (default sind 95%) geplottet

import seaborn as sns

sns.set_style("whitegrid")
sns.lineplot(data=Messungen, x="Weg (mm)", y="Kraft (N)", hue="Feder", palette="tab10")

# da Seaborn auf Matplotlib aufbaut können diese Befehle weiterhin verwendet werden
plt.title("Alle Messungen von Feder 1 bis 3 (95% KI)") 
plt.savefig('03-Feder1bis3_Alle-Messungen_Seaborn_ci.png', bbox_inches='tight', dpi=200)


Das Konfidenzintervall kann mit dem Parameter `ci` eingestellt werden. Mit `ci=sd` wird die Standardabweichung geplottet 

import seaborn as sns

sns.set_style("whitegrid")
sns.lineplot(data=Messungen, x="Weg (mm)", y="Kraft (N)", hue="Feder", ci="sd")

# da Seaborn auf Matplotlib aufbaut können diese Befehle weiterhin verwendet werden
plt.title("Alle Messungen von Feder 1 bis 3 (sd)") 
plt.savefig('03-Feder1bis3_Alle-Messungen_Seaborn_sd.png', bbox_inches='tight', dpi=200)

Mit `setstyle` können verschiedene vordefinierte Stile verwendet werden
- `darkgrid`, `whitegrid`, `dark`, `white`, `ticks` 


Nachfolgend mit `darkgrid`

import seaborn as sns

sns.set_style("darkgrid")
sns.lineplot(data=Messungen, x="Weg (mm)", y="Kraft (N)", hue="Feder", ci="sd")

# da Seaborn auf Matplotlib aufbaut können diese Befehle weiterhin verwendet werden
plt.title("Alle Messungen von Feder 1 bis 3 (sd)") 
plt.savefig('03-Feder1bis3_Alle-Messungen_Seaborn_sd_darkgrid.png', bbox_inches='tight', dpi=200)

`white`

import seaborn as sns

sns.set_style("white")
sns.lineplot(data=Messungen, x="Weg (mm)", y="Kraft (N)", hue="Feder", ci="sd")

# da Seaborn auf Matplotlib aufbaut können diese Befehle weiterhin verwendet werden
plt.title("Alle Messungen von Feder 1 bis 3 (sd)") 
plt.savefig('03-Feder1bis3_Alle-Messungen_Seaborn_sd_white.png', bbox_inches='tight', dpi=200)

`dark`

import seaborn as sns

sns.set_style("dark")
sns.lineplot(data=Messungen, x="Weg (mm)", y="Kraft (N)", hue="Feder", ci="sd")

# da Seaborn auf Matplotlib aufbaut können diese Befehle weiterhin verwendet werden
plt.title("Alle Messungen von Feder 1 bis 3 (sd)") 
plt.savefig('03-Feder1bis3_Alle-Messungen_Seaborn_sd_dark.png', bbox_inches='tight', dpi=200)

`ticks`

import seaborn as sns

sns.set_style("ticks")
sns.lineplot(data=Messungen, x="Weg (mm)", y="Kraft (N)", hue="Feder", ci="sd")

# da Seaborn auf Matplotlib aufbaut können diese Befehle weiterhin verwendet werden
plt.title("Alle Messungen von Feder 1 bis 3 (sd)") 
plt.savefig('03-Feder1bis3_Alle-Messungen_Seaborn_sd_ticks.png', bbox_inches='tight', dpi=200)



Ein riesen Vorteil an der Verwendung von Seaborn ist, dass die Standardeinstellungen sehr oft bereits sehr gut aussehende Grafiken erzeugen und somit mit sehr wenig Zeilen code gearbeitet werden kann.

Neben den Anpassungen des Aussehens über `set_style` kann auch die Größe der Schrift über `set_context` definiert werden, dabei gibt es folgende Möglichkeiten
- `paper` (Schrift klein)
- `notebook` (Schrift normal) (**default**)
- `talk` (Schrift groß)
- `poster` (Schrift sehr groß)

`paper`

import seaborn as sns

sns.set_style("darkgrid")
sns.set_context("paper")

sns.lineplot(data=Messungen, x="Weg (mm)", y="Kraft (N)", hue="Feder", ci="sd")

# da Seaborn auf Matplotlib aufbaut können diese Befehle weiterhin verwendet werden
plt.title("Alle Messungen von Feder 1 bis 3 (sd)") 
plt.savefig('03-Feder1bis3_Alle-Messungen_Seaborn_sd_darkgrid_paper.png', bbox_inches='tight', dpi=200)

`talk`

import seaborn as sns

sns.set_style("darkgrid")
sns.set_context("talk")

sns.lineplot(data=Messungen, x="Weg (mm)", y="Kraft (N)", hue="Feder", ci="sd")

# da Seaborn auf Matplotlib aufbaut können diese Befehle weiterhin verwendet werden
plt.title("Alle Messungen von Feder 1 bis 3 (sd)") 
plt.savefig('03-Feder1bis3_Alle-Messungen_Seaborn_sd_darkgrid_talk.png', bbox_inches='tight', dpi=200)

`poster`

import seaborn as sns

sns.set_style("darkgrid")
sns.set_context("poster")

sns.lineplot(data=Messungen, x="Weg (mm)", y="Kraft (N)", hue="Feder", ci="sd")

# da Seaborn auf Matplotlib aufbaut können diese Befehle weiterhin verwendet werden
plt.title("Alle Messungen von Feder 1 bis 3 (sd)") 
plt.savefig('03-Feder1bis3_Alle-Messungen_Seaborn_sd_darkgrid_talk.png', bbox_inches='tight', dpi=200)





## Zusätzliche `Seaborn` plots mit weiteren Parametern

Um die Funktionen von Seaborn weiter zu verdeutlichen wurden zusätzliche Parameter in unser virtuelles Experiment eingefügt:

- Es werden nun 3 Federn jeweils 25 mal gemessen
- Dies wird jeweils von zwei verschiedenen Personen durchgeführt (Clara und Peter)
- Jeder Person nutzt jeweils zwei verschiedene Kraftmessdosen

### Messdaten automatisiert einlesen mit Kategorien

import pandas as pd
import glob # Zur Bestimmung der Liste an Dateien nach Suchschema

all_files = glob.glob("Big_Feder*-Messung*.csv") # Liste aller Dateien die eingelesen werden sollen

li = [] # dummy array um Dataframes zu sammeln

# Funktion die Parameter aus Dateinamen liest 
def get_file_parameter(filename,start_indicator,end_indicator):
    start = filename.find(start_indicator) + len(start_indicator)
    end = filename.find(end_indicator)
    substring = filename[start:end]
    return substring

for filename in all_files:

    # Datei einlesen
    df = pd.read_csv(filename, index_col=None, header=0)

    # Feder aus Namen lesen
    Feder = get_file_parameter(filename,"Big_Feder_","-")
    df['Feder'] = Feder

    # Person aus Namen lesen
    Person = get_file_parameter(filename,"Person_","-Messdose")
    df['Person'] = Person

    # Messdose aus Namen lesen
    Messdose = get_file_parameter(filename,"Messdose_","-Messung")
    df['Messdose'] = Messdose

    # Messnummer aus Namen lesen
    Messung = get_file_parameter(filename,"Messung_",".csv")
    df['Messung'] = Messung

    # Dataframes anfügen
    li.append(df)

# Dataframe zusammenführen
Messungen = pd.concat(li, axis=0, ignore_index=True)

Unser neuer Dataframe besitzt 1500 Reihen und 6 Spalten

# Messungen exportieren
Messungen.to_csv('Messungen_4Parameter.csv', index=None)

### Plotten Lineplot (Bootstrapping)

import seaborn as sns

sns.set_style("darkgrid")
sns.set_context("talk")

sns.lineplot(data=Messungen, x="Weg (mm)", y="Kraft (N)", hue="Feder")

plt.savefig('04-Big-Feder-Weg-Kraft.png', bbox_inches='tight', dpi=200)

### Plotten Lineplot mit FacetGrid

import seaborn as sns

sns.set_style("darkgrid")
sns.set_context("notebook")

g = sns.FacetGrid(data=Messungen, col="Person",  row="Messdose", hue="Feder")
g.map_dataframe(sns.lineplot, x="Weg (mm)", y="Kraft (N)")
g.set_axis_labels("Weg (mm)", "Kraft (N)")

plt.savefig('04-Big-Feder-Weg-Kraft-FacetGrid.png', bbox_inches='tight', dpi=200)

### Maximalwerte aus Messkurven bestimmen

- Darstellung eines Wertes pro Messung besser als jede Kurve, daher wird hier nur der Maximalwert rausgezogen

MaxWerte = Messungen.groupby(['Feder','Person','Messdose','Messung']).agg({'Kraft (N)': ['max']}).reset_index()
MaxWerte.columns = ['Feder','Person','Messdose','Messung','Kraft_max (N)']
MaxWerte.describe()

### Maximalwerte plotten (stripplot)

import seaborn as sns

sns.set_style("darkgrid")
sns.set_context("notebook")

sns.stripplot(data=MaxWerte, x="Feder", y="Kraft_max (N)", hue="Person", dodge=True)

plt.savefig('04-Big-Feder-KraftMax-Strip-Personen.png', bbox_inches='tight', dpi=200)

### Maximalwerte plotten (catplot mit stripplot)

- Aufteilung mittels catplot

import seaborn as sns

sns.set_style("darkgrid")
sns.set_context("notebook")

sns.catplot(x="Feder", y="Kraft_max (N)",
                hue="Person", col="Messdose",
                data=MaxWerte, kind="strip", dodge=True,
                height=4, aspect=.7); # dodge=True bewirkt das Daten nicht übereinander geplottet werden

plt.savefig('04-Big-Feder-KraftMax-CatPlot-Strip-Personen-Messdosen.png', bbox_inches='tight', dpi=200)


### Maximalwerte plotten (catplot mit boxplot)

import seaborn as sns

sns.set_style("darkgrid")
sns.set_context("notebook")

sns.catplot(x="Feder", y="Kraft_max (N)",
                hue="Person", col="Messdose",
                data=MaxWerte, kind="box",
                height=4, aspect=.7);

plt.savefig('04-Big-Feder-KraftMax-CatPlot-Box-Personen-Messdosen.png', bbox_inches='tight', dpi=200)

### Maximalwerte plotten (catplot mit bar plot)

import seaborn as sns

sns.set_style("darkgrid")
sns.set_context("notebook")

sns.catplot(x="Feder", y="Kraft_max (N)",
                hue="Person", col="Messdose",
                data=MaxWerte, kind="bar",
                height=4, aspect=.7);

plt.savefig('04-Big-Feder-KraftMax-CatPlot-Bar-Personen-Messdosen.png', bbox_inches='tight', dpi=200)

tauschen Messdose / Person

import seaborn as sns

sns.set_style("darkgrid")
sns.set_context("notebook")

sns.catplot(x="Feder", y="Kraft_max (N)",
                hue="Messdose", col="Person",
                data=MaxWerte, kind="bar",
                height=4, aspect=.7);

plt.savefig('04-Big-Feder-KraftMax-CatPlot-Bar-Messdosen-Personen.png', bbox_inches='tight', dpi=200)

# Filtern (nur Clara und Messdose 1)

Clara_Messdose1 = MaxWerte[(MaxWerte["Person"] == "Clara") & (MaxWerte["Messdose"] == "1")]
Clara_Messdose1


## Prüfen ob Filter richtig funktioniert mit `.unique()`

Clara_Messdose1["Person"].unique()

Clara_Messdose1["Messdose"].unique()

## `.unique()` für MaxWerte Dataframe anwenden

MaxWerte["Person"].unique()