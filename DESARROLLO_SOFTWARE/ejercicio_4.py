#EJERCICIO 4. 
# Explica, en un breve texto, cómo estos tests te ayudan a diseñar mejor la función
# antes de implementarla, relacionándolo con la filosofía de TDD.
"""
Al trabajar con este ejercicio se puede notar que: antes de escribir 
la función, primero pensamos en cómo debería comportarse. Los tests ayudan justamente 
a eso. En lugar de empezar programando directamente, uno se detiene a pensar en 
diferentes situaciones que la función debe manejar. Todas esas decisiones 
sobre el comportamiento del sistema se toman antes de escribir una sola línea de implementación.

Esto está muy relacionado con la idea de Test Driven Development (TDD). En TDD, los tests 
no solo sirven para comprobar que el código funciona, sino que también ayudan a diseñar 
mejor la función. Al definir primero los casos de prueba, estamos describiendo claramente 
qué se espera del programa. Es como escribir una pequeña guía de comportamiento, qué 
entradas son válidas, qué resultados deberían obtenerse y qué errores deben detectarse. 

En los ejercicios que se desarrollaron, los tests actuaron como una especie de mapa. Cada 
prueba representaba un escenario diferente: descuentos normales, casos extremos como 0% o 100%, 
y también situaciones inválidas que debían generar un error. La implementación 
de la función terminó siendo más clara, porque simplemente tenía que cumplir con lo que ya se 
había definido en los tests.
"""