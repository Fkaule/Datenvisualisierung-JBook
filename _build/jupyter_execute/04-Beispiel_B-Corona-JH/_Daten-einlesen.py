# John Hopkins Corona Daten

COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University
https://github.com/CSSEGISandData/COVID-19

Link zu den Daten bekommen:
- Datei raussuchen: 
    - **COVID-19** / **csse_covid_19_data** / **csse_covid_19_time_series** / 
- Datei `time_series_covid19_confirmed_global.csv` anklicken und Link von `RAW` (rechts oben) kopieren und diesen verwenden


Einlesen analog Vorgehen hier: https://towardsdatascience.com/covid-19-data-processing-58aaa3663f6

## `confirmed` einlesen

import pandas as pd


data_confirmed="https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

df_confirmed_wide = pd.read_csv(data_confirmed)
df_confirmed_wide

Die Daten liegen mit jedem Datum pro Spalte vor. Diese Art ist für die Verarbeitung mit `Pandas` sehr ungeeignet, weshalb wir aus dem **breiten** (nach rechts) Dataframe jetzt einen **langen** (nach unten) erstellen und nutzen dafür den `.melt` Befehl

# Liste der Einträge aller Daten erstellen 
dates = df_confirmed_wide.columns[4:] # Nimm alle Spalten ab der fünften (0=erste Spalte)
dates

df_confirmed_long = df_confirmed_wide.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
    value_vars=dates, 
    var_name='Date', 
    value_name='Confirmed'
)
df_confirmed_long

- der neue lange Dataframe `df_long` hat **100191 rows × 6 columns** = 601.146 Einträge
- der alte breite Dataframe `df_wide` hat **273 rows × 371 columns** = 101.283 Einträge

Die Einträge haben sich also für unseren neuen Dataframe `df_long` vervielfacht, da jetzt das Datum immer dazu geschrieben werden muss und somit oft doppelt vorkommt

### `deaths` + `recovered` analog 

data_death="https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
data_recovered="https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"


df_death_wide = pd.read_csv(data_death)
df_recovered_wide = pd.read_csv(data_recovered)

df_death_long = df_death_wide.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
    value_vars=dates, 
    var_name='Date', 
    value_name='Deaths'
)

recovered_df_long = df_recovered_wide.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
    value_vars=dates, 
    var_name='Date', 
    value_name='Recovered'
)


#### alle drei Dataframes zusammenführen

# Merging confirmed_df_long and deaths_df_long
full_table = df_confirmed_long.merge(
  right=df_death_long, 
  how='left',
  on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
)
# Merging full_table and recovered_df_long
full_table = full_table.merge(
  right=recovered_df_long, 
  how='left',
  on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
)

full_table

#### Datum als Datetime

full_table['Date'] = pd.to_datetime(full_table['Date'])
full_table.head()

#### missing NaN 

full_table.isna().sum()

#### recovered mit nullen füllen

full_table['Recovered'] = full_table['Recovered'].fillna(0)

#### Kreuzfahrtschiffe rausnehmen

ship_rows = full_table['Province/State'].str.contains('Grand Princess') | full_table['Province/State'].str.contains('Diamond Princess') | full_table['Country/Region'].str.contains('Diamond Princess') | full_table['Country/Region'].str.contains('MS Zaandam')
full_ship = full_table[ship_rows]

full_table = full_table[~(ship_rows)]

### Neue Spalte `active`

# Active Case = confirmed - deaths - recovered
full_table['Active'] = full_table['Confirmed'] - full_table['Deaths'] - full_table['Recovered']

### Länder zusammenfassen (falls mehrere Province/State) infos vorhanden

full_grouped = full_table.groupby(['Date', 'Country/Region'])['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
full_grouped

### neue Spalten New cases, New deaths and New recovered

import numpy as np 

# new cases 
temp = full_grouped.groupby(['Country/Region', 'Date', ])['Confirmed', 'Deaths', 'Recovered']
temp = temp.sum().diff().reset_index()
mask = temp['Country/Region'] != temp['Country/Region'].shift(1)
temp.loc[mask, 'Confirmed'] = np.nan
temp.loc[mask, 'Deaths'] = np.nan
temp.loc[mask, 'Recovered'] = np.nan
# renaming columns
temp.columns = ['Country/Region', 'Date', 'New cases', 'New deaths', 'New recovered']
# merging new values
full_grouped = pd.merge(full_grouped, temp, on=['Country/Region', 'Date'])
# filling na with 0
full_grouped = full_grouped.fillna(0)
# fixing data types
cols = ['New cases', 'New deaths', 'New recovered']
full_grouped[cols] = full_grouped[cols].astype('int')
# 
full_grouped['New cases'] = full_grouped['New cases'].apply(lambda x: 0 if x<0 else x)

full_grouped.to_csv("JH_Corona_global.csv", index=False)

## Deutschland rausfiltern

Deutschland = full_grouped.loc[full_grouped["Country/Region"] == "Germany"]
Deutschland.to_csv("JH_Corona_Deutschland.csv", index=False)