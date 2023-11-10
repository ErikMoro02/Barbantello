import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dati=data = pd.read_csv('covid.csv', delimiter=',', usecols=(0,2,17))
dati1=dati[dati['codice_regione']==18]
dati2=dati[dati['codice_regione']==6]
#print(dati)
x=[i for i in range(len(dati1))]
y=dati1['totale_casi']
y2=dati2['totale_casi']

plt.plot(x,y, color='black', label='Casi totali')
plt.plot(x,y2, color='red', label='Casi totali')
plt.title('Totale Casi in Calabria')
plt.show()
