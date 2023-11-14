import requests

def download_and_save_csv(url):
  
  # Realizamos el GET request
  response = requests.get(url)

  # Comprobamos si el request fue exitoso
  if response.status_code == 200:
    # Obtenemos el contenido de la respuesta
    data = response.content

    # Creamos un archivo con el nombre especificado
    filename = url.split("/")[-1] + ".csv"
    with open(filename, "wb") as f:
      # Escribimos el contenido en el archivo
      f.write(data)

    # Devolvemos el nombre del archivo creado
    return filename
  else:
    # Imprimimos un error
    print(f"Error al descargar los datos de la URL: {url}")
    return None


# Descargamos los datos
filename = download_and_save_csv("https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv")

# Imprimimos el nombre del archivo creado
print(filename)
