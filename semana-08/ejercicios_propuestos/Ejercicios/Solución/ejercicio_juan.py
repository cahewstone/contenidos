import json
import pickle
import random


class Pelicula:

    def __init__(self, title=None, category_name=None, release_year=None, running_time=None):

        self.title = title
        self.category_name = category_name
        self.release_year = release_year
        self.running_time = running_time

    def __getstate__(self):
        with open("opiniones.pkl", "rb") as file:
            opiniones = pickle.load(file)

        opinion = random.choice(opiniones)
        new = self.__dict__.copy()
        new.update({"opinion": opinion})

        return new


def hook_peliculas(peliculas):
    with open("caracteristicas.pkl", "rb") as file:
        caracteristicas = pickle.load(file)
    filtrado = {c: peliculas[c] for c in caracteristicas}

    return Pelicula(**filtrado)


def cargar_peliculas():
    with open("movies.json", encoding="utf-8") as file:
        return json.load(file, object_hook=hook_peliculas)


def recomendar_peliculas(peliculas):
    with open("recomendacion.pkl", "wb") as file:
        for p in peliculas:
            pickle.dump(p, file)


# Main code
peliculas = cargar_peliculas()
recomendar_peliculas(peliculas)

"""
El siguiente código puede ser descomentado y corrido para comprobar que se realizo el ejercicio
correctamente. Deberían imprimirse diccionarios por pelicula, con todas las caracteristicas de cada
pelicula del archivo caracteristicas.pkl como keys y key "opinion" que tiene como value
alguna de las tres opiniones del archivo opiniones.pkl. Tiene que ser corrido en este archivo.
"""

# with open("recomendacion.pkl", "rb") as file:
#     peliculas_recomendadas = list()
#     while True:
#         try:
#             peliculas_recomendadas.append(pickle.load(file))
#         except EOFError:
#             break
# for p in peliculas_recomendadas:
#     print(p.__dict__)
