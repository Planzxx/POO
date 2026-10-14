"""Ejercicio 03 — Datos que escribe una persona

Pide un título y un número de páginas con input. Convierte las páginas con int y muestra cuántas tendría el libro si se añadieran 10. En esta primera versión la entrada numérica será un entero válido. Anota qué ocurre al introducir "muchas" y conserva esa duda para el ejercicio 17.

Comprueba: Con Dune y 412, la nueva cantidad es 422. input devuelve texto incluso cuando escribes dígitos. "muchas" produce ValueError en esta versión.

Ampliación: Muestra cuánto ocuparían dos ejemplares si sumamos sus páginas.
"""



# Escribe tu solución debajo.
titulo = str(input('Dime el titulo de un libro:'))
paginas = int(input('Dime el número de páginas:'))

new_paginas= paginas + 10
print(new_paginas)