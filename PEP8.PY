def parar():
    """Pausa el programa hasta que el usuario presione Enter."""
    input("Presione <ENTER> para continuar")


def capturar():
    """Solicita una temperatura y la devuelve como número decimal."""
    while True:
        try:
            temperatura = float(
                input("Por favor, digite la temperatura: ")
            )
            return temperatura
        except ValueError as error:
            print(f"Error: {error}. Ingrese un número válido.")


def celsius_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9 / 5) + 32


def celsius_kelvin(celsius):
    """Convierte grados Celsius a Kelvin."""
    return celsius + 273.15


def kelvin_fahrenheit(kelvin):
    """Convierte grados Kelvin a Fahrenheit."""
    return (kelvin - 273.15) * 9 / 5 + 32


def kelvin_celsius(kelvin):
    """Convierte grados Kelvin a Celsius."""
    return kelvin - 273.15


def fahrenheit_kelvin(fahrenheit):
    """Convierte grados Fahrenheit a Kelvin."""
    return (fahrenheit - 32) * 5 / 9 + 273.15


def fahrenheit_celsius(fahrenheit):
    """Convierte grados Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5 / 9


def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\nSeleccione una opción:")
    print("1 --> Capturar temperatura")
    print("2 --> Celsius a Fahrenheit")
    print("3 --> Celsius a Kelvin")
    print("4 --> Kelvin a Fahrenheit")
    print("5 --> Kelvin a Celsius")
    print("6 --> Fahrenheit a Kelvin")
    print("7 --> Fahrenheit a Celsius")
    print("0 --> Salir")


def main():
    """Ejecuta el programa principal."""
    temperatura = 0.0
    continuar = True

    while continuar:
        mostrar_menu()
        opcion = input("Ingrese una opción: ").strip()

        try:
            if opcion == "1":
                temperatura = capturar()

            elif opcion == "2":
                resultado = celsius_fahrenheit(temperatura)
                print(f"{temperatura} °C = {resultado:.2f} °F")
                parar()

            elif opcion == "3":
                resultado = celsius_kelvin(temperatura)
                print(f"{temperatura} °C = {resultado:.2f} K")
                parar()

            elif opcion == "4":
                resultado = kelvin_fahrenheit(temperatura)
                print(f"{temperatura} K = {resultado:.2f} °F")
                parar()

            elif opcion == "5":
                resultado = kelvin_celsius(temperatura)
                print(f"{temperatura} K = {resultado:.2f} °C")
                parar()

            elif opcion == "6":
                resultado = fahrenheit_kelvin(temperatura)
                print(f"{temperatura} °F = {resultado:.2f} K")
                parar()

            elif opcion == "7":
                resultado = fahrenheit_celsius(temperatura)
                print(f"{temperatura} °F = {resultado:.2f} °C")
                parar()

            elif opcion == "0":
                print("Bye delfina")
                continuar = False

            else:
                print("Seleccione una opción válida.")

        except (ValueError, TypeError) as error:
            print(f"Se produjo un error: {error}")


if __name__ == "__main__":
    main()
    