#Dentro de la carpeta Scripts cree un programa llamado res_estadistico.py que reciba como input 
# desde la consola un archivo csv con un solo conjunto de datos, y retorne como resultado un 
# resumen estadístico que incluya los siguientes:
#indicadores: Tamaño de la muestra, Media, Mediana, Cuartil 1, Cuartil 2, Rango Interquartil 
import pandas as pd 
import argparse

# Modelo de argumentos
parser = argparse.ArgumentParser()

#argumentos a ser llamados 
parser.add_argument("https://raw.githubusercontent.com/jsaraujott/datos/main/datos.csv", type=str)

#Transformación a Python
args = parser.parse_args()

#Proceso del programa
datos = pd.read_csv("https://raw.githubusercontent.com/jsaraujott/datos/main/datos.csv", header=None)

serie = datos.iloc[:,0]

n = serie.count() #serie.shape[0]
prom = serie.mean()
med = serie.median()
q1 = serie.quantile(0.25)
q3 = serie.quantile(0.75)
iqr = q3 - q1 

resumen = pd.DataFrame({"n":n, "Promedio":round(prom,1), "Mediana":round(med, 1), "Cuartil_1":round(q1, 1), "Cuartil_3":round(q3, 1), "IRQ":round(iqr, 1)}, index = [""])

print(resumen)





