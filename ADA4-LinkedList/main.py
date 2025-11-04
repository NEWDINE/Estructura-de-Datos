from MyLinkedList import MyLinkedList

def menu():
    print("\n========== MENÚ LINKED LIST ==========")
    print("1. Agregar elemento")
    print("2. Mostrar lista")
    print("3. Buscar por ID")
    print("4. Actualizar valor")
    print("5. Eliminar por ID")
    print("6. Mostrar tamaño de la lista")
    print("0. Salir")
    print("=====================================")

lista = MyLinkedList()

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        valor = input("Ingrese el valor a agregar: ")
        lista.agregar(valor)
        print("Elemento agregado correctamente.")

    elif opcion == "2":
        lista.mostrar()

    elif opcion == "3":
        try:
            id_buscar = int(input("Ingrese el ID a buscar: "))
            nodo = lista.buscar_por_id(id_buscar)
            if nodo:
                print(f"ID: {nodo.id} | Valor: {nodo.valor}")
            else:
                print("No se encontró un nodo con ese ID.")
        except ValueError:
            print("ID inválido.")

    elif opcion == "4":
        try:
            id_act = int(input("Ingrese el ID a actualizar: "))
            nuevo_valor = input("Ingrese el nuevo valor: ")
            if lista.actualizar(id_act, nuevo_valor):
                print("Nodo actualizado correctamente.")
            else:
                print("No se encontró un nodo con ese ID.")
        except ValueError:
            print("ID inválido.")

    elif opcion == "5":
        try:
            id_eliminar = int(input("Ingrese el ID a eliminar: "))
            if lista.eliminar_por_id(id_eliminar):
                print("Nodo eliminado.")
            else:
                print("No se encontró un nodo con ese ID.")
        except ValueError:
            print("ID inválido.")

    elif opcion == "6":
        print(f"Tamaño actual de la lista: {lista.longitud()}")

    elif opcion == "0":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
