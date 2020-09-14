import sys
import argparse
import pandas as pd

def filtro():

    # Creamos el parser.
    my_parser = argparse.ArgumentParser(description="Imprime el DataFrame filtrado")
    
    # Agragamos los diferentes argumentos por los que queremos filtrar.
    my_parser.add_argument("-platform", dest="platform",
            default="Switch",
            type=str,
            required=True,
            help="Introduce una de las siguientes plataformas: Switch, 3DS, WIIU")   
    
    my_parser.add_argument("-year", dest="year",
        default=2011,
        type=int,
        required=True,
        help="Introduce un year comprendido entre 2011 y 2020 (ambos inclusive)")

    my_parser.add_argument("-genre", dest="genre",
        default="Action",
        type=str,
        required=True,
        help="""Introduce uno de los siguientes géneros:
        Action,
        Role-Playing,
        Action Adventure,
        Miscellaneous,
        Adventure,
        Puzzle,
        Strategy,
        Sports,
        Simulation,
        General,
        Casual,
        Driving,
        Platformer,
        Action RPG,
        Racing,
        Fantasy,
        RPG,
        Scrolling,
        Fighting,
        Breeding/Constructing,
        Japanese-Style,
        Other,
        Sim,
        Console-style RPG,
        Sci-Fi,
        Modern""")

    my_parser.add_argument("-calification", dest="calification",
        default=71,
        type=int,
        required=True,
        help="Introduce una calification comprendido entre 71 y 97 (ambos inclusive)")

    # Ejecutamos el parse_args()
    args = my_parser.parse_args()
    return args



