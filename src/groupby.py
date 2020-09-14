import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

videogames = pd.read_csv("../outputs/clean_metacritic_games.csv")

def groupby(column1, column2):
    """Devuelve un pd.Series ordenado a solicitud del cliente por la terminal, un diágrama de barras del 
    pd.Series en cuestión, un diagrama de caja de la column1, y un archivo de texto con el pd.Series"""
    videogames1 = videogames.groupby([column1]).agg({column2: "value_counts"})
    videogames1.plot.barh(figsize=(15,20), color="slateblue")
    plt.title(f"relation {column1}, {column2}")
    plt.xlabel("quantity")
    plt.ylabel(f"{column1}, {column2}")
    plt.savefig("../outputs/barh.png")
    plt.figure(figsize=(15,5))
    sns.boxplot([videogames[column1]], color="seagreen")
    plt.title(f"{column1}")
    plt.xlabel("quantity")
    plt.savefig("../outputs/box.png")
    
    original_stdout = sys.stdout 
    with open('../outputs/groupby.txt', 'w') as f:
        sys.stdout = f 
        print("Nintendo en los últimos 10 años:\n\n",videogames1.sort_values(by=["metascore"], ascending=False).head())
        sys.stdout = original_stdout

    return print(videogames1.sort_values(by=["metascore"], ascending=False).head())

column1 = input("Introduce la columna por la que quieres agrupar: ")
column2 = input("introduce la columna de la que quieres contar los valores: ")

groupby(column1, column2)