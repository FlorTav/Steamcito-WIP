# -*- coding: utf-8 -*-


import pickle


#  Función que valida, que el valor ingresado sea entero
def validate_integer(opcion):
    loop = True
    while loop:
        try:
            opcion = int(opcion)
            loop = False
        except ValueError:
            print "\n\n\tERROR. Debe ingresar sólo valores ENTEROS."
            opcion = raw_input("\n\n\t\tIngrese nuevamente una opción: ")
            loop = True
    return opcion

#  Función que valida, que el valor ingresado pertenezca a un rango de valores que estará determinado por las variables start y end
def validate_range(opcion, start, end):
    while opcion < start or opcion > end:
        print "\n\n\tERROR. Debe ingresar sólo valores VÁLIDOS."
        print "\n\n\tLos valores deben estar comprendidos entre", start, "y", end, "para considerarse una opción válida."
        opcion = raw_input("\n\n\t\tIngrese nuevamente una opción: ")
        opcion = validate_integer(opcion)
    return opcion

#  Función que valida la existencia de un archivo
def validating_existence_file(file_name):
    try:
        object_type_file = open(file_name, "r+")
    except IOError:
        object_type_file = open(file_name, "w+")
    object_type_file.close()
