def burbuja(lista):
    lista = lista.copy()
    n = len(lista)
    pasos = 0
    print("Procedimiento Burbuja:")
    for i in range(n):
        for j in range(0, n - i - 1):
            pasos += 1
            print(f"Comparando {lista[j]} y {lista[j+1]}")
            if lista[j] > lista[j+1]:
                print(f" -> Se intercambian {lista[j]} y {lista[j+1]}")
                lista[j], lista[j+1] = lista[j+1], lista[j]
            print("Estado actual:", lista)
    print(f"Total de pasos: {pasos}")
    return lista


def seleccion(lista):
    lista = lista.copy()
    n = len(lista)
    pasos = 0
    print("Procedimiento Selección:")
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            pasos += 1
            print(f"Comparando {lista[j]} con mínimo actual {lista[minimo]}")
            if lista[j] < lista[minimo]:
                print(f" -> Nuevo mínimo encontrado: {lista[j]}")
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
        print(f"Intercambio posición {i} con mínimo {minimo}")
        print("Estado actual:", lista)
    print(f"Total de pasos: {pasos}")
    return lista


def insercion(lista):
    lista = lista.copy()
    pasos = 0
    print("Procedimiento Inserción:")
    for i in range(1, len(lista)):
        key = lista[i]
        print(f"Tomando elemento {key}")
        j = i - 1
        while j >= 0 and key < lista[j]:
            pasos += 1
            print(f" {key} < {lista[j]} entonces se mueve {lista[j]} a la derecha")
            lista[j + 1] = lista[j]
            j -= 1
            print("Estado actual:", lista)
        lista[j + 1] = key
        print(f"Insertado {key} en posición {j + 1}")
        print("Estado actual:", lista)
    print(f"Total de pasos: {pasos}")
    return lista


def ordenar_lista(lista, metodo):
    metodo = metodo.lower()
    if metodo == "burbuja":
        return burbuja(lista)
    elif metodo == "seleccion":
        return seleccion(lista)
    elif metodo == "insercion":
        return insercion(lista)
    else:
        raise ValueError("Método no válido. Usa: burbuja, seleccion o insercion.")

if __name__ == "__main__":
    numeros = list(map(int, input("Ingresa una lista de números separados por espacio: ").split()))
    metodo = input("Método de ordenamiento (burbuja, seleccion, insercion): ")
    resultado = ordenar_lista(numeros, metodo)
    print("Lista ordenada:", resultado)
