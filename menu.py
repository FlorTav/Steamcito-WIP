# -*- coding: utf-8 -*-


import sys
import pickle

sys.path.append("python-modules")

from tools.validate.validate import *
from tools.view.view import *

validating_existence_file("usuarios.dat")

# este diccionario tendra una clave = int y los valores seran de tipo lista = str
# la clave sera el id de usuario
# la lista tendra guardado el correo, nombre completo, n° de telefono, pais, fecha de nacimiento

usuarios = {}
menu_prin = ("\nSistema de Steamcito.\n\nMenú Principal.\n\n \n\t1. Usuario. \n\t2. Tienda. \n\t3. Salir.")
menu_usa = ("\nMenú de GESTIÓN de USUARIOS.\n\n \n\t1. Registro. \n\t2. Buscar usuario. \n\t3. Modificar usuario. \n\t4. Desactivar usuario. \n\t5. Reactivar usuario. \n\t6. Regresar al menú principal.")

def menu_principal():
    cleaning()
    print menu_prin
    opcion = raw_input("\n\n\t\tIngrese una opción: ")
    opcion = validate_integer(opcion)
    opcion = validate_range(opcion, 1, 3)
    return opcion
    
def menu_usuario():
    cleaning()
    print menu_usa
    opcion = raw_input("\n\n\t\tIngrese una opción: ")
    opcion = validate_integer(opcion)
    opcion = validate_range(opcion, 1, 6)
    return opcion

def registro_usuario(base):
    cleaning()
    print "\nRegistre el Usuario.\n\n"
    id_usuario = raw_input("\nIngrese el ID del usuario: ")
    id_usuario = validate_integer(id_usuario) 
    if id_usuario not in base.keys():
        cleaning()
        print "\n\tRellene los campos con la informacion correspondiente al Usuario.\n"
        temporal = []
        dato = raw_input("\nIngrese el nombre de usuario: ")
        temporal.append(dato)
        dato = raw_input("\nIngrese su nombre: ").capitalize()
        temporal.append(dato)
        dato = raw_input("\nIngrese su apellido: ").capitalize()
        temporal.append(dato)
        dato = raw_input("\nIngrese su correo electrónico: ")
        temporal.append(dato)
        dato = raw_input("\nIngrese su fecha de nacimiento(formato DDMMYY):")
        dato = validate_integer(dato)
        temporal.append(dato)
        dato = raw_input("\nIngrese su país de residencia:  ").capitalize()
        temporal.append(dato)
        dato = True
        temporal.append(dato)
        usuarios[id_usuario] = temporal
        cleaning()
        print "El usuario se registro de forma exitosa."
    else:
        print "El usuario ya se encuentra en el sistema."
    raw_input("\n\n\t\t\t\tPresione ENTER para continuar")
    
def mostrar_datos(usuarios, id_usuario):
    
    temporal = usuarios[id_usuario]
    print "\nLos datos de usuarios buscados son:\n"
    print "\n\t\tId usuario: ", id_usuario
    print "\n\t\tNombre de usuario: ", temporal[0]
    print "\n\t\tNombre completo: ", temporal[1], " ", temporal[2]
    print "\n\t\tCorreo Electronico: ", temporal[3]
    print "\n\t\tFecha de nacimiento: ", temporal[4]
    print "\n\t\tPais: ", temporal[5]
    if temporal[6] == True:
        print "\n\t\tEl usuario se encuentra activo."
    else:
        print "\n\t\tEl usuario se encuentra inactivo."
        
def mostrar_datos_modif(usuarios, id_usuario):
    temporal = usuarios[id_usuario]
    print "\nLos datos del usuario a modificar son:\n"
    print "\n\t\tID usuario: ", id_usuario
    print "\n\t\t1. Nombre de usuario: ", temporal[0]
    print "\n\t\t2. Nombre: ", temporal[1]
    print "\n\t\t3. Apellido: ", temporal[2]
    print "\n\t\t4. Correo Electronico: ", temporal[3]
    print "\n\t\t5. Fecha de nacimiento: ", temporal[4]
    print "\n\t\t6. Pais: ", temporal[5]


def buscar_usuario(base):
    cleaning()
    print "\nBuscar Usuario.\n\n"
    id_usuario = raw_input("\n\t\tIngrese el ID del usuario que desea buscar: ")
    id_usuario = validate_integer(id_usuario)
    cleaning()
    if id_usuario in base.keys():
        mostrar_datos(usuarios, id_usuario)
    else:
        print "\nEl usuario N°", id_usuario, "que desea buscar NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")


def modificar_usuario(base):
    cleaning()
    print "\nModificar Usuario.\n\n"
    id_usuario = raw_input("\n\t\tIngrese el nombre del usuario que desea modificar: ")
    id_usuario = validate_integer(id_usuario)
    cleaning()
    if id_usuario in base.keys():
        if base[id_usuario][6] == True:
            temporal = usuarios[id_usuario]
            mostrar_datos_modif(usuarios, id_usuario)
            print "\n\n\n\t\t7. Salir SIN MODIFICAR DATOS del Usuario."
            atributo = raw_input("\n\n\t\tIngrese una opción: ")
            atributo = validate_integer(atributo)
            atributo = validate_range(atributo, 1, 7)
            cleaning()
            if atributo != 7:
                msje = "Ingrese "
                etiquetas = ["Nombre de usuario: ", "Nombre: ", "Apellido: ", "Correo Electronico" , "Fecha de Nacimiento: ", "País: "]
                msje = msje + etiquetas[atributo - 1]
                dato = raw_input(msje)
                if atributo == 5:
                    dato = validate_integer(dato)
                temporal[atributo - 1] = dato
                usuarios[id_usuario] = temporal
                cleaning()
                saving_changes_to_the_file("usuarios.dat", usuarios)
                print "\n\t\tEl Usuario ha sido modificado exitosamente."
            else:
                print "\n\t\tNO se ha modificado ningún atributo del Usuario."
        else:
            print "\nEl usuario N°", id_usuario, "que desea buscar ESTÁ INACTIVO.\n"
    else:
        print "\nEl Usuario", n_usuario, "que desea modificar, NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")
    
def desactivar_usuario(base):
    cleaning()
    print "\nDesactivar Usuario.\n\n"
    id_usuario = raw_input("\n\t\tIngrese el ID del usuario que desea desactivar: ")
    id_usuario = validate_integer(id_usuario)
    cleaning()
    if id_usuario in base.keys():
        if usuarios[id_usuario][6] == True:
            mostrar_datos (usuarios, id_usuario)
            confirmacion = raw_input ("\n\t\t¿Desea desactivar este usuario? \n\t\t1.Si \n\t\t0.No.")
            confirmacion = validate_integer(confirmacion)
            confirmacion = validate_range(confirmacion, 0, 1)
            if confirmacion == 1:
                usuarios[id_usuario][6] = False
                cleaning()
                saving_changes_to_the_file("usuarios.dat", usuarios)
                print "\n\t\tEl usuario ha sido eliminado del SISTEMA exitosamente."
            else:
                cleaning()
                print "\n\t\tSe ha cancelado la desactivación."
        else:
            cleaning()
            print "\n\t\tEl usuario ya se encuentra desactivado."
    else:
        print "\nEl usuario ", id_usuario, " que desea desactivar NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar")
    
def activar_usuario(base):
    cleaning()
    print "\nActivar Usuario.\n\n"
    id_usuario = raw_input("\n\t\tIngrese el ID del usuario que desea reactivar: ")
    id_usuario = validate_integer(id_usuario)
    cleaning()
    if id_usuario in base.keys():
        if usuarios[id_usuario][6] == False:
            mostrar_datos (usuarios, id_usuario)
            confirmacion = raw_input ("\n\t\t¿Desea reactivar este usuario? \n\t\t1.Si \n\t\t0.No.")
            confirmacion = validate_integer(confirmacion)
            confirmacion = validate_range(confirmacion, 0, 1)
            if confirmacion == 1:
                usuarios[id_usuario][6] = True
                cleaning()
                saving_changes_to_the_file("usuarios.dat", usuarios)
                print "\n\t\tEl usuario ha sido reactivado en el SISTEMA exitosamente."
            else:
                cleaning()
                print "\n\t\tSe ha cancelado la reactivación."
        else:
            cleaning()
            print "\n\t\tEl usuario ya se encuentra activo."
    else:
        print "\nEl usuario ", id_usuario, " que desea reactivar NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar")
    
    
seleccion = menu_principal()
while seleccion != 3:
    if seleccion == 1:
        usuarios = loading_file_into_memory("usuarios.dat")
        seleccion = menu_usuario()
        while seleccion != 6:
            if seleccion == 1:
                registro_usuario(usuarios)
            elif seleccion == 2:
                buscar_usuario(usuarios)
            elif seleccion == 3:
                modificar_usuario(usuarios)
            elif seleccion == 5:
                activar_usuario(usuarios)
            else:
                desactivar_usuario(usuarios)
            seleccion = menu_usuario()    
        saving_changes_to_the_file("usuarios.dat", usuarios)
    else:
        cleaning()
        raw_input("\n\tLa tienda SE ENCUENTRA ACTUALMENTE EN DESARROLLO.\n\n\t\t\tPresione la tecla ENTER para continuar operando.")
    seleccion = menu_principal()
cleaning()
raw_input("\n\tUsted ha salido exitosamente del sistema.\n\n\t\t\tPresione ENTER para continuar")
cleaning()

#{1 : registro_usuario(usuarios), 2 : buscar_usuario(usuarios), 
#3 : modificar_usuario(usuarios), 4 : desactivar_usuario(usuarios), 
#5 : activar_usuario(usuarios)[seleccion]}()
