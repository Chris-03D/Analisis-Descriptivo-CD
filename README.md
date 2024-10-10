[README.md](https://github.com/user-attachments/files/17321846/README.md)# ANALISIS DESCRIPTVO
Este repositorio contiene un análisis descriptivo realizado con Python enmarcado en el
proyecto de aula del curso Introducción a la adquisición y tratamiento de datos del
programa de Ingeniería Informática de Aunar Villavicencio.
El objetivo es explorar y visualizar datos utilizando técnicas estadísticas básicas para
obtener información relevante.

`Tabla de contenido`
1. Fundamentos para el Análisis de Datos.
2. Análisis Exploratorio: Tipos de datos
3. Análisis Descriptivo: Medidas de tendencia central
    * Media Aritmética
    * Media Geométrica
    * Media Armónica
    * Media Ponderada
    * Mediana
    * Moda
    * Error típico o desviación estándar
4. Visualización de datos: 
    * Gráfico de barras
    * Gráfico circular
    * Histogramas
    * Boxplot
    * Scatterplot
    * Gráficos de dispersión 
5. Aplicación
`Tecnologias utilizadas`
> Python
![alt text](https://i.redd.it/rxezjyf4ojx41.png)
>Bibliotecas
| Modulos       | concepto |
| ------------- |:------------|
|Pandas        |Para la manipulación y análisis de datos|
| Numpy         |Para cálculos numéricos|
| Matplotlib    |Para visualización de datos|
| seaborn       |Para visualización de datos|
| Scipy         |Para cálculos estadísticos|
| Statsmodels   |Para cálculos estadísticos|
> **Pandas**
```python
import pandas as pd
# Crear un DataFrame simple
data = {'Nombre': ['Alejandro', 'Camila', 'Juan'],
        'Edad': [21, 22, 23],
        'Ciudad': ['Villavicencio', 'Bogotá', 'Cali']}
df = pd.DataFrame(data)
# Mostrar el DataFrame
print(df)
# Operaciones básicas
print("Media de las edades:", df['Edad'].mean())  # Media de la columna 'Edad'
print("Filtrar por Edad > 21:", df[df['Edad'] > 21])  # Filtrar filas donde Edad > 21
```
> **Numpy**
```python
import numpy as np
# Crear un array de Numpy
arr = np.array([1, 2, 3, 4, 5])
# Operaciones básicas
print("Suma de los elementos:", np.sum(arr))
print("Media de los elementos:", np.mean(arr))
print("Elemento máximo:", np.max(arr))
```
> **Matplotlib**
```python
import matplotlib.pyplot as plt
# Datos simples
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
# Crear un gráfico de línea
plt.plot(x, y, label='Línea de ejemplo')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de Línea')
plt.legend()
plt.show()
```
> **Seaborn**
```python
import seaborn as sns
import matplotlib.pyplot as plt
# Crear un DataFrame simple
data = sns.load_dataset("iris")
# Crear un gráfico de dispersión (scatterplot)
sns.scatterplot(x='sepal_length', y='sepal_width', data=data)
plt.title('Gráfico de Dispersión de Iris')
plt.show()
```
> **Scipy**
```python
from scipy import stats
# Datos
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# Calcular la media, mediana y moda
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)
print("Media:", mean)
print("Mediana:", median)
print("Moda:", mode)
```
> **Statsmodels**
```python
import statsmodels.api as sm
# Datos de ejemplo
X = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
# Agregar constante a X (para la intersección del modelo)
X = sm.add_constant(X)
# Ajustar un modelo de regresión lineal
model = sm.OLS(y, X)
results = model.fit()
# Ver los resultados del resumen
print(results.summary())
```



















