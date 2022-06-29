1# Autores: Alejandro cabrera
#           Rodrigo Pérez  DNI: 35054269
#           Milena Coyante Arias DNI: 43411822 
#Fecha: 16/06/22
#version:0.0.2
#Description: Proyectyo Integrador 


import funciones as fun
if __name__ == "__main__":
    print("Calculadora ISPC")
    print("Buen dia: ")
    print("Por favor ingrese 5 numeros: ")
    lista = fun.list()
    print("\nLos Números ingresados son: ", lista)
    print()
    max = fun.funcion_max (lista)
    print()
    min = fun.funcion_min (lista) 
    print()
    prom = fun.funcion_promedio(lista)
    print() 
    fun.funcion_suma(lista)
    print()