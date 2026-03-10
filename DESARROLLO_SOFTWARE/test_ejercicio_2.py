import unittest
from ejercicio_2 import esPalindromo

class TestPalindromo(unittest.TestCase):

    def test_palabra_palindroma(self):
        """CASO: PALABRA QUE SÍ ES PALÍNDROMO"""
        texto = "RADAR"
        resultado = esPalindromo(texto)

        print("\nCASO: PALABRA QUE SÍ ES PALÍNDROMO")
        print("- ENTRADA:", texto)
        print("- RESULTADO:", resultado)
        self.assertTrue(resultado)

    def test_palabra_no_palindroma(self):
        """CASO: PALABRA QUE NO ES PALÍNDROMO"""
        texto = "JADER"
        resultado = esPalindromo(texto)

        print("\n CASO: PALABRA QUE NO ES PALÍNDROMO")
        print("- ENTRADA:", texto)
        print("- RESULTADO:", resultado)
        self.assertFalse(resultado)

    def test_cadena_vacia(self):
        """CASO: CADENA VACÍA"""
        texto = ""
        resultado = esPalindromo(texto)

        print("\nCASO: CADENA VACÍA")
        print("- ENTRADA:", texto)
        print("- RESULTADO:", resultado)
        self.assertTrue(resultado)

    def test_un_caracter(self):
        """CASO: UN SOLO CARÁCTER"""
        texto = "H"
        resultado = esPalindromo(texto)

        print("\nCASO: UN SOLO CARÁCTER")
        print("- ENTRADA:", texto)
        print("- RESULTADO:", resultado)
        self.assertTrue(resultado)

    def test_ignorando_espacios(self): 
        """CASO: IGNORANDO ESPACIOS"""
        texto = "SOMOS O NO SOMOS"
        resultado = esPalindromo(texto.replace(" ", ""))

        print("\nCASO: IGNORANDO ESPACIOS")
        print("- ENTRADA:", texto)
        print("- RESULTADO:", resultado)
        self.assertTrue(resultado)  

if __name__ == "__main__":
    unittest.main()