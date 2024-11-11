import csv
from collections import namedtuple

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'anyo,nombre,frecuencia,genero')

def leer_frecuencias_nombres(fichero):
    frecuencia_nombres = []

    with open(fichero,"r", encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for anyo,nombre,frecuencia,genero in lector:
            anyo = int(anyo)
            frecuencia = int(frecuencia)
            nombre = FrecuenciaNombre(anyo, nombre, frecuencia, genero)
            frecuencia_nombres.append(nombre)
    
    return frecuencia_nombres


def filtrar_por_genero(frecuencia_nombres, genero:str):
    filtrado = []
    for nombre in frecuencia_nombres:
        if nombre.genero == genero:
            filtrado.append(nombre)
    
    return filtrado

def calcular_nombres(frecuencia_nombres,genero=None):
    filtrado = set()
    for nombre in frecuencia_nombres:
        if genero == None:
            filtrado.add(nombre.nombre)
        elif nombre.genero == genero:
            filtrado.add(nombre.nombre)

    return sorted(filtrado)

def calcular_top_nombres_de_año(frecuencia_nombres, anyo:int, limite=10, genero=None):
    res = []
    
    for nombre in frecuencia_nombres:
        # (nombre.genero == None or nombre.genero == genero) and nombre.anyo == anyo
        if nombre.anyo == anyo:
            if genero == None:
                res.append((nombre.nombre,nombre.frecuencia))
            elif nombre.genero == genero:
                res.append((nombre.nombre,nombre.frecuencia))
    


    return sorted(res, key = lambda tupla:tupla[1], reverse=True)[:limite]
        
def calcular_nombres_ambos_generos(frecuencia_nombres):
    res = set()
    hombres = calcular_nombres(frecuencia_nombres, "Hombre")
    mujeres = calcular_nombres(frecuencia_nombres, "Mujer")
    

    '''
    for nombre in hombres:
        if nombre in mujeres:
            res.add(nombre)
    '''

    res = set(hombres).intersection(set(mujeres))

    return res

def calcular_nombres_compuestos(frecuencia_nombres,genero=None):
    res = set()
    
    for nombre in frecuencia_nombres:
        if genero == None:
            if " " in nombre.nombre:
                res.add(nombre)
        elif nombre.genero == genero:
            if " " in nombre.nombre:
                res.add(nombre)
    
    return res

def calcular_frecuencia_media_nombre_años():
    pass

def calcular_nombre_mas_frecuente_año_genero():
    pass

def calcular_año_mas_frecuencia_nombre(frecuencia_nombres, nombre):
    frecuencia = 0
    anyo = 0000
    '''
    for n in frecuencia_nombres:
        if n.nombre == nombre:
            res.append( (n.anyo, n.frecuencia) )

    # return sorted(res, key= lambda x:x[1], reverse=True)[0][0]
    return max((res, key= lambda x:x[1])[0]
    '''
    
    for frecuencia_nombre in frecuencia_nombres:
        if frecuencia_nombre.nombre == nombre and frecuencia_nombre.frecuencia > frecuencia:
            frecuencia = frecuencia_nombre.frecuencia
            anyo = frecuencia_nombre.anyo
    
    return anyo

def calcular_nombres_mas_frecuentes(frecuencia_nombres, genero, decada, num=5):
    dict_nombres_por_frecuencia = dict()
    ## lista = calcular_nombres(frecuencia_nombres, genero)
    for n in frecuencia_nombres:
        if n.genero== genero and decada <= n.anyo <= decada+9 :
            if n.nombre in dict_nombres_por_frecuencia:
                dict_nombres_por_frecuencia[n.nombre] += n.frecuencia
            
            else:
                dict_nombres_por_frecuencia[n.nombre] = n.frecuencia
    '''
    dict_nombres = sorted(dict_nombres_por_frecuencia.items(), key= lambda x:x[1], reverse=True)[:num]
    res=[]    
    for n in dict_nombres:
        res.append(n[0])

    return res
    '''

    ordenados = sorted(dict_nombres_por_frecuencia, key= dict_nombres_por_frecuencia.get, reverse=True)
    return ordenados[:num]
