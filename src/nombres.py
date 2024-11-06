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

    return filtrado

def calcular_top_nombres_de_año(frecuencia_nombres, anyo:int, limite=10, genero=None):
    res = []
    
    for nombre in frecuencia_nombres:
        
        if len(res) >= limite:
            break

        if nombre.anyo == anyo:
            if genero == None:
                res.append((nombre.nombre,nombre.frecuencia))
            elif nombre.genero == genero:
                res.append((nombre.nombre,nombre.frecuencia))
    
    return sorted(res, lambda tupla:tupla[1])
        
def calcular_nombres_ambos_generos(frecuencia_nombres):
    res = set()
    hombres = calcular_nombres(frecuencia_nombres, "Hombre")
    mujeres = calcular_nombres(frecuencia_nombres, "Mujer")
    for nombre in hombres:
        if nombre in mujeres:
            res.add(nombre)
    
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