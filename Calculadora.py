
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def calculadora():
    while True:
        print("\nCalculadora:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '5':
            print("Saliendo de la calculadora.")
            break

        if opcion in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
                if opcion == '1':
                    print(f"Resultado: {suma(num1, num2)}")
                elif opcion == '2':
                    print(f"Resultado: {resta(num1, num2)}")
                elif opcion == '3':
                    print(f"Resultado: {multiplicacion(num1, num2)}")
                elif opcion == '4':
                    print(f"Resultado: {division(num1, num2)}")
            except ValueError:
                print("Error: Entrada no válida. Introduce solo números.")
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    calculadora()
