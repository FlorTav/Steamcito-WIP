# -*- coding: utf-8 -*-

# NOMBRE - PRECIO - DEV - EDITOR - FECHA - GENERO

import sys

sys.path.append("python-modules")

from tools.validate.validate import *
from tools.view.view import *

validating_existence_file("catalogo_juegos.dat")

def corregir_nombre(lista_original):
    tope = len(lista_original) - 5
    contador = 0
    nombre = ""
    while contador < tope:
        nombre += lista_original[contador]
        if contador != tope - 1:
            nombre += " "
        contador += 1
    return nombre

def corregir_lista(lista_original):

    lista = []
    if len(lista_original) != 6:
        nombre = corregir_nombre(lista_original)
        lista.append(nombre)
    tope = len(lista_original) - 5
    while tope != len(lista_original):
        lista.append(lista_original[tope])
        tope += 1
    return lista

with open("juegoslista.txt") as texto:
    contador = 1
    juegos = {}
    juegos = loading_file_into_memory("catalogo_juegos.dat")
    for line in texto:
        raw_list = line.split()
        if len(raw_list) != 6:
            lista = corregir_lista(raw_list)
            juegos[contador] = lista
            contador += 1
        else:
            juegos[contador] = raw_list
            contador += 1
saving_changes_to_the_file("catalogo_juegos.dat", juegos)
print "La carga ha terminado."   

