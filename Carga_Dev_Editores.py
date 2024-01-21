# -*- coding: utf-8 -*-

import sys

sys.path.append("python-modules")

from tools.validate.validate import *
from tools.view.view import *

def get_pair(line):
    key, sep, value = line.strip().partition(" ")
    #Strip remueve espacios al final o al comienzo del string
    #Partition arma una tupla con los vaores separados por " "
    return int(key), value

validating_existence_file("desarrolladores.dat")
validating_existence_file("editores.dat")
developers = {}
publisher  = {}
developers = loading_file_into_memory("desarrolladores.dat")
with open("devs.txt") as texto:
    developers = dict(get_pair(line) for line in texto) 
#arma un diccionario con los valores que devuelve la funcion
publisher = loading_file_into_memory("editores.dat")
with open("editores.txt") as texto:
    publisher = dict(get_pair(line) for line in texto)    
saving_changes_to_the_file("desarrolladores.dat", developers)
saving_changes_to_the_file("editores.dat", publisher)
print "El proceso ha terminado."