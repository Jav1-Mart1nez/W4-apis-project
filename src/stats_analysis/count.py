import sys
import pandas as pd
videogames = pd.read_csv("../../outputs/clean_metacritic_games.csv")

def count(column):
    """Devuelve la cantida de valores de la columna que se quiere consultar"""
    return print(videogames[column].count())

if __name__ == "__main__":
    count(input("introduce columna: "))
