def calcular_suma_descendente(num: int) -> int:
    suma = num
    k = 10
    sumando = num % k
    while sumando != num:
        suma += sumando
        k *= 10
        sumando = num % k
    return suma

def procesar_datos():
    num = int(input())
    while num != 0:
        resultado = calcular_suma_descendente(num)
        print(resultado)
        num = int(input())

def main() -> None:
    procesar_datos()

if __name__ == "__main__":
    main()