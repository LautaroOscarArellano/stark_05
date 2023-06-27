import json,re,os,sys

def imprimir_menu_desafio_5():
    print(""" 
    "A":leer_archivos
    "B":guardar_archivo
    "C":capitalizar_palabras
    "D":obtener_nombre_capitalizado
    "E":obtener_nombre_y_dato
    "F":es_genero
    "G":stark_guardar_heroe_genero
    "H":calcular_min_genero
    "I":calcular_max_genero
    "J":calcular_max_min_dato
    "K":stark_calcular_imprimir_guardar_heroe_genero
    "l":sumar_dato_heroe_genero
    "M":cantidad_heroes_genero
    "N":calcular_promedio_genero
    "O":stark_calcular_imprimir_guardar_promedio_altura_genero
    "P":esta_en_lista
    "Q":calcular_cantidad_tipo
    "R":obtener_lista_de_tipos
    "S":normalizar_dato
    """)
    opcion=input("Ingresar letra :")
    opcion=re.findall("[A-Oa-o]",opcion)
    opcion=str(opcion)
    opcion=opcion.replace("['","").replace("']","")#check
    if(opcion != ""):
        return opcion
    else:
        return "-1"

#1.4           
def leer_archivos()->list:
    nombre="data_stark"
    extension=".json"
    print(nombre+extension)
    with open(nombre+extension,"r")as documento:
        cadena = json.load(documento)
        for item in cadena:
            item["altura"]=float(item["altura"])
            item["peso"]=float(item["altura"])
            item["fuerza"]=float(item["fuerza"])
        return cadena
#1.5
def guardar_archivo(nombre_guardado :str, extension_guardado:str , contenido_a_guardar:str):
    if contenido_a_guardar != "":
        valor=nombre_guardado+"."+extension_guardado
        with open(valor,"w")as documento:
            documento.write(contenido_a_guardar)
        print(f"Se creó el archivo: {nombre_guardado}.{extension_guardado}")
        return True
    else:
        print(f"Error al crear elarchivo: {nombre_guardado}.{extension_guardado}")
        return False
#1.6
def capitalizar_palabras(cadena:str):
    return cadena.capitalize()

#1.7
def obtener_nombre_capitalizado(diccionario:dict,key_n:str):
    palabra=diccionario[key_n]
    diccionario[key_n]=palabra.capitalize()
    return diccionario

#1.8
def obtener_nombre_y_dato(diccionario:dict , key_random):
    dato_a=obtener_nombre_capitalizado(diccionario,"nombre")
    diccionario[key_random]
    exportar=(f"Nombre : {dato_a} | {key_random} : {diccionario[key_random]}")
    return exportar

#2da parte
#2.1
def es_genero(diccionario:dict,evaluador_genero:str):
    evaluador_genero=evaluador_genero.capitalize()
    if diccionario["genero"] == "M" or diccionario["genero"] =="F" or diccionario["genero"] == "NB":
        return diccionario
    else:
        return False

#2.2

def stark_guardar_heroe_genero(lista_heroes:str,evaluador_genero:str):
    genero=evaluador_genero.capitalize()
    for item in lista_heroes:
        if item["genero"] == evaluador_genero:
            dato_a=es_genero(item,evaluador_genero)
            dato_b=obtener_nombre_capitalizado(dato_a,"nombre")

    if genero == "F":
        guardar_archivo("heroes_F","csv",str(dato_b))
    if genero == "M":
        guardar_archivo("heroes_M","csv",str(dato_b))
    if genero == "NB":
        guardar_archivo("heroes_NB","csv",str(dato_b))

#Tercera parte
#3.1

def calcular_min_genero(lista_heroes:list , key_dato:str , genero:str)->str:
    for heroe in lista_heroes:
        if(heroe["genero"]==genero.capitalize()):
            comparador=heroe
            break
        elif(heroe["genero"]==genero.capitalize()):
            comparador=heroe
            break
        elif(heroe["genero"]==genero.capitalize()):
            comparador=heroe
            break

    for item in lista_heroes:
        if item["genero"] == comparador["genero"]:
            if(comparador[key_dato] > item[key_dato]): 
                comparador=item
    return comparador

#3.2
def calcular_max_genero(lista_heroes:list , key_dato:str , genero:str)->str:
    for heroe in lista_heroes:
        if(heroe["genero"]==genero.capitalize()):
            comparador=heroe
            break
        elif(heroe["genero"]==genero.capitalize()):
            comparador=heroe
            break
        elif(heroe["genero"]==genero.capitalize()):
            comparador=heroe
            break

    for item in lista_heroes:
        if item["genero"] == comparador["genero"]:
            if(comparador[key_dato] < item[key_dato]): 
                comparador=item
    #print(f"El mayor de tipo {key_dato} :{comparador['nombre']}")
    return comparador

#3.3
def calcular_max_min_dato(lista_heroes:list , estado:str , key:str,genero :str)->str:
    if estado == "minimo":
        dato=calcular_min_genero(lista_heroes,key,genero)
    elif estado =="maximo":
        dato=calcular_max_genero(lista_heroes,key,genero)
    return dato
# aberc=calcular_max_min_dato(prueba , "minimo" , "altura" ,"m")
# print(aberc , " activado ")

#3.4 
def stark_calcular_imprimir_guardar_heroe_genero(lista_heroes:list , estado:str , key :str, genero)->None:
    dato=calcular_max_min_dato(lista_heroes,estado,key,genero)
    nombre=obtener_nombre_y_dato(dato,key)
    print(nombre , estado) 
    print("------------------------------")

    if estado == "minimo" and genero == "F":
        print("(1)")
        exportar="heroes_"+estado+"_"+key+"_"+genero
        guardar_archivo(exportar,"csv",nombre)

    elif estado == "maximo" and genero.upper() == "F":
        print("(2)")
        exportar="heroes_"+estado+"_"+key+"_"+genero
        guardar_archivo(exportar,"csv",nombre)

    elif estado == "minimo" and genero.upper() == "M":
        print("(3)")
        exportar="heroes_"+estado+"_"+key+"_"+genero
        guardar_archivo(exportar,"csv",nombre)

    elif estado == "maximo" and genero.upper() == "M":
        print("(4)")
        exportar="heroes_"+estado+"_"+key+"_"+genero
        guardar_archivo(exportar,"csv",nombre)

    elif estado == "minimo" and genero.upper() == "NB":
        print("(5)")
        exportar="heroes_"+estado+"_"+key+"_"+genero
        guardar_archivo(exportar,"csv",nombre)

    elif estado == "maximo" and genero.upper() == "NB":
        print("(6)")
        exportar="heroes_"+estado+"_"+key+"_"+genero
        guardar_archivo(exportar,"csv",nombre)


#4. Cuarta Parte
#4.1
def sumar_dato_heroe_genero(lista_heroes:list,key:str,genero:str)->str:
    sumatoria=0
    genero=genero.upper()
    for item in lista_heroes:
        if(len(item) > 0) and type(item) == dict:
            if genero =="F" or genero =="M" or genero == "NB":
                if item["genero"] == genero:
                    sumatoria+=item[key]
        else:
            print("diccionario vacio")
    return sumatoria  

#4.2
def cantidad_heroes_genero (lista_heroes:list , genero_busqueda:str):
    contador_genero=0
    for item in lista_heroes:
        if item["genero"]==genero_busqueda.upper():
            contador_genero+=1
    return contador_genero
# asca=cantidad_heroes_genero(prueba,"m")
# print(asca)

#4.3
def calcular_promedio_genero(lista_heroes:list , key_dato:str,genero_busqueda:str)->None:
    sumar=sumar_dato_heroe_genero(lista_heroes,key_dato,genero_busqueda)   
    cantidad=cantidad_heroes_genero(lista_heroes , genero_busqueda)
    promedio=sumar//cantidad
    return promedio
# asa=calcular_promedio_genero(prueba , "altura" ,"m")
# print(asa)
#4.4
def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes:list,key_dato:str , genero_busqueda:str):
    if len(lista_heroes) > 0:
        genero_busqueda=genero_busqueda.upper()

        promedio=calcular_promedio_genero(lista_heroes,key_dato,genero_busqueda)
        dato="Altura promedio genero "+genero_busqueda+":"+str(promedio)
        print(dato)
    else:
        print("Error : lista de heroes vacia")

    if genero_busqueda == "F":
        exportar="heroes_promedio"+key_dato+"_"+genero_busqueda
        guardar_archivo(exportar,"csv",dato)
    elif genero_busqueda == "M":
        exportar="heroes_promedio"+key_dato+"_"+genero_busqueda
        guardar_archivo(exportar,"csv",dato)
#5 quta
def esta_en_lista (lista:list , valor:str)->list:
    esta=False
    for elemento in lista:
        if(elemento == valor):
            esta=True
            break
    return esta

def calcular_cantidad_tipo(lista_heroes:list , key_dato):
    lista=list()
    diccionario=dict()
    if len(lista_heroes) > 0 :
        for item in lista_heroes:
            if not esta_en_lista(lista_heroes,item[key_dato]):
                lista.append(item[key_dato])

        for item in lista:
            i=0
            for itema in lista_heroes:
                if(item==itema[key_dato]):
                    i+=1
            diccionario[item]=i
        return diccionario
    else: 
        diccionario["Error"]="La lista se encuentra vacia"
        return diccionario
#5.2
def guardar_cantidad_heroes_tipo(diccionario:dict ,key_dato:str):
    lista_guardado=list()
    for item in diccionario:
        for itema in diccionario.values():
            dato="Caracteristica : "+key_dato+" "+item+" Cantidad "+str(itema)+"\n"
            lista_guardado.append(dato)
    
    exportar="heroes_cantidad_"+key_dato
    guardar_archivo(exportar,"csv",str(lista_guardado)) 
#guardar_cantidad_heroes_tipo(a,"color_ojos")
#6
def obtener_lista_de_tipos(lista_heroes:list , key_dato:str):
    lista_tipos=list()
    for item in lista_heroes:
        if not esta_en_lista(lista_heroes,item[key_dato]):
            lista_tipos.append(item[key_dato])
    print(lista_tipos)
#6.2
def normalizar_dato(dato_heroe , vacio:str):
    if len(dato_heroe) > 0:
        return dato_heroe
    else:
        dato_heroe="N/A"
#6.3


