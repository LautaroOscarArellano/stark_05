from funciones import *
flag_salida=True
while (flag_salida==True):
    os.system("cls")
    match(imprimir_menu_desafio_5().upper()):
        case "A":
            lista=leer_archivos()
        case "B":
            nombre_guardado=input("Ingresar nombre guardado :> ")
            extension_guardado=input("Ingresar la extencion de guardado (json.csv.py) :> ")
            contenido_a_guardar=input("Ingresar la extencion de guardado (json.csv.py) :> ")
            guardar_archivo(nombre_guardado , extension_guardado , contenido_a_guardar)
        case "C":
            cadena=input("Capitalizar string")
            capitalizar_palabras(cadena)
        case "D":
            diccionario=obtener_nombre_capitalizado(lista[0],"nombre")
            print(diccionario)
        case "E":
            exportar=obtener_nombre_y_dato(lista[0], "altura")
        case "F":
            dic_1=es_genero(lista[0],"F")
        case "G":
            stark_guardar_heroe_genero(lista, "F")
        case "H":
           comparador = calcular_min_genero(lista , "altura" , "m")
        case "I":
            comparador_1=calcular_max_genero(lista , "altura" , "m")
        case "j":
            dato=calcular_max_min_dato(lista , "minimo" , "altura","f")
        case "k":
            stark_calcular_imprimir_guardar_heroe_genero(lista , "minimo" , "altura" , "f")
        case "l":
           sumatoria=sumar_dato_heroe_genero(lista,"altura","altura")
        case "M":
           contador_genero=cantidad_heroes_genero (lista , "f")
        case "N":
            promedio=calcular_promedio_genero(lista , "altura","f")
        case "O":
            stark_calcular_imprimir_guardar_promedio_altura_genero(lista,"altura" , "f")
        case "P":
            diccionario_2=calcular_cantidad_tipo(lista , "altura")
        case "Q":
            guardar_cantidad_heroes_tipo(lista[0] ,"altura")
            






        case "SALIR":
            opcion=input("Esta seguro? s/n :>").lower()
            if(opcion=="s"):
                print("Que tenga un lindo viaje♪♪♪")
                break
        case _:
            print("Opcion innesistente ")
    os.system("pause")    