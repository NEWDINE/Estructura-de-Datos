import hashlib

# ===========================================================
#  MÉTODO 1: BÚSQUEDA SECUENCIAL
# ===========================================================
def busqueda_secuencial(lista, valor):
    print("\n[ BÚSQUEDA SECUENCIAL ]")
    for i in range(len(lista)):
        print(f"Revisando posición {i}: {lista[i]}")
        if lista[i] == valor:
            return i
    return -1


# ===========================================================
#  MÉTODO 2: BÚSQUEDA BINARIA
# ===========================================================
def busqueda_binaria(lista, valor):
    print("\n[ BÚSQUEDA BINARIA ]")
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        print(f"Medio en posición {medio}: {lista[medio]}")

        if lista[medio] == valor:
            return medio

        if lista[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


# ===========================================================
#  MÉTODO 3: CIFRADO HASH (SHA-256)
# ===========================================================
def cifrar_hash(texto):
    print("\n[ CIFRANDO CON SHA-256 ]")
    hash_sha = hashlib.sha256(texto.encode()).hexdigest()
    return hash_sha


# ===========================================================
#  MENÚ PRINCIPAL
# ===========================================================
def main():
    while True:
        print("\n==============================")
        print("        MENÚ PRINCIPAL")
        print("==============================")
        print("1. Búsqueda Secuencial")
        print("2. Búsqueda Binaria")
        print("3. Cifrado Hash (SHA-256)")
        print("4. Salir")
        print("==============================")

        opcion = input("Selecciona una opción: ")

        # ------------------------------
        # 1. BÚSQUEDA SECUENCIAL
        # ------------------------------
        if opcion == "1":
            datos = input("\nIngresa números separados por coma: ")
            lista = [int(x) for x in datos.split(",")]
            valor = int(input("Número a buscar: "))

            resultado = busqueda_secuencial(lista, valor)

            if resultado != -1:
                print(f"\n✔ Valor encontrado en la posición {resultado}")
            else:
                print("\n✘ Valor NO encontrado")

        # ------------------------------
        # 2. BÚSQUEDA BINARIA
        # ------------------------------
        elif opcion == "2":
            datos = input("\nIngresa números separados por coma (ordenados o no): ")
            lista = sorted([int(x) for x in datos.split(",")])
            print(f"\nLista ordenada para la búsqueda: {lista}")

            valor = int(input("Número a buscar: "))

            resultado = busqueda_binaria(lista, valor)

            if resultado != -1:
                print(f"\n✔ Valor encontrado en la posición {resultado}")
            else:
                print("\n✘ Valor NO encontrado")

        # ------------------------------
        # 3. CIFRADO HASH
        # ------------------------------
        elif opcion == "3":
            texto = input("\nIngresa el texto a cifrar: ")
            print("\nHash generado:")
            print(cifrar_hash(texto))

        # ------------------------------
        # 4. SALIR
        # ------------------------------
        elif opcion == "4":
            print("\nSaliendo del programa...")
            break

        else:
            print("\nOpción inválida, intenta de nuevo.")


# Ejecutar programa
main()
