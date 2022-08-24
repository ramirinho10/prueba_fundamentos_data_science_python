import pandas as pd # Es una librería orientada a la manipulación y limpieza de estructuras de datos.
import numpy as np # Es una librería orientada a la computación científica.
import scipy.stats as stats # Esta librería contiene un y nos ayuda a generar distribuciones

import matplotlib.pyplot as plt # Esta librería nos ayudará a generar gráficos.
import seaborn as sns # Esta librería podremos generar gráficos elegantes y se complementa con matplotlib.

import scipy.stats as stats # Es una libreria que sirve para simular y generar distribuciones.
from sklearn.preprocessing import LabelEncoder # Es una librería y podremos recodificar variables.
from sklearn.model_selection import train_test_split # Generamos los subset para entrenamiento y testeo del modelo.
from sklearn.preprocessing import StandardScaler # Esta librería nos sirve para estendarizar datos. from sklearn.metrics import confusion_matrix # Esta librería nos sirve para generar la matriz de confusión, una metrica.

import statsmodels.api as sm # podremos generar un modelo
import statsmodels.formula.api as smf # librería que sirve para crear modelos Logistico o Regresion

import warnings # Esta es una librería que muestra los warning.
warnings.filterwarnings("ignore", category=DeprecationWarning) # con esto se evita que genere warnings de metodos o funciones desactualizadas.

import missingno as msngo

#Funcion para realizar graficos de barra para variables discretas de mi df

def grafico_barra(df, var):
    df[var].value_counts().plot(kind="bar");
    plt.ylabel("Frecuencia");
    plt.xlabel("Categoria");
    plt.title(f"{var}");


#Funcion para realizar graficos histogramas para variables continuas de mi df

def plot_hist(df, var, true_mean=False):
    plt.hist(df[var].dropna())
    plt.title(var)
    plt.xlabel("Valores")                 
    plt.ylabel("Frecuencia")
    
    if true_mean:
        plt.axvline(df[var].mean(), color="red", label=f"Promedio de {var}")
    
    plt.legend()


def fetch_descriptives(df, var):
    print(f"La media de {var} es {df[var].mean()}")
    print(f"La mediana de {var} es {df[var].median()}")
    print(f"La moda de {var} es {stats.mode(df[var])[0]} y su frec es {stats.mode(df[var])[1]}")
    print(f"La desviacion estandar es {np.std(df[var])}")