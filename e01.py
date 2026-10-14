"""Ejercicio 01 — La ficha de un libro

Crea titulo = "Dune", paginas = 412 y disponible = True. Muestra cada valor y su tipo con print y type. Cambia solo el título a "1984" y vuelve a mostrarlo. Antes de ejecutar, predice qué línea cambiará.

Comprueba: Los tipos son str, int y bool. El cambio del título no modifica las páginas ni la disponibilidad.

Ampliación: Añade autor = "Frank Herbert" y comprueba su tipo.
"""



# Escribe tu solución debajo.
titulo = 1984
disponible = True
autor = 'Frank Herbert'

print ((titulo), type(titulo))
print ((disponible), type(disponible))
print ((autor), type(autor))
## Explicación ##
# Predicción: Si cambiamos el titulo, cambiará el tipo a INT (entero)
# Resultado Observado: Efectivamente, cambia el tipo
# La diferencia reside en el uso de las comillas, eso hace que Python interpréte que es del tipo STRING.