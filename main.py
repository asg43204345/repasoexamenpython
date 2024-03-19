import random
import re

bandas = []

print("***ATAVOZ ES TU VOZ***")
print("**********************")

opcion = 100
while opcion != 6:
    print("1. Registrar Banda")
    print("2. Buscar información de una banda")
    print("3. Agenda del evento")
    print("4. Modificar banda")
    print("5. Quitar o eliminar banda")
    print("6. SALIR")

    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    if opcion == 1:
        banda = {}
        banda["id"] = random.randint(1, 100)
        banda["nombre"] = input("Nombre de la banda: ")
        banda["genero"] = input("Género: ")
        while True:
            clasificacion = input("Clasificación (1. Amateur, 2. Intermedia, 3. Especiales): ")
            if clasificacion in ['1', '2', '3']:
                banda["clasificacion"] = int(clasificacion)
                break
            else:
                print("Clasificación no válida. Debe ser 1, 2 o 3.")
        while True:
            tiempo = input("Tiempo en el escenario (formato HH:MM): ")
            if re.match(r'^\d{1,2}:\d{2}$', tiempo):
                banda["tiempo"] = tiempo
                break
            else:
                print("Formato de tiempo incorrecto. Debe ser HH:MM.")
        while True:
            try:
                banda["costo"]=int(input("Costo: $"))
                break
            except ValueError:
                print("Por favor, introduce un valor numérico para el costo.")

        bandas.append(banda)

    elif opcion == 2:
        bandaBuscada = input("Digita el nombre de la banda que estás buscando: ")
        found = False
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"].lower() == bandaBuscada.lower():
                found = True
                print(f"ID: {bandAuxiliar['id']} --- Nombre: {bandAuxiliar['nombre']} --- Género: {bandAuxiliar['genero']} --- Clasificación: {bandAuxiliar['clasificacion']} --- Tiempo: {bandAuxiliar['tiempo']} --- Costo: ${bandAuxiliar['costo']}")
        if not found:
            print("Banda no encontrada.")

    elif opcion == 3:
        print("Agenda del evento:")
        for banda in bandas:
            print(f"ID: {banda['id']}")
            print(f"Nombre: {banda['nombre']}")
            print(f"Género: {banda['genero']}")
            print(f"Clasificación: {banda['clasificacion']}")
            print(f"Tiempo en el escenario: {banda['tiempo']}")
            print(f"Costo: ${banda['costo']}")
            print("-----------------------")

    elif opcion == 4:
        id_modificar = int(input("Ingrese el ID de la banda que desea modificar: "))
        found = False
        for banda in bandas:
            if banda["id"] == id_modificar:
                found = True
                print(f"Modificar Banda ID: {banda['id']}")
                banda["nombre"] = input("Nuevo nombre de la banda: ")
                banda["genero"] = input("Nuevo género: ")
                while True:
                    clasificacion = input("Nueva clasificación (1. Amateur, 2. Intermedia, 3. Especiales): ")
                    if clasificacion in ['1', '2', '3']:
                        banda["clasificacion"] = int(clasificacion)
                        break
                    else:
                        print("Clasificación no válida. Debe ser 1, 2 o 3.")
                while True:
                    tiempo = input("Nuevo tiempo en el escenario (formato HH:MM): ")
                    if re.match(r'^\d{1,2}:\d{2}$', tiempo):
                        banda["tiempo"] = tiempo
                        break
                    else:
                        print("Formato de tiempo incorrecto. Debe ser HH:MM.")
                while True:
                    try:
                        banda["costo"] = int(input("Nuevo costo: $"))
                        break
                    except ValueError:
                        print("Por favor, introduce un valor numerico para el costo.")
                print("Banda modificada con éxito.")
        if not found:
            print("Banda no encontrada.")

    elif opcion == 5:
        id_eliminar = int(input("Ingrese el ID de la banda que desea eliminar: "))
        found = False
        for i, banda in enumerate(bandas):
            if banda["id"] == id_eliminar:
                found = True
                del bandas[i]
                print("Banda eliminada con éxito.")
        if not found:
            print("Banda no encontrada.")

    elif opcion == 6:
        print("¡Hasta luego!")

    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 6.")
