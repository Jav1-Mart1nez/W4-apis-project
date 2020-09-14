import sys
import pandas as pd
videogames = pd.read_csv("../../outputs/clean_metacritic_games.csv")

def max(column):
    """Devuelve el valor máximo de la columna que se quiere consultar"""
    return print(videogames[column].max())

if __name__ == "__main__":
    max(input("introduce columna: "))