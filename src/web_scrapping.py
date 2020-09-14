import json
import urllib
import requests
import pandas as pd
from pandas import json_normalize
import numpy as np
import re

# introducimos las urls.

url1 = "https://rawg.io/api/games?ordering=-released&parent_platforms=7&dates=2020-01-01%2C2020-12-31&page=1&page_size=40&filter=true&comments=true"
url2 = "https://rawg.io/api/games?ordering=-released&parent_platforms=7&dates=2020-01-01%2C2020-12-31&page=2&page_size=40&filter=true&comments=true"
url3 = "https://rawg.io/api/games?ordering=-released&parent_platforms=7&dates=2020-01-01%2C2020-12-31&page=3&page_size=40&filter=true&comments=true"
url4 = "https://rawg.io/api/games?ordering=-released&parent_platforms=7&dates=2020-01-01%2C2020-12-31&page=4&page_size=40&filter=true&comments=true"
url5 = "https://rawg.io/api/games?ordering=-released&parent_platforms=7&dates=2020-01-01%2C2020-12-31&page=5&page_size=40&filter=true&comments=true"

# Hacemos la llamada a la url1.
response = urllib.request.urlopen(url1)
results = json.load(response)

flattened_data = json_normalize(results)
flattened_data1 = json_normalize(flattened_data.results[0])

# Hacemos la llamada a la url2.
response1 = urllib.request.urlopen(url2)
results1 = json.load(response1)

flattened_data2 = json_normalize(results1)
flattened_data3 = json_normalize(flattened_data2.results[0])

# Hacemos la llamada a la url3.
response2 = urllib.request.urlopen(url3)
results2 = json.load(response2)

flattened_data4 = json_normalize(results2)
flattened_data5 = json_normalize(flattened_data4.results[0])

# Hacemos la llamada a la url4.
response3 = urllib.request.urlopen(url4)
results3 = json.load(response3)

flattened_data6 = json_normalize(results3)
flattened_data7 = json_normalize(flattened_data6.results[0])

# Hacemos la llamada a la url5.
response4 = urllib.request.urlopen(url5)
results4 = json.load(response4)

flattened_data8 = json_normalize(results4)
flattened_data9 = json_normalize(flattened_data8.results[0])

# Una vez que hemos obtenido todos los DataFrames, los concatenamos para tener un único DataFrame.
switch2020 = pd.concat([flattened_data1, flattened_data3, flattened_data5, flattened_data7, flattened_data9], axis= 0)

# Comprobamos que columnas tiene nuestro DataFrame y seleccionamos aquellas que queremos.
switch2020.columns
switch2020 = switch2020[["name","platforms","genres","released","metacritic"]]

# Sustituimos los valores NaN por 0.
switch2020.fillna(0)

# Ordenamos los valores por calificación de metacritic en orden descendiente.
switch2020_1 = switch2020.sort_values(by=["metacritic"], ascending=False)

# Redondeamos los valores y seleccionamos las filas cuya calificación es mayor a 70.
switch2020_2 = round(switch2020_1[switch2020_1["metacritic"]>70]).reset_index(drop=True)
switch2020_2["metacritic"] = switch2020_2["metacritic"].astype(int)

# Creamos una nueva columna llamada platform, en la que todos los valores serán Switch.
switch2020_2["platform"] = "Switch"

# Eliminamos la antigua columna platforms
switch2020_3 = switch2020_2.drop(["platforms"], axis=1)

# Ahora vamos a buscar los diferentes géneros dentro de la lista de diccionarios de la columna genres. 
switch2020_3.genres[0:]
switch2020_3["genres"] = pd.DataFrame(str(names[0]["name"])for names in switch2020_3["genres"])

# Modificamos los valores para relacionarlos con el DataFrame obtenido de Kaggle.
switch2020_3["genres"] = switch2020_3["genres"].replace("Shooter", "Action")
switch2020_3["genres"] = switch2020_3["genres"].replace("Indie", "Casual")
switch2020_3["genres"] = switch2020_3["genres"].replace("Racing", "Driving")

# Cambiamos el nombre de algunas columnas y las ordenamos para tener el mismo formato que el DataFrame de Kaggle.
switch2020_3.columns=["game", "genre", "release_date", "metascore","platform"]
switch2020_3 = switch2020_3[["game", "platform", "genre", "release_date", "metascore"]]

# Modificamos cada valor de la columna release_date por 2020.
for value in switch2020_3["release_date"]:
    if "2020" in value:
        switch2020_3["release_date"] = "2020"

# Finalmente exportamos nuestro archivo .csv
switch2020_3.to_csv("../outputs/api_clean_metacritic_games.csv")