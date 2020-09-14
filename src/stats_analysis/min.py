import sys
import pandas as pd
videogames = pd.read_csv("../../outputs/clean_metacritic_games.csv")

def min(column):
    """Devuelve el valor mínimo de la columna que se quiere consultar"""
    return print(videogames[column].min())

if __name__ == "__main__":
    min(input("introduce columna: "))