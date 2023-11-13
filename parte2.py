import numpy as np
import pandas as pd
from datasets import load_dataset

# Cargamos el dataset
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

# Convertimos el dataset a un DataFrame de Pandas
df = pd.DataFrame(data)

# Obtenemos los índices de las filas con personas que perecieron
dead_indices = df[df["is_dead"] == 1].index

# Creamos un DataFrame con las filas de personas que perecieron
df_dead = df.iloc[dead_indices]

# Creamos un DataFrame con las filas de personas que no perecieron
df_alive = df.drop(dead_indices)

# Calculamos el promedio de edad de las personas que perecieron
mean_age_dead = df_dead["age"].mean()

# Calculamos el promedio de edad de las personas que no perecieron
mean_age_alive = df_alive["age"].mean()

print(mean_age_dead, mean_age_alive)
