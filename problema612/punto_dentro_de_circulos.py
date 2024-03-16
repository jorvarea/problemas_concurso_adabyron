from math import sqrt

def punto_contenido_circulo(r: int, centro_x: int, centro_y: int, x: int, y: int):
    distancia_punto_centro = sqrt((x - centro_x)**2 + (y - centro_y)**2)
    if distancia_punto_centro <= r:
        resultado = True
    else:
        resultado = False
    return resultado

def calcular_circulos_contienen_punto(r: int, centro_x: int, centro_y: int, x: int, y: int) -> int:
    num_circulos = 0
    if punto_contenido_circulo(r, centro_x, centro_y, x, y):
        num_circulos += 1
    if r != 1:
        nuevo_r = r // 2
        num_circulos += (calcular_circulos_contienen_punto(nuevo_r, centro_x + r, centro_y, x, y)
                        + calcular_circulos_contienen_punto(nuevo_r, centro_x - r, centro_y, x, y)
                        + calcular_circulos_contienen_punto(nuevo_r, centro_x, centro_y + r, x, y)
                        + calcular_circulos_contienen_punto(nuevo_r, centro_x, centro_y - r, x, y)
                        )
    return num_circulos

def procesar_datos() -> None:
    entrada = input()
    while entrada:
        r0, x, y = (int(num) for num in entrada.split())
        resultado = calcular_circulos_contienen_punto(r0, 0, 0, x, y)
        print(resultado)
        entrada = input()

def main():
    procesar_datos()

if __name__ == "__main__":
    main()