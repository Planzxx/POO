"""Ejercicio 02 — Un cálculo de existencias

Una biblioteca tiene 12 ejemplares y ha prestado 5. Calcula cuántos quedan y qué porcentaje representan. Guarda ambos resultados y muéstralos con un texto. Usa una cadena f para incluir valores, por ejemplo f"Quedan {restantes}". Supón que el total es positivo.

Comprueba: Quedan 7 ejemplares. El porcentaje es aproximadamente 58,33. Si prestados vale 0, quedan 12 y el porcentaje es 100.

Ampliación: Calcula cuántas cajas de 5 ejemplares se llenan con los 12 y cuántos sobran.
"""



# Escribe tu solución debajo.
stock_biblioteca = 12
stock_prestado= 5

new_stock_biblioteca = stock_biblioteca - stock_prestado 
por_new_stock_biblioteca = (new_stock_biblioteca * 100 ) / stock_biblioteca 
print ('La biblioteca tuvo un stock de: ', stock_biblioteca,'hemos prestado', stock_prestado, 'nuestro stock actual es de:', new_stock_biblioteca, 'representa el: ', por_new_stock_biblioteca)
## Explicación ##
# Predicción: 
# Resultado Observado:
# Explicación: