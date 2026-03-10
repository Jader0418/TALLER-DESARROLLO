import unittest
from ejercicio_3 import calcularDescuento


class TestCalcularDescuento(unittest.TestCase):

    def test_descuento_cero_por_ciento(self):
        """CASO: DESCUENTO CON EL 0%"""

        precioBase = 100000
        porcentaje = 0

        resultado = calcularDescuento(precioBase, porcentaje)

        print("\n TEST: DESCUENTO DEL 0%")
        print("- ENTRADA PRECIO BASE:", precioBase)
        print("- ENTRADA PORCENTAJE:", porcentaje)
        print("- RESULTADO OBTENIDO:", resultado)
        print("- RESULTADO ESPERADO: 100000")

        self.assertEqual(resultado, 100000)


    def test_descuento_cien_por_ciento(self):
        """CASO: DESCUENTO DEL 100%"""

        precioBase = 100000
        porcentaje = 100

        resultado = calcularDescuento(precioBase, porcentaje)

        print("\n TEST: DESCUENTO DEL 100%")
        print("- ENTRADA PRECIO BASE:", precioBase)
        print("- ENTRADA PORCENTAJE:", porcentaje)
        print("- RESULTADO OBTENIDO:", resultado)
        print("- RESULTADO ESPERADO: 0")

        self.assertEqual(resultado, 0)


    def test_descuento_normal(self):
        """CASO: DESCUENTO NORMAL"""

        precioBase = 200
        porcentaje = 25

        resultado = calcularDescuento(precioBase, porcentaje)

        print("\n TEST: DESCUENTO NORMAL")
        print("- ENTRADA PRECIO BASE:", precioBase)
        print("- ENTRADA PORCENTAJE:", porcentaje)
        print("- RESULTADO OBTENIDO:", resultado)
        print("- RESULTADO ESPERADO: 150")

        self.assertEqual(resultado, 150)


    def test_porcentaje_negativo(self):
        """CASO: PORCENTAJE NEGATIVO"""

        precioBase = 100
        porcentaje = -10

        print("\n TEST: PORCENTAJE NEGATIVO")
        print("- ENTRADA PRECIO BASE:", precioBase)
        print("- ENTRADA PORCENTAJE:", porcentaje)
        print("- RESULTADO ESPERADO: ValueError")

        with self.assertRaises(ValueError) as contexto:
            calcularDescuento(precioBase, porcentaje)

        print("ERROR:", contexto.exception)


    def test_porcentaje_mayor_que_cien(self):
        """CASO: PORCENTAJE MAYOR QUE 100"""

        precioBase = 100
        porcentaje = 120

        print("\n TEST: PORCENTAJE MAYOR QUE 100")
        print("- ENTRADA PRECIO BASE:", precioBase)
        print("- ENTRADA PORCENTAJE:", porcentaje)
        print("- RESULTADO ESPERADO: ValueError")

        with self.assertRaises(ValueError) as contexto:
            calcularDescuento(precioBase, porcentaje)

        print("ERROR:", contexto.exception)


    def test_precio_base_negativo(self):
        """CASO: PRECIO BASE NEGATIVO"""

        precioBase = -50
        porcentaje = 10

        print("\n TEST: PRECIO BASE NEGATIVO")
        print("- ENTRADA PRECIO BASE:", precioBase)
        print("- ENTRADA PORCENTAJE:", porcentaje)
        print("- RESULTADO ESPERADO: ValueError")

        with self.assertRaises(ValueError) as contexto:
            calcularDescuento(precioBase, porcentaje)

        print("ERROR:", contexto.exception)


if __name__ == "__main__":
    unittest.main()