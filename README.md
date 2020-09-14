# Apis-Project

![nintendo](inputs/nintendo.png) 

El objetivo de este proyecto es emplear todos los conocimientos adquiridos hasta ahora.   


## Análisis.

Se ha realizado el ánalisis de los videojuegos lanzados para plataformas Nintendo en los 10 últimos años.


## Como se ha realizado.
 
 Se ha importado una extensa base de datos con todos los videojuegos lanzados para todas las plataformas desde el año 2011 hasta el año 2019. El archivo .csv de la base de datos  ha sido descargado del siguiente enlace, https://www.kaggle.com/skateddu/metacritic-games-stats-20112019

Para realizar la limpieza y manipulación de los datos para la obtención del DataFrames, he importado el módulo Panda y he realizado la limpieza  en un archivo .ipynb.

Posteriormente se ha realizado el scrapping seleccionado las siguientes API´s de la página https://https://rawg.io/:

    - https://rawg.io/api/games?ordering=-released&parent_platforms=7&dates=2020-01-01%2C2020-12-31&page=1&page_size=40&filter=true&comments=true
    - https://rawg.io/api/games?ordering=-released&parent_platforms=7&dates=2020-01-01%2C2020-12-31&page=2&page_size=40&filter=true&comments=true
    - https://rawg.io/api/games?ordering=-released&parent_platforms=7&dates=2020-01-01%2C2020-12-31&page=3&page_size=40&filter=true&comments=true
    - https://rawg.io/api/games?ordering=-released&parent_platforms=7&dates=2020-01-01%2C2020-12-31&page=4&page_size=40&filter=true&comments=true
    - https://rawg.io/api/games?ordering=-released&parent_platforms=7&dates=2020-01-01%2C2020-12-31&page=5&page_size=40&filter=true&comments=true

Una vez filtrado el DataFrame, se ha concatenado con el DataFrame obtenido de Kaggle.

Se han generado una serie de archivos .py para el filtrado de datos y obtención de datos estadísticos.

Finalmente se han obtenido una serie de archivos .png y .txt por terminal que posteriormente se han empleado para la creación de un archivo .pdf.


## Conclusión.

### Ánalisis lanzamientos en plataformas de Nintendo

Del ánalisis realizado, se observa que la gran mayoría de los videojuegos lanzados para la plataforma Nintendo tienen unas calificaciones entre 75 y 83 puntos.

![box](ouputs/box.png) 

Las plataformas de Nintendo con videojuegos de mayor puntuación son las siguientes:

    - Switch: 406
    - 3DS: 208
    - WIIU: 121

![barh](ouputs/barh.png) 

Los mejores videojuegos lanzados por Nintendo en los últimos 10 años son hasta el momento:

    - The legend of Zelda: Breath of the Wild.
    - Super Mario Odyssey.
    
Estos dos videojuegos pertenecen a Nintendo Switch y curiosamente, han sido desarrollados por la propia compañía.
