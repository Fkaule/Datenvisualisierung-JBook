# Daten erzeugen (kleiner df)

import numpy as np
import pandas as pd

# Steifigkeiten
c1 = 0.55 # N/mm
c2 = 0.6 # N/mmh
c3 = 0.9 # N/mm
Federsteifigkeiten=[c1,c2,c3]

#Weg
Weglaenge = 10 # mm
Wegschritt = 2.5 # mm
Weg = np.arange(0, Weglaenge+Wegschritt, Wegschritt)

# Rauschen pro Messung 
M_mu, M_sigma = 0, 0.1 # Mittelwert und Standardabweichung für Rauschen Person 1

Anz_Messung=5

for j in range(len(Federsteifigkeiten)):

    Feder = j + 1 # Variable fuer Speichern der Textdatei
    Kraft = np.linspace(0, Weglaenge*Federsteifigkeiten[j], int(Weglaenge/Wegschritt)+1) # Kraftwerte bestimmen

    for i in range(Anz_Messung):

        Messung = i + 1              
        Noise = np.random.normal(M_mu, M_sigma, int(Weglaenge/Wegschritt)+1) # Rauschen des Kraftsensors
        
        # Daten erzeugen

        Kraftmessung = Kraft + Noise
        Kraftmessung[0] = 0 # ersten Wert Null setzen
        Kraftmessung = np.around(Kraftmessung, 1) # Werte runden
        Kraftmessung

        # in Dataframe speichern
        df=pd.DataFrame(Kraftmessung,Weg)
        df.reset_index(level=0, inplace=True)
        df.rename(columns = {"index":"Weg (mm)",
                            0:"Kraft (N)"},
                    inplace=True)

        # als csv exportieren
        filename_1='Feder_'
        filename_2='Messung_'
        
        filename=filename_1+str(Feder)+'-'+filename_2+str(Messung)+'.csv'
        df.to_csv (filename, index = False, header=True)


# Daten erzeugen (großer df)


import numpy as np
import pandas as pd
import glob # Zur Bestimmung der Liste an Dateien nach Suchschema

# Steifigkeiten
c1 = 0.55 # N/mm
c2 = 0.6 # N/mmh
c3 = 0.9 # N/mm
Federsteifigkeiten=[c1,c2,c3]

#Weg
Weglaenge = 10 # mm
Wegschritt = 2.5 # mm
Weg = np.arange(0, Weglaenge+Wegschritt, Wegschritt)

# Rauschen Kraftmessdose
F1_mu, F1_sigma = 0, 0.1 # Mittelwert und Standardabweichung für Rauschen Kraftmessdose 1
F2_mu, F2_sigma = 0.5, 1.5 # Mittelwert und Standardabweichung für Rauschen Kraftmessdose 2
F_mu=[F1_mu,F2_mu]
F_sigma=[F1_sigma,F2_sigma]

# Rauschen Person
P1_mu, P1_sigma = 0, 0.05 # Mittelwert und Standardabweichung für Rauschen Person 1 (Clara)
P2_mu, P2_sigma = 0, 1.5 # Mittelwert und Standardabweichung für Rauschen Person 2 (Peter)
P_mu=[P1_mu,P2_mu]
P_sigma=[P1_sigma,P2_sigma]
Person=["Clara","Peter"]

# Rauschen pro Messung 
M_mu, M_sigma = 0, 0.1 # Mittelwert und Standardabweichung für Rauschen Person 1

Anz_Messung=25

for j in range(len(Federsteifigkeiten)):

    Feder = j + 1 # Variable fuer Speichern der Textdatei
    Kraft = np.linspace(0, Weglaenge*Federsteifigkeiten[j], int(Weglaenge/Wegschritt)+1) # Kraftwerte bestimmen


    for m in range(len(P_mu)):

        #Person = m + 1 # Variable fuer Speichern der Textdatei
    
        for k in range(len(F_mu)):

            Kraftmessdose = k + 1 # Variable fuer Speichern der Textdatei

            for i in range(Anz_Messung):

                Messung = i + 1              
                Noise = np.random.normal((M_mu+P_mu[m]+F_mu[k]), (M_sigma+P_sigma[m]+F_sigma[k]), int(Weglaenge/Wegschritt)+1) # Rauschen des Kraftsensors
                
                # Daten erzeugen

                Kraftmessung = Kraft + Noise
                Kraftmessung[0] = 0 # ersten Wert Null setzen
                Kraftmessung = np.around(Kraftmessung, 1) # Werte runden
                Kraftmessung

                # in Dataframe speichern
                df=pd.DataFrame(Kraftmessung,Weg)
                df.reset_index(level=0, inplace=True)
                df.rename(columns = {"index":"Weg (mm)",
                                    0:"Kraft (N)"},
                            inplace=True)

                # als csv exportieren
                filename_1='Big_Feder_'
                filename_2='Person_'
                filename_3='Messdose_'
                filename_4='Messung_'
                
                filename=filename_1+str(Feder)+'-'+filename_2+Person[m]+'-'+filename_3+str(Kraftmessdose)+'-'+filename_4+str(Messung)+'.csv'
                df.to_csv (filename, index = False, header=True)
