# Tratamiento de datos
import pandas as pd


def eda_preliminar (df):

    """ 
Realiza un análisis exploratorio preliminar sobre un DataFrame dado.

Este análisis inlcuye:
- Muestra aleatoria de 5 filas del DataFrame.
- Información general del DataFrame (Tipo de datos, nulos, etc,...)
- Porcentaje de valores nulos por columnas
- Conteo de filas duplicadas.
- Distribución de valores para columnas categoricas.

Pareametros:
df (pd.DataFrame): DataFrame a analizar

Returns:
None
"""
    display(df.sample(5))
    print('--------------')

    print('DIMENSIONES')
    print(f'Nuestro conjunto de datos presenta un total de {df.shape[0]} filas y {df.shape[1]} columnas')
    print('--------------')

    print('INFORMACION')
    display(df.info())
    print('--------------')

    print('NULOS')
    nulos_porcentaje = df.isnull().mean()*100
    nulos = nulos_porcentaje[nulos_porcentaje>0].round(2)
    display(nulos)
    print('--------------')

    print('DUPLICADOS')
    print(f'Tenemos un total de {df.duplicated().sum()} duplicados')
    print('--------------')

    print('FRECUENCIA CATEGORICA')
    for col in df.select_dtypes(include ='object').columns:
        print(col.upper())
        print(df[col].value_counts())
        print('--------')
    print('--------------')

    print('DUPLICADOS')
    print(f'Tenemos un total de {df.duplicated().sum()} duplicados')
    print('--------------')

    print('FRECUENCIA CATEGORICA')
    for col in df.select_dtypes(include ='object').columns:
        print(col.upper())
        print(df[col].value_counts())
        print('--------')