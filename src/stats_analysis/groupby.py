import sys
import pandas as pd
import matplotlib.pyplot as plt

videogames = pd.read_csv("../../outputs/clean_metacritic_games.csv")

def groupby(column1, column2):
    """Imprime un Data Frame ordenado a solicitud del cliente"""
    videogames1 = videogames.groupby([column1]).agg({column2: "value_counts"})
    return print(videogames1)

    videogames1.plot.barh(figsize=(15,20), color="slateblue")
    plt.title("nº videojuegos por calificación")
    plt.xlabel("nº videojuegos")
    plt.ylabel("calificacción, plataforma")

if __name__ == "__main__":
    groupby(input("introduce la columna por la que quieres agrupar"), input("introduce la columna de la que quieres contar los valores"))

