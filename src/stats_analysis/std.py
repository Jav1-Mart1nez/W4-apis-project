import sys
import pandas as pd
videogames = pd.read_csv("../../outputs/clean_metacritic_games.csv")

def std(column):
    """Devuelve la desviación estandar de la columna que se quiere consultar"""
    return print(videogames[column].std())

if __name__ == "__main__":
    std(input("introduce columna: "))