# -*- coding: utf-8 -*-


import sys
import pickle

sys.path.append("python-modules")

from tools.validate.validate import *
from tools.view.view import *

validating_existence_file("catalogo_juegos.dat")
validating_existence_file("desarrolladores.dat")
validating_existence_file("editores.dat")
juegos = loading_file_into_memory("catalogo_juegos.dat")
devs = loading_file_into_memory("desarrolladores.dat")
editores = loading_file_into_memory("editores.dat")

generos = ["Acción", "Aventura", "Cartas", "Cooperativo", "FPS", "Lucha", "Metroidvania", "Plataformas", "Roguelike", "RPG", "Sigilo", "Simulación", "Supervivencia", "Terror", "Zombies"]

menu_bus = ("\nMenu Busqueda de Juegos.\n\n \n\t1. Buscar juego por nombre. \n\t2. Buscar juego por desarrollador. \n\t3. Buscar juego por distribuidor. \n\t4. Buscar for genero. \n\t5. Salir del programa.")

def menu_busqueda():
    cleaning()
    print menu_bus
    seleccion = raw_input("\n\n\t\tIngrese una opción: ")
    seleccion = validate_integer(seleccion)
    seleccion = validate_range(seleccion, 1, 5)
    return seleccion

def busqueda_nombre(juegos, corte):
    
    while corte == 1:
        cleaning()
        print "\n\tBuscar juego por nombre.\n"
        for juego_id, datos in juegos.items():
            print juego_id, ".", datos[0]   
        seleccion = raw_input("\nSeleccione el juego que desea ver: ")
        seleccion = validate_integer(seleccion)
        if seleccion in juegos.keys():
            cleaning()
            temporal = juegos[seleccion]
            cod_dev = int(temporal[2])
            cod_ed = int(temporal[3])
            print "ID: ", seleccion
            print "Nombre: ", temporal[0]
            print "Precio: ", temporal[1]
            print "Genero: ", temporal[5]
            print "Desarrollador: ", devs[cod_dev]
            print "Editor: ", editores[cod_ed]
            print "Fecha de lanzamiento: ", temporal[4]
        else:
            print "\nEl ID ingresado no se encuentra en la base de datos."
        raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")
        corte = raw_input("\n\t¿Desea seguir buscando juegos? \n\n1.Si \n\n0.No")
        corte = validate_integer(corte)
        corte = validate_range(corte, 0, 1)
 
def busqueda_dev(juegos):
    cleaning()
    print "\n\tBuscar juego por desarrollades.\n"
    for cod_dev, nombre in devs.iteritems():
        print cod_dev, ".", nombre
    seleccion = raw_input("\nIngrese el codigo del desarrollador: ")
    seleccion = validate_integer(seleccion)
    seleccion = validate_range(seleccion, 1, 74)
    cleaning()
    print "\tJuegos publicados por ", devs[seleccion], ": "
    bandera = False
    for juego_id, datos in juegos.items():
        if seleccion == int(datos[2]):
            band = True
            print "ID: ", juego_id
            print "Nombre: ", datos[0]
            print "Precio: ", datos[1]
            print "\n"
    if not band:
        cleaning()
        print "No existe ningún juego bajo el desarrollador seleccionado en nuestra base de datos."
    raw_input("\n\n\t\t\t\tPresione ENTER para continuar.")  

def busqueda_genero(juegos):
    
    cleaning()
    print "\n\tBuscar juego por genero.\n"
    contador = 1
    for dato in generos:
        print contador, ".", dato
        contador += 1
    seleccion = raw_input("\nSeleccione el genero que desea ver: ")
    seleccion = validate_integer(seleccion)
    seleccion = validate_range(seleccion, 1, 15)
    cleaning()
    for juego_id, datos in juegos.items():
        if generos[seleccion - 1] == datos[5]:
            print "ID: ", juego_id
            print "Nombre: ", datos[0]
            print "Precio: ", datos[1]
            print "\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def busqueda_editor(editores):
        
    cleaning()
    for cod_ed, nombre in editores.items():
        print cod_ed, ".", nombre
    seleccion = raw_input("\nSeleccione el editor que desea ver: ")
    seleccion = validate_integer(seleccion)
    seleccion = validate_range(seleccion, 1, 59)
    cleaning()
    print "\tJuegos publicados por ", editores[seleccion], ": "
    validacion = str(seleccion)
    bandera = False
    for juego_id, datos in juegos.items():
        if seleccion == int(datos[3]):
            bandera = True
            print "ID: ", juego_id
            print "Nombre: ", datos[0]
            print "Precio: ", datos[1]
            print "\n"   
    if not bandera:
        cleaning()
        print "No existe ningún juego bajo el distribuidor seleccionado en nuestra base de datos."
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

seleccion = menu_busqueda()
while seleccion != 5:
    if seleccion == 1:
        busqueda_nombre(juegos, 1)
    elif seleccion == 2:
        busqueda_dev(juegos)
    elif seleccion == 3:
        busqueda_editor(juegos)
    else:
        busqueda_genero(juegos)
    seleccion = menu_busqueda()
cleaning()
raw_input("\n\tUsted ha salido exitosamente del sistema.\n\n\t\t\tPresione ENTER para continuar")
cleaning()    