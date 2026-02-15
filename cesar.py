ALFABETO = "abcdefghijklmnñopqrstuvwxyz"  # Alfabeto español con ñ
LONGITUD = len(ALFABETO)  # 27


def cifrar(texto, clave):
    clave = clave % LONGITUD  # Normalizar clave
    resultado = ""

    for caracter in texto:
        if caracter.lower() in ALFABETO:
            es_mayuscula = caracter.isupper()
            indice = ALFABETO.index(caracter.lower())
            nuevo_indice = (indice + clave) % LONGITUD
            nueva_letra = ALFABETO[nuevo_indice]

            if es_mayuscula:
                nueva_letra = nueva_letra.upper()

            resultado += nueva_letra
        else:
            resultado += caracter

    return resultado


def descifrar(texto, clave):
    clave = clave % LONGITUD  # Normalizar clave
    return cifrar(texto, -clave)


def obtener_clave():
    while True:
        try:
            clave = int(input("Ingrese la clave (ROT#): "))
            return clave
        except ValueError:
            print("Error: Debe ingresar un número válido.")


def menu():
    while True:
        print("\n=== CIFRADO CÉSAR (Alfabeto Español) ===")
        print("1. Cifrar texto")
        print("2. Descifrar texto")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            texto = input("Ingrese el texto a cifrar: ")
            clave = obtener_clave()
            print("\nTexto cifrado:")
            print(cifrar(texto, clave))

        elif opcion == "2":
            texto = input("Ingrese el texto a descifrar: ")
            clave = obtener_clave()
            print("\nTexto descifrado:")
            print(descifrar(texto, clave))

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
