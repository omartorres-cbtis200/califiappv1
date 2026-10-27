# ==============================================================
#  Proyecto Scrum: "CalifiApp" - Control de calificaciones
#  Submódulo 2: Aplica metodologías ágiles para el desarrollo de software
#  CBTIS 200 - 3AM PGR
#
#  Avance: Historias de usuario HU-01 a HU-04 con sus
#  CRITERIOS DE ACEPTACIÓN implementados (ver calificaciones.py)
#  y verificados con pruebas (ver test_calificaciones.py).
# ==============================================================
from calificaciones import (
    LIMITE_ALUMNOS, registrar_alumno, validar_calificacion,
    calcular_promedio, obtener_estatus, fila_reporte, promedio_grupal,
)#ESTAS 3 LINEAS IMPORTAN DESDE EL ARCHIVO CALIFICACIONES LA CONSTANTE Y LAS FUNCIONES

NOMBRE_APP = "CalifiApp"
OBJETIVO = "Registrar y consultar las calificaciones de un grupo desde la consola"
NUM_PARCIALES = 3
#Los dos guardan datos, pero de forma distinta: la lista guarda cosas en orden y el diccionario guarda parejas nombre → dato.
alumnos = []          # ["Ana López", "Luis Pérez", ...]
calificaciones = {}   # {"Ana López": [8.0, 9.0, 7.5], ...}


# ---------------- HU-01 Registrar alumnos ----------------
def opcion_registrar():
    print("\n[HU-01] Registrar alumnos  (ENTER vacío para terminar)")
    while True:
        if len(alumnos) >= LIMITE_ALUMNOS:
            print("Se alcanzó el límite de", LIMITE_ALUMNOS, "alumnos.")
            break
        nombre = input("Nombre del alumno: ")
        if nombre.strip() == "":
            break
        if registrar_alumno(alumnos, nombre):
            print("  ✔ ❤️ Registrado:❤️", nombre.strip(), "(" + str(len(alumnos)) + "/" + str(LIMITE_ALUMNOS) + ")")
        else:
            print("  ✘ No se pudo registrar.")
           



# ---------------- HU-02 Capturar calificaciones ----------------
def pedir_calificacion(mensaje):
    while True:
        calificacion = validar_calificacion(input(mensaje))
        if calificacion is not None:
            return calificacion
        print("  ✘ Calificación inválida. Escribe un número de 0 a 10.")


def opcion_capturar():
    print("\n[HU-02] Capturar calificaciones")
    if len(alumnos) == 0:
        print("Primero registra alumnos (opción 1).")
        return
    for nombre in alumnos:
        print("\nAlumno:", nombre)
        parciales = []
        for i in range(1, NUM_PARCIALES + 1):
            parciales.append(pedir_calificacion("  Parcial " + str(i) + ": "))
        calificaciones[nombre] = parciales


# ---------------- HU-03 Calcular promedio y estatus ----------------
def opcion_promedios():
    print("\n[HU-03] Promedio y estatus")
    if len(calificaciones) == 0:#ESTA INSTRUCCIÓN DETECTA SI CALIFICACIONES IGUAL A CERO IMPRIME QUE NO HAY
        print("No hay calificaciones capturadas (opción 2).")
        return
    for nombre in alumnos:#REALIZA EL RECORRIDO EN EL ARREGLO
        if nombre in calificaciones:
            promedio = calcular_promedio(calificaciones[nombre])
            print(" ", nombre, "->", promedio, obtener_estatus(promedio))
        else:
            print(" ", nombre, "-> sin calificaciones")


# ---------------- HU-04 Mostrar reporte del grupo ----------------
def opcion_reporte():
    print("\n[HU-04] Reporte del grupo")
    print("-" * 50)
    print("NOMBRE | PROMEDIO | ESTATUS")
    print("-" * 50)
    promedios = []
    for nombre in alumnos:
        if nombre in calificaciones:
            promedio = calcular_promedio(calificaciones[nombre])
            promedios.append(promedio)
            print(fila_reporte(nombre, promedio))
    print("-" * 50)
    print("Promedio grupal:", promedio_grupal(promedios))


# ---------------- Menú principal ----------------
opcion = ""

while opcion != "0":
    print()
    print("=" * 50)
    print("  " + NOMBRE_APP + " - " + OBJETIVO)
    print("=" * 50)
    print("  1. Registrar alumnos             (HU-01)")
    print("  2. Capturar calificaciones       (HU-02)")
    print("  3. Calcular promedio y estatus   (HU-03)")
    print("  4. Mostrar reporte del grupo     (HU-04)")
    print("  0. Salir")
    print("-" * 50)

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        opcion_registrar()
    elif opcion == "2":
        opcion_capturar()
    elif opcion == "3":
        opcion_promedios()
    elif opcion == "4":
        opcion_reporte()
    elif opcion == "0":
        print("\nGracias por usar " + NOMBRE_APP + ". ¡Hasta pronto!")
    else:
        print("\nOpción no válida. Escribe un número del 0 al 4.")

    if opcion != "0":
        input("\nPresiona ENTER para volver al menú...")
