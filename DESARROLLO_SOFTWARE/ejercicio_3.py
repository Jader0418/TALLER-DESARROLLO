def calcularDescuento(precioBase, porcentaje):
    """
    CALCULAR EL PRECIO FINAL DESPUÉS DE APLICAR UN DESCUENTO
    PARÁMETROS:  
    precioBase : float o int
        Precio original del producto.
    porcentaje : float o int
        Porcentaje de descuento a aplicar.
        RESULTADO: 
    float
        Precio final después del descuento.
        EXCEPCIONES:
    ValueError:
        - Si el precio base es negativo
        - Si el porcentaje es menor que 0
        - Si el porcentaje es mayor que 100
    """
    if precioBase < 0:
        raise ValueError("El precio base no puede ser negativo")
    # Validar porcentaje negativo
    if porcentaje < 0:
        raise ValueError("El porcentaje no puede ser negativo")
    # Validar que el porcentaje mayor a 100
    if porcentaje > 100:
        raise ValueError("El porcentaje no puede ser mayor a 100")
    # Caso especial: descuent del 0%
    if porcentaje == 0:
        return precioBase
    # Caso especial: descuento del 100%
    if porcentaje == 100:
        return 0
    # Calcular valor del descuento
    descuento = precioBase * (porcentaje / 100)
    # Calcular precio final
    precio_final = precioBase - descuento
    return precio_final