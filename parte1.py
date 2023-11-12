import numpy as np
from datasets import load_dataset

# Cargar el dataset
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

# Obtener la lista de edades
ages = np.array(data['age'])

# Calcular el promedio de edades
average_age = np.mean(ages)

print(f"El promedio de edad de las personas en el estudio es: {average_age} años")
