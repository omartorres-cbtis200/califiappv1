# ==============================================================
#  calificaciones.py - Lógica de CalifiApp
#  Cada función cumple uno o más CRITERIOS DE ACEPTACIÓN
#  de las Historias de Usuario (HU) del Product Backlog.
# ==============================================================

LIMITE_ALUMNOS = 30
MINIMA_APROBATORIA = 6


# --------------------------------------------------------------
# HU-01 Registrar alumnos
#  CA1: Se registra un alumno con nombre válido.
#  CA2: No se registra un nombre vacío.
#  CA3: Máximo 30 alumnos por grupo.
# --------------------------------------------------------------
def registrar_alumno(alumnos, nombre):
    nombre = nombre.strip()
    if nombre == "" or len(alumnos) >= LIMITE_ALUMNOS:
        return False
    alumnos.append(nombre)
    return True


# --------------------------------------------------------------
# HU-02 Capturar calificaciones
#  CA1: Se aceptan calificaciones de 0 a 10 (con decimales).
#  CA2: Se rechazan valores fuera de rango.
#  CA3: Se rechazan textos no numéricos.
# --------------------------------------------------------------
def validar_calificacion(texto):
    try:
        calificacion = float(texto)
    except ValueError:
        return None
    if calificacion < 0 or calificacion > 10:
        return None
    return calificacion


# --------------------------------------------------------------
# HU-03 Calcular promedio y estatus
#  CA1: El promedio se redondea a un decimal.
#  CA2: Promedio >= 6 es APROBADO.
#  CA3: Promedio < 6 es REPROBADO.
# --------------------------------------------------------------
def calcular_promedio(calificaciones):
    return round(sum(calificaciones) / len(calificaciones), 1)


def obtener_estatus(promedio):
    if promedio >= MINIMA_APROBATORIA:
        return "APROBADO"
    return "REPROBADO"


# --------------------------------------------------------------
# HU-04 Mostrar reporte del grupo
#  CA1: Cada fila muestra nombre | promedio | estatus.
#  CA2: Se muestra el promedio grupal.
#  CA3: Sin alumnos, el promedio grupal es 0.0.
# --------------------------------------------------------------
def fila_reporte(nombre, promedio):
    return nombre + " | " + str(promedio) + " | " + obtener_estatus(promedio)


def promedio_grupal(promedios):
    if len(promedios) == 0:
        return 0.0
    return round(sum(promedios) / len(promedios), 1)
