import os
from os import  system

ruta = "C:\\Users\\lenovo\\Desktop\\Recetas"
ruta_base = os.path.basename(ruta)
ruta_directorio = os.path.dirname(ruta)
op=''
#Función saludar
def saludar_usuario():
    saludo="Bienvenido/a"
    print(saludo)
    return saludo
#validar opción nuevo directorio
def opcion_valida():
    opcion_crear=input("¿Deseas crear un nuevo directorio,s/n?\n").lower()
    opciones=['s','n']
    while opcion_crear not in opciones:
        opcion_crear=input("¡Error!Introduce una de estas 2 opciones s o n:\n")
    return opcion_crear
#crear directorio
def crear_directorio(opcion):
    if opcion=='s':
        directorio=input("Nombre del directorio:\n").lower()
        os.makedirs(f"C:\\Users\\lenovo\\Desktop\\Recetas\\{directorio}")
        system('cls')
        return directorio
    elif opcion=='n':
        directorio=''
        system('cls')
    return directorio
#seleccionamos la categoría de la receta
def categoria_receta(directorio):
    string_directorio=str(directorio.lower())
    categoria_elegida=''
    null=""
    categoria_valida=False
    categorias_receta =os.listdir("C:\\Users\\lenovo\\Desktop\\Recetas")

    if(string_directorio not in categorias_receta):
        categorias_receta.append(string_directorio)

    while not categoria_valida:
        for c in categorias_receta:
            print(c)
        categoria_elegida=input("Elige una categoría:\n")

        if categoria_elegida in categorias_receta:
            categoria_valida=True
        elif categoria_elegida==null:
            print("Debes escribir el nombre de la categoría a la que deseas acceder.")
        else:
            print("No has elegido una categoría correcta.")
    return categoria_elegida
#mostramos donde se encuentran las recetas
def mostrar_directorio():

    print(f"Las recetas se encuentran en la ruta:\n{ruta_directorio}\\{ruta_base}")
    return ruta,ruta_base,ruta_directorio
#elegimos la categoria
def elegir_carpeta(categoria_elegida):
    ruta=f"C:\\Users\\lenovo\\Desktop\\Recetas\\{categoria_elegida}"
    ruta_base=os.path.basename(ruta)
    print(f"Has accedido a:\n{ruta_directorio}\\{ruta_base}")
    cantidad_archivos = os.listdir(f"C:\\Users\\lenovo\\Desktop\\Recetas\\{categoria_elegida}")
    if not cantidad_archivos:
        if not cantidad_archivos:
            print("Al estar la carpeta vacia, lo conveniente es que crees un archivo\n")
            a = crear_archivo(categoria_elegida)
            archivo = a
            return archivo
    print("Esta carpeta contiene los archivos:\n")
    for c in cantidad_archivos:
        print(c)

    return ruta,ruta_base,ruta_directorio,cantidad_archivos

#obtener el archivo con el que queremos trabajar
def obtener_archivo(categoria_elegida):
    ruta = f"C:\\Users\\lenovo\\Desktop\\Recetas\\{categoria_elegida}"
    cantidad_archivos = os.listdir(f"C:\\Users\\lenovo\\Desktop\\Recetas\\{categoria_elegida}")
    os.chdir(ruta)
    archivo=""
    opciones=['s','n']
    pregunta=input("¿Quieres crear un archivo,s/n?\n").lower()
    if pregunta=='s':
       a= crear_archivo(categoria_elegida)
       archivo=a
       ruta = f"C:\\Users\\lenovo\\Desktop\\Recetas\\{categoria_elegida}"
       print("Archivo añadido con exito.")
       cantidad_archivos = os.listdir(ruta)
       for c in cantidad_archivos:
           print(c)
    else:
        print("")
        while pregunta not in opciones:
            pregunta=input("Introduce una opción valida,s/n\n")
    while archivo not in cantidad_archivos:
        archivo = input("¿A que archivo deseas acceder?\n")+".txt"
        if archivo not in cantidad_archivos:
            system('cls')
            print("El nombre introducido no pertenece a ningún archivo.")
    system('cls')
    return archivo
#metodo para leer los archivos
def leer_archivo(archivo,categoria_elegida):
    ruta = f"C:\\Users\\lenovo\\Desktop\\Recetas\\{categoria_elegida}"
    cantidad_archivos = os.listdir(ruta)
    if archivo not in cantidad_archivos:
        print("El arhivo que intentas leer no existe.")
    else:
        archivo=open(archivo,'r')
        print(archivo.read())
        archivo.close()
#metodo para sobreescribir archivos
def sobreescribir_archivo(archivo,categoria_elegida):
    ruta_string = f"C:\\Users\\lenovo\\Desktop\\Recetas\\{categoria_elegida}"
    cantidad_archivos = os.listdir(ruta_string)
    if archivo in cantidad_archivos:
        archivo= open(archivo, "w")
        archivo.write(input("Escribe el nuevo contenido:\n"))
        archivo.close()
    else:
        print("El archivo que intentas sobreescribir no existe, crea uno nuevo.")
#metodo para crear archivos
def crear_archivo(categoria_elegida):
    ruta = f"C:\\Users\\lenovo\\Desktop\\Recetas\\{categoria_elegida}"
    os.chdir(ruta)
    cantidad_archivos = os.listdir(ruta)
    archivo=input("Nombre del archivo:\n")+".txt"
    for c in cantidad_archivos:
        print("")
        if archivo==c:
            archivo=input("El archivo ya existe, prueba otro nombre:\n")+".txt"
    archivo=open(archivo,"w")
    archivo.write(input("Escribe el contenido:\n"))
    archivo.close()
    return archivo
#metodo para borrar un archivo
def borrar_archivo(archivo,categoria_elegida):
    ruta_string=f"C:\\Users\\lenovo\\Desktop\\Recetas\\{categoria_elegida}"
    cantidad_archivos = os.listdir(ruta_string)
    if archivo in cantidad_archivos:
        os.remove(archivo)
        print("Archivo eliminado con exito.")
#metodo que despliega lista de opciones
def menu_opciones():
    lista=print("[0]-Crear archivo\n[1]-Leer receta.\n[2]-Sobreescribir receta."
            "\n[3]-Eliminar receta."  
            "\n[4]-Finazlizar programa.")
    return lista

#metodo para validar opciones
def validar_opcion():
    op =(input("¿Que tarea desea ejecutar?\n"))
    opciones=['0','1','2','3','4']
    while op in opciones:
        return op
    else:
            print("Elije una opción correcta:\n")
            op=input()
            system('cls')
            return op
#metodo para elegir opciones
def ejecutar_acciones(op):

  if op=='0':
      crear_archivo(categoria)
  elif op=='1':
      leer_archivo(a,categoria)
  elif op=='2':
      sobreescribir_archivo(a,categoria)
  elif op=='3':
    borrar_archivo(a,categoria)
  else:
      Fin_programa=True
      system('cls')
      print("Programa finalizado con exito.")
      return Fin_programa


#metodo para iterar en el menú
def programa(op):
    while op!='4':
        menu_opciones()
        op = validar_opcion()
        system('cls')
        ejecutar_acciones(op)




#invocamos las funciones para que el programa funcione
saludar_usuario()
mostrar_directorio()
opcion_sn = opcion_valida()
directorio = crear_directorio(opcion_sn)
c = categoria_receta(directorio)
categoria = c
elegir_carpeta(c)
a = obtener_archivo(categoria)
programa(op)







