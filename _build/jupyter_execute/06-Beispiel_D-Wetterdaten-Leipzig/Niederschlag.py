# Niederschlag

RSK;tgl. Niederschlagshoehe,mm

## Daten einlesen und verarbeiten

import pandas as pd

# historische Daten einlesen
data_hist = pd.read_csv("produkt_klima_tag_19340101_20181231_02932.txt", sep=";")
data_hist = data_hist.loc[:,("MESS_DATUM"," RSK")]

# aktuelle Daten einlesen
data_aktuell = pd.read_csv("produkt_klima_tag_20190719_20210118_02932.txt", sep=";")
data_aktuell = data_aktuell.loc[:,("MESS_DATUM"," RSK")]

# Daten zusammenfuehren
df = pd.concat([data_hist, data_aktuell]).reset_index(drop=True)

# Spalte umbennnen
df.rename(columns={" RSK":"tgl. Niederschlagshoehe [mm]"}, inplace=True)

# Datumsformat einführen
df['Datum'] = pd.to_datetime(df['MESS_DATUM'],format='%Y%m%d')

# Tag/Monat/Jahr Spalte hinzufuegen
df["Jahr"] = pd.DatetimeIndex(df['Datum']).year
df["Monat"] = pd.DatetimeIndex(df['Datum']).month
df["Tag"] = pd.DatetimeIndex(df['Datum']).day

# Spalte MESS_DATUM entfernen
df = df.drop(["MESS_DATUM"],axis=1)

df

### auf ungewöhnliche Werte prüfen

df["tgl. Niederschlagshoehe [mm]"].describe()

# Werte "-999" rausfiltern 
df = df.loc[df["tgl. Niederschlagshoehe [mm]"] > -999]

# Jahre entfernen die weniger als 360 Tage enthalten
df = df.groupby(by=["Jahr"]).filter(lambda x: len(x) > 360)

df

import seaborn as sns
sns.set(rc={'figure.figsize':(10,15)})
sns.countplot(data=df, y="Jahr")

# Jahreswerte bestimmen
Niederschlag_Jahreswerte = df.groupby("Jahr").agg(
    sum=pd.NamedAgg(column='tgl. Niederschlagshoehe [mm]', aggfunc='sum')
).reset_index()

Niederschlag_Jahreswerte.columns=["Jahr","summierte Jahresniederschlagsmenge [mm]"]
Niederschlag_Jahreswerte

# Monatswerte bestimmen
Niederschlag_Monatswerte = df.groupby(["Jahr","Monat"]).agg( 
    sum=pd.NamedAgg(column='tgl. Niederschlagshoehe [mm]', aggfunc='sum')
).reset_index()

Niederschlag_Monatswerte.columns=["Jahr","Monat","summierte Monatsniederschlagsmenge [mm]"]
Niederschlag_Monatswerte

# Plot 1 : Jahreswerte

import seaborn as sns
import matplotlib.pyplot as plt

sns.reset_defaults()
sns.set_style("darkgrid")
plt.figure(figsize=(10,4))

ax = sns.barplot(data=Niederschlag_Jahreswerte, x="Jahr", y="summierte Jahresniederschlagsmenge [mm]", color="dodgerblue")

ax.axhline(Niederschlag_Jahreswerte["summierte Jahresniederschlagsmenge [mm]"].mean(), alpha=0.5, c="gray")
ax.text(0,Niederschlag_Jahreswerte["summierte Jahresniederschlagsmenge [mm]"].max(),"Mittelwert="+str(Niederschlag_Jahreswerte["summierte Jahresniederschlagsmenge [mm]"].mean().round(1))+"mm",c="gray")

for item in ax.get_xticklabels():
    item.set_rotation(90)

# Plot 1b : Sommermonate

# Monatswerte bestimmen

df_Sommer = df.loc[(df["Monat"] == 6) | (df["Monat"] == 7) | (df["Monat"] == 8)]

Niederschlag_Sommermonate = df_Sommer.groupby(["Jahr"]).agg( 
    sum=pd.NamedAgg(column='tgl. Niederschlagshoehe [mm]', aggfunc='sum')
).reset_index()

Niederschlag_Sommermonate.columns=["Jahr","summierte Sommerniederschlagsmenge [mm]"]
Niederschlag_Sommermonate

import seaborn as sns
import matplotlib.pyplot as plt

sns.reset_defaults()
sns.set_style("darkgrid")
plt.figure(figsize=(10,4))

ax = sns.barplot(data=Niederschlag_Sommermonate, x="Jahr", y="summierte Sommerniederschlagsmenge [mm]", color="dodgerblue")

ax.axhline(Niederschlag_Sommermonate["summierte Sommerniederschlagsmenge [mm]"].mean(), alpha=0.5, c="gray")
ax.text(0,Niederschlag_Sommermonate["summierte Sommerniederschlagsmenge [mm]"].max(),"Mittelwert="+str(Niederschlag_Sommermonate["summierte Sommerniederschlagsmenge [mm]"].mean().round(1))+"mm",c="gray")

for item in ax.get_xticklabels():
    item.set_rotation(90)

# Plot 2 : Monatswerte

import seaborn as sns
import calendar
sns.set(rc={'figure.figsize':(12,6)})

# Monatswerte für jedes Jahr
Jahr2020=Niederschlag_Monatswerte.loc[(Niederschlag_Monatswerte["Jahr"]==2020)]
Jahr2018=Niederschlag_Monatswerte.loc[(Niederschlag_Monatswerte["Jahr"]==2018)]
Jahr2017=Niederschlag_Monatswerte.loc[(Niederschlag_Monatswerte["Jahr"]==2017)]
Jahr2016=Niederschlag_Monatswerte.loc[(Niederschlag_Monatswerte["Jahr"]==2016)]

# Funktion zum Darstellen der Min/Max Werte fuer ein Jahr
def print_min_max(df,ax):

    min=df["summierte Monatsniederschlagsmenge [mm]"].min().round(1)
    minMonat=df.loc[df["summierte Monatsniederschlagsmenge [mm]"].idxmin(),"Monat"]
    max=df["summierte Monatsniederschlagsmenge [mm]"].max().round(1)
    maxMonat=df.loc[df["summierte Monatsniederschlagsmenge [mm]"].idxmax(),"Monat"]
    
    Month_name_min=calendar.month_name[minMonat]
    Month_name_max=calendar.month_name[maxMonat]

    ax.text(1,90,"Min ("+Month_name_min+"):"+str(min)+"mm",color="gray", horizontalalignment='left')
    ax.text(1,80,"Max ("+Month_name_max+"):"+str(max)+"mm",color="gray", horizontalalignment='left')
    return
    

# Figure mit 2 x 2 "subplots=ax" 
fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)

# Links oben : 2020
sns.lineplot(x=Niederschlag_Monatswerte["Monat"],y=Niederschlag_Monatswerte["summierte Monatsniederschlagsmenge [mm]"],ci="sd", ax=ax[0,0])
ax[0,0].plot(Jahr2020["Monat"],Jahr2020["summierte Monatsniederschlagsmenge [mm]"], color="red")
ax[0,0].set_title("2020")
ax[0,0].set_ylabel("summierte\nMonatsniederschlagsmenge\n[mm]")
print_min_max(Jahr2020,ax[0,0])

# Rechts oben : 2018
sns.lineplot(x=Niederschlag_Monatswerte["Monat"],y=Niederschlag_Monatswerte["summierte Monatsniederschlagsmenge [mm]"],ci="sd", ax=ax[0,1])
ax[0,1].plot(Jahr2018["Monat"],Jahr2018["summierte Monatsniederschlagsmenge [mm]"], color="red")
ax[0,1].set_title("2018")
print_min_max(Jahr2018,ax[0,1])

# Links unten : 2017
sns.lineplot(x=Niederschlag_Monatswerte["Monat"],y=Niederschlag_Monatswerte["summierte Monatsniederschlagsmenge [mm]"],ci="sd", ax=ax[1,0])
ax[1,0].plot(Jahr2017["Monat"],Jahr2017["summierte Monatsniederschlagsmenge [mm]"], color="red")
ax[1,0].set_title("2017")
ax[1,0].set_ylabel("summiert\nMonatsniederschlagsmenge\n[mm]")
print_min_max(Jahr2017,ax[1,0])

# Rechts unten : 2016
sns.lineplot(x=Niederschlag_Monatswerte["Monat"],y=Niederschlag_Monatswerte["summierte Monatsniederschlagsmenge [mm]"],ci="sd", ax=ax[1,1])
ax[1,1].plot(Jahr2016["Monat"],Jahr2016["summierte Monatsniederschlagsmenge [mm]"], color="red")
ax[1,1].set_title("2016")
print_min_max(Jahr2016,ax[1,1])


fig.tight_layout()

