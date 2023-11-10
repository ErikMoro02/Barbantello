import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dati = pd.read_csv('covid.csv', delimiter=',')

graf=str(input('Inserire nome regione: '))
regione=str(input('Inserire nome regione: '))
dati1=dati[dati['denominazione_regione']==regione]
#dati2=dati[dati['codice_regione']==6]
#print(dati)
x=[i for i in range(len(dati1))]
y=dati1['totale_casi']
#y2=dati2['totale_casi']

plt.plot(x,y, color='black', label=regione)
#plt.plot(x,y2, color='red', label='FVG')
plt.title("Andamento totale casi in {}".format(regione) )
plt.ylabel('Totale Casi')
plt.xlabel('Giorno')
plt.legend()
plt.show()
