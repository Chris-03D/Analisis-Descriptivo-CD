# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1P-opbZFM1c4r9NTt7u--wqjJuQul7P79

# Cristian Ducuara
# Katherin Martin
"""

import numpy as np
import pandas as pd

"""Para el analisis de los siguientes datos nos realizaremos la siguiente pregunta. ¿COMNO ESTAN DESTINADOS LOS SUBSIDIOS EN LA POBLACION DE COLOMBIA?

En el siguiente codigo analizaremos cuantas filas y columnas tiene nuestro dataframe
"""

df = pd.read_csv('/content/Subsidios_De_Vivienda_Asignados_20240911.csv')

print(df.shape)

"""A lo largo de este analisis iremos mostrando las 5 primeras filas y las 5 primeras columnas del dataframe."""

df.head()

"""Para enfocarnos mas a nuestra prengunta revisaremos cual es estado de los diferentes subsidios asignados a la poblacion de colombia."""

df['Estado de Postulación'].value_counts()

"""En el siguiente codigo analizaremos cuales fueron los 5 departamentos con los mayores valores asignados."""

df.sort_values(by='Valor Asignado',ascending=False)[['Departamento', 'Valor Asignado']].head(5)

"""En el siguiente codigo analizaremos cuales fueron los 5 departamentos con los menores valores asignados."""

df.sort_values(by='Valor Asignado',ascending=True)[['Departamento', 'Valor Asignado']].head(5)

"""En el siguiente codigo analizaremos en que años fueron los 5 subsidios mayores valores asignados y en donde."""

df.sort_values(by='Año de Asignación',ascending=False)[['Valor Asignado', 'Departamento', 'Año de Asignación']].head(5)

"""En el siguiente codigo analizaremos en que años fueron los 5 subsidios menores valores asignados y en donde."""

df.sort_values(by='Año de Asignación',ascending=True)[['Valor Asignado', 'Departamento', 'Año de Asignación']].head(5)

