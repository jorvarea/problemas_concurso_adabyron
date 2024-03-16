def calcular_multiplicacion(num1: int, num2: int) -> str:
    resultado_decimal = num1 * num2
    resultado_sin_cinco = ""
    while resultado_decimal > 0:
        resultado_sin_cinco += "012346789"[resultado_decimal % 9]
        resultado_decimal //= 9
    return resultado_sin_cinco

def procesar_datos() -> None:
    entrada = input()
    while entrada:
        num1, num2 = (int(num) for num in entrada.split())
        resultado = calcular_multiplicacion(num1, num2)
        print(resultado)
        entrada = input()

def main() -> None:
    procesar_datos()

if __name__ == "__main__":
    main()