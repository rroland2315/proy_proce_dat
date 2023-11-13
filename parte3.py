from datasets import load_dataset
import numpy as np
import pandas as pd

# Cargamos el dataset
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

# Convertimos el dataset a un DataFrame de Pandas
df = pd.DataFrame(data)

# Verificamos los tipos de datos de cada columna
for col in df.columns:
  print(f"Columna: {col} - Tipo de dato: {df[col].dtype}")

# Definimos la función para calcular la cantidad de hombres fumadores vs mujeres fumadoras
def count_smokers(df):
  """
  Calcula la cantidad de hombres fumadores vs mujeres fumadoras.

  Args:
    df: El DataFrame sobre el que se calcularán las cantidades.

  Returns:
    Un diccionario con las cantidades de hombres y mujeres fumadoras.
  """

  # Obtenemos los índices de las filas con hombres
  male_indices = df[df["is_male"] == True].index

  # Creamos un DataFrame con las filas de hombres
  df_male = df.iloc[male_indices]

  # Obtenemos los índices de las filas con mujeres
  female_indices = df[df["is_male"] == False].index

  # Creamos un DataFrame con las filas de mujeres
  df_female = df.iloc[female_indices]

  # Calculamos la cantidad de hombres fumadores
  count_male_smokers = df_male["is_smoker"].sum()

  # Calculamos la cantidad de mujeres fumadoras
  count_female_smokers = df_female["is_smoker"].sum()

  # Devolvemos un diccionario con las cantidades
  return {"hombres": count_male_smokers, "mujeres": count_female_smokers}


# Calculamos las cantidades
counts = count_smokers(df)

# Imprimimos las cantidades
print(counts)
