import sys
import pandas as pd
videogames = pd.read_csv("../../outputs/clean_metacritic_games.csv")

def describe():
    """Devuelve un resumen estadístico del Data Frame, y lo guarda en un archivo llamado resumen estadístico"""
    original_stdout = sys.stdout 
    with open('../../outputs/describe.txt', 'w') as f:
        sys.stdout = f 
        print("Este es el resumen estadístico de los videojuegos de Nintendo en los últimos 10 años:\n\n",videogames.describe())
        sys.stdout = original_stdout
    
    return print(videogames.describe())

if __name__ == "__main__":
    describe()