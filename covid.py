import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dati=np.loadtxt('covid.csv', delimiter=",", usecols=(0,2,16))
print(dati)
