import sys
import pandas as pd
videogames = pd.read_csv("../../outputs/clean_metacritic_games.csv")

def mean(column):
    """Devuelve la media de la columna que se quiere consultar"""
    return print(videogames[column].mean())

if __name__ == "__main__":
    mean(input("introduce columna: "))