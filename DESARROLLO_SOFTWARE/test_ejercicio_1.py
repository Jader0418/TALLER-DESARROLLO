import unittest
from ejercicio_1 import sumarPositivos

class TestSumarPositivos(unittest.TestCase):

    def test_lista_vacia(self):
        """CASO: PARA LISTA VACÍA"""
        lista = []
        resultado = sumarPositivos(lista)
        print("\n CASO: PARA LISTA VACÍA")
        print(" - ENTRADA:", lista)
        print(" - RESULTADO:", resultado)
        self.assertEqual(resultado, 0)

    def test_solo_negativos(self):
        """CASO: PARA NÚMEROS NEGATIVOS"""
        lista = [-5, -2, -10, -30, -54, -75, -101]
        resultado = sumarPositivos(lista)
        print("\n CASO: PARA NÚMEROS NEGATIVOS")
        print(" - ENTRADA:", lista)
        print(" - RESULTADO:", resultado)
        self.assertEqual(resultado, 0)

    def test_mezcla_positivos_negativos(self):
        """CASO: PARA NÚMEROS POSITIVOS Y NEGATIVOS"""
        lista = [3, -2, 7, -1, 100, 2, -23, -34, 5]
        resultado = sumarPositivos(lista)
        print("\nCASO: MEZCLA POSITIVOS Y NEGATIVOS")
        print(" - ENTRADA:", lista)
        print(" - RESULTADO:", resultado)
        self.assertEqual(resultado, 117)

    def test_un_solo_positivo(self):
        """CASO: PARA UN SOLO POSITIVO"""
        lista = [8]
        resultado = sumarPositivos(lista)
        print("\nCASO: PARA UN SOLO POSITIVO")
        print(" - ENTRADA:", lista)
        print(" - RESULTADO:", resultado)
        self.assertEqual(resultado, 8)

if __name__ == "__main__":
    unittest.main()