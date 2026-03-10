def esPalindromo(texto):
    """ 
    EJERCICIO: DETERMINAR SI UNA CADENA DE CARACTERES ES UN PALÍNDROMO.
    PARÁMETRO: TEXTO CON UNA CADENA DE CARACTERES
    RESULTADO:
    TRUE = SI es PALÍNDROMO
    FALSE = SI NO es PALÍNDROMO
    """
    texto_invertido = "" #CADENA PARA GUARDAR EL TEXTO INVERTIDO
    # RECORRE EL TEXTO DESDE EL FINAL HASTA EL INICIO
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido = texto_invertido + texto[i]
    # COMPARAR TEXTO ORIGINAL CON EL TEXTO INVERTIDO
    if texto == texto_invertido:
        return True
    else:
        return False
    
    
# REFACTOR REALIZADO
# Se realizó un refactor estructural extrayendo la lógica de inversión del texto a una
# función auxiliar llamada "invertirTexto". En la versión inicial toda la lógica se
# encontraba dentro de la función principal "esPalindromo", lo que hacía que la función
# tuviera múltiples responsabilidades. Con el refactor se separó la responsabilidad de
# invertir la cadena en una función independiente, permitiendo que "esPalindromo" se
# concentre únicamente en la comparación del texto original con el texto invertido.
# Esta mejora incrementa la modularidad del código, facilita su reutilización y mejora
# significativamente la legibilidad sin alterar el comportamiento del programa.