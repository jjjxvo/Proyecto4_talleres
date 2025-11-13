import csv

#**********************CARGA Y GUARDADO DE DATOS EN CSV**********************

#Función 1
def guardar_csv(talleres):
    with open("Talleres.csv","w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre","cupos","inscritos"])
        for nombre, datos in talleres.items():
            inscritos_str = ";".join(datos["inscritos"])
            escritor.writerow([nombre, datos["cupos"], inscritos_str])
    print("¡Datos guardados exitosamente!")

#Función 2
def cargar_los_datos():
    talleres = {}
    try:
        with open("Talleres.csv", "r") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                talleres[fila["nombre"]] = {
                    "cupos": int(fila["cupos"]),
                    "inscritos": fila["inscritos"].split(";") if fila["inscritos"] else []
                }
    except FileNotFoundError:
        print("No existe el archivo.")
    return talleres

#**********************FUNCIONES DEL SISTEMA**********************

#Función 1
def crear_taller(talleres):
    nombre = input("Ingrese el nombre del taller: ").strip()
    if nombre in talleres:
        print("No se puede agregar un taller ya creado, intente nuevamente.")
        return
    try:
        cupos = int(input("Ingrese la cantidad de cupos disponibles para el taller: "))
        talleres[nombre] = {
            "cupos": cupos,
            "inscritos": [] 
            }
        print("¡Taller creado correctamente!")
    except ValueError:
        print("Ingrese un número válido.")
        return

#Función 2
def inscribir_participante(talleres):
    nombre = input("Taller: ").strip()
    if nombre not in talleres:
        print("No existe ese taller.")
        return
    if len(talleres[nombre]["inscritos"]) >= talleres[nombre]["cupos"]:
        print("No hay cupos disponibles.")
        return
    persona = input("Ingrese el nombre del participante: ").strip()
    if persona in talleres[nombre]["inscritos"]:
        print("La persona ya está inscrita.")
        return
    talleres[nombre]["inscritos"].append(persona)
    print("Participante inscrito correctamente.")

#Función 3
def desinscribir_participante(talleres):
    nombre_taller = input("Ingrese el nombre del taller: ").strip()
    if nombre_taller not in talleres:
        print("Ese taller no existe.")
        return
    participante = input("Ingrese el nombre del participante a eliminar: ").strip()
    if participante not in talleres[nombre_taller]["inscritos"]:
        print("Ese participante no está inscrito en este taller.")
        return
    talleres[nombre_taller]["inscritos"].remove(participante)
    print(f"{participante} fue eliminado del taller: '{nombre_taller}'.")

#Función 4
def actualizar_taller(talleres):
    nombre = input("Ingrese el nombre del taller que desea actualizar: ").strip()
    if nombre not in talleres:
        print("Ese taller no existe.")
        return
    try:
        nuevos_cupos = int(input("Ingrese la nueva cantidad de cupos: "))
        if nuevos_cupos < len(talleres[nombre]["inscritos"]):
            print("No puede poner menos cupos que los ya inscritos.")
            return
        talleres[nombre]["cupos"] = nuevos_cupos
        print("Cupos actualizados correctamente.")
    except ValueError:
        print("Debe ingresar un número válido.")

#Función 5
def listar_taller(talleres):
    if not talleres:
        print("Aún no hay talleres.")
        return
    print("\n Lista de talleres:")
    for nombre, datos in talleres.items():
        inscritos = len(datos["inscritos"])
        print(f"- {nombre}: {inscritos}/{datos['cupos']} inscritos")

#Función 6
def eliminar_taller(talleres):
    nombre = input("Taller a eliminar: ").strip()
    if nombre in talleres:
        del talleres[nombre]
        print("Taller eliminado correctamente.")
    else:
        print("Ese taller no existe.")

#Función 7
def reporte_taller(talleres):
    if not talleres:
        print("No hay talleres registrados para mostrar.")
        return
    print("\n Reporte de talleres:")
    for nombre, datos in talleres.items():
        disponibles = datos["cupos"] - len(datos["inscritos"])
        print(f"- {nombre}: {disponibles} cupos disponibles")
    
#**********************PROGRAMA PRINCIPAL MENÚ**********************

if __name__ == "__main__":
    talleres = cargar_los_datos()

    while True:
        print("\n *******MENÚ*******")
        print("1. Crear taller.")
        print("2. Inscribir participante.")
        print("3. Desinscribir participante.")
        print("4. Actualizar taller.")
        print("5. Listar talleres.")
        print("6. Eliminar taller.")
        print("7. Reporte taller.")
        print("8. Guardar y salir.")

        op = input("Ingrese una opción (1-8): ")

        if op == "1":
            crear_taller(talleres)
        elif op == "2":
            inscribir_participante(talleres)
        elif op == "3":
            desinscribir_participante(talleres)
        elif op == "4":
            actualizar_taller(talleres)
        elif op == "5":
            listar_taller(talleres)
        elif op == "6":
            eliminar_taller(talleres)
        elif op == "7":
            reporte_taller(talleres)
        elif op == "8":
            guardar_csv(talleres)
            print("Saliendo del programa...")
            break
        else:
            print("Ingrese una opción válida.")


