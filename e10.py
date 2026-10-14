"""Ejercicio 10 — Una función que calcula

Define dias_restantes(plazo, transcurridos). Debe devolver la resta, sin imprimirla ni cambiar los argumentos. Llama a la función y muestra el resultado desde fuera. Prueba (14, 4), (14, 14) y (14, 17).

Comprueba: Los resultados son 10, 0 y -3. return entrega un valor que se puede guardar. print solo lo muestra.

Ampliación: Define estado_plazo(plazo, transcurridos), reutilizando dias_restantes, que devuelva En plazo, Vence hoy o Con retraso.
"""



# Escribe tu solución debajo.
def dias_restantes(dias_plazo:int, dias_transcurrido: int) -> int:
    return dias_plazo - dias_transcurrido


def estado_plazo (dias_plazo: int, dias_transcurrido: int) -> str:
    resultado_final = dias_restantes(dias_plazo,dias_transcurrido)
    if resultado_final > 0:
        return (f'Quedan {resultado_final} días de plazo')
    elif resultado_final == 0:
        return ('El plazo finaliza hoy')
    else:
        return ("El resultado es no es valido")
if __name__ == '__main__':
    plazo = int(input('Dime el total de número de plazo: '))
    transcurridos = int(input('Dime los días transcurridos: '))
    if 
    mensaje = estado_plazo(plazo,transcurridos)
    print(mensaje)
