from nombres import *


def test_leer_frecuencias_nombres(fichero):
    #print(leer_frecuencias_nombres(fichero)[:3])
    return leer_frecuencias_nombres(fichero)

def  test_filtrar_por_genero(frecuencia_nombres, genero):
    print(filtrar_por_genero(frecuencia_nombres,genero)[-3:])

def test_calcular_nombres(frecuencia_nombres,genero=None):
    print(calcular_nombres(frecuencia_nombres,genero))

def test_calcular_top_nombres_de_año(frecuencia_nombres, anyo, limite, genero):
    print(calcular_top_nombres_de_año(frecuencia_nombres, anyo, limite, genero))

def test_calcular_nombres_ambos_generos(frecuencia_nombres):
    print(calcular_nombres_ambos_generos(frecuencia_nombres))

def test_calcular_nombres_compuestos(frecuencia_nombres,genero=None):
    print(calcular_nombres_compuestos(frecuencia_nombres,genero))


if __name__ == "__main__":
    fichero = "LAB-Nombres/data/frecuencias_nombres.csv"
    frecuencia_nombres = test_leer_frecuencias_nombres(fichero)
    #test_filtrar_por_genero(frecuencia_nombres, "Hombre")
    #test_calcular_nombres(frecuencia_nombres,"Mujer")   
    #test_calcular_top_nombres_de_año(frecuencia_nombres, 2006, 5, "Hombre")
    #test_calcular_nombres_ambos_generos(frecuencia_nombres)
    test_calcular_nombres_compuestos(frecuencia_nombres,"Hombre")