def calcular_multiplicacion(num1: int, num2: int) -> int:
    resultado_normal = num1 * num2
    resultado_sin_cinco = resultado_normal + (resultado_normal // 5) - (resultado_normal // 10)
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