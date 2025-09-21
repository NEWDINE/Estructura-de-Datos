#Leonardo Gabriel Osorio Castillo
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
departamentos = ["Ropa", "Deportes", "Juguetería"]

ventas = [[0 for _ in departamentos] for _ in meses]

def insertar_venta():
    mes = int(input("Ingresa el número de mes (1-12): ")) - 1
    depto = int(input("Ingresa el departamento (1=Ropa, 2=Deportes, 3=Juguetería): ")) - 1
    valor = int(input("Ingresa el valor de la venta: "))
    ventas[mes][depto] = valor
    print("Venta registrada.\n")

def buscar_venta():
    mes = int(input("Ingresa el número de mes (1-12): ")) - 1
    depto = int(input("Ingresa el departamento (1=Ropa, 2=Deportes, 3=Juguetería): ")) - 1
    print("Venta encontrada:", ventas[mes][depto], "\n")

def eliminar_venta():
    mes = int(input("Ingresa el número de mes (1-12): ")) - 1
    depto = int(input("Ingresa el departamento (1=Ropa, 2=Deportes, 3=Juguetería): ")) - 1
    ventas[mes][depto] = 0
    print("Venta eliminada.\n")

def mostrar_tabla():
    print(f"\n{' ':<12}", end="")
    for dep in departamentos:
        print(f"{dep:<12}", end="")
    print()
    for i in range(len(meses)):
        print(f"{meses[i]:<12}", end="")
        for j in range(len(departamentos)):
            print(f"{ventas[i][j]:<12}", end="")
        print()
    print()

while True:
    print("\n--- Menú de Ventas ---")
    print("1. Insertar venta")
    print("2. Buscar venta")
    print("3. Eliminar venta")
    print("4. Mostrar tabla completa")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        insertar_venta()
    elif opcion == "2":
        buscar_venta()
    elif opcion == "3":
        eliminar_venta()
    elif opcion == "4":
        mostrar_tabla()
    elif opcion == "5":
        break
    else:
        print("Opción no válida.\n")
