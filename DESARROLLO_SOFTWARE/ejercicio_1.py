def sumarPositivos(lista):
    """
    EJERCICIO: REALIZA LA SUMA DE NÚMEROS MAYORES QUE 0. 
    PARÁMETRO: [LISTA DE ENTEROS]
    RESULTADO:
    SUMA DE LOS NÚMEROS POSITIVOS DE LA LISTA
    """

    suma = 0  #ACUMULADOR DE LA SUMA

    for numero in lista:
        #VERIFICAR SI ES POSITIVO 
        if numero > 0:
            suma = suma + numero #HACER LA SUMA
    return suma #DEVUELVE EL RESULTADO


# REFACTOR REALIZADO
# Se realizó un refactor en la función para mejorar la legibilidad y claridad del código.
# Inicialmente la lógica de suma se encontraba directamente en la variable acumuladora
# sin expresar claramente el propósito de la operación. En la versión refactorizada se
# reorganizó la estructura del código separando claramente el proceso de iteración y la
# validación de números positivos mediante una condición explícita dentro del ciclo.
# Además, se mejoró el nombre de la variable acumuladora para que describa con mayor
# precisión su función dentro del algoritmo. Este refactor no modifica el comportamiento
# del programa, pero hace que el código sea más comprensible, mantenible y fácil de leer.