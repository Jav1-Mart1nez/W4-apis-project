import argparse
import pandas as pd
import genera_args as gen_a

def main():
    # Importamos el DataFrame que queremos filtrar.
    videogames = pd.read_csv("../outputs/clean_metacritic_games.csv")

    args = gen_a.filtro()
    release_date = args.year
    platform = args.platform
    genre = args.genre
    metascore = args.calification

    # Creamos los condicionales para el filtrado de datos.
    if platform:
        videogames1 = videogames[videogames.platform==args.platform].head()
        if platform not in "Switch, 3DS, WIIU":
            print("no has introducido una plataforma correcta, por favor consulta -help para observar las plataformas disponibles")
    
    if release_date:
        videogames2 = videogames1[videogames1.release_date==args.year].head()
        if release_date<2011 or release_date>2020:
            print("el year debe estar comprendido entre 2011 y 2020 (ambos inclusive)")

    if genre:
        videogames3 = videogames2[videogames2.genre==args.genre].head()
        if genre not in "Action, Role-Playing, Action Adventure, Miscellaneous, Adventure, Puzzle, Strategy, Sports, Simulation, General, Casual, Driving, Platformer, Action RPG, Racing, Fantasy, RPG, Scrolling, Fighting, Breeding/Constructing, Japanese-Style, Other, Sim, Console-style RPG, Sci-Fi, Modern":
            print("no has introducido un género correcto, por favor consulta -help para observar los géneros disponibles") 

    if metascore:
        videogames4 = videogames3[videogames3.metascore==args.calification].head()
        if metascore<71 or metascore>97:
            print("la calification debe estar comprendido entre 71 y 97 (ambos inclusive)")
        print(videogames4)

if __name__ == "__main__":
    main()