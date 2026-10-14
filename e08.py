"""Ejercicio 08 — Una lista que recorre el catálogo

Crea titulos = ["Dune", "1984"]. Añade "Fundación" con append. Recorre la lista con for y muestra un título por línea con su número, empezando por 1. Usa un contador que aumente en cada vuelta.

Comprueba: Aparecen tres títulos numerados 1, 2 y 3. La lista original sí cambia al llamar a append.

Ampliación: Cuenta cuántos títulos contienen la letra "a", ignorando mayúsculas.
"""



# Escribe tu solución debajo

import pandas as pd
libro = {
    'Titulo' : ['El Árbol de la Ciencia', 'La Casa de Bernarda Alba', 'Berlarminio y Apolonio'],
    'Fecha' : [1911,1936,1921],
}
lb = pd.DataFrame(libro)
print (lb)