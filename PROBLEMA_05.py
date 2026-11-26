# ============================================================================
# Nombre del estudiante: Fabio Hernandez
# Grupo: 213022_775
# Programa: Ingenieria de Sistemas
# Codigo Fuente: autoria propia
# ============================================================================
# PROBLEMA 5: Control de Jornada Laboral Semanal
# ============================================================================


def calcular_total_horas(horas_dias):
    """Calcula la suma total de horas semanales recibiendo una lista de horas."""
    return sum(horas_dias)


def clasificar_jornada(total_horas):
    """Clasifica la jornada laboral en 'Sobretiempo' o 'Horario estandar'."""
    umbral_horas = 40.0
    if total_horas > umbral_horas:
        return "Sobretiempo"
    return "Horario estandar"


def procesar_jornada_equipo(matriz_recursos):
    """Procesa la matriz de recursos, calcula totales y clasifica la jornada."""
    resultados = []
    for fila in matriz_recursos:
        nombre = fila[0]
        horas_dias = fila[1:]  # Extrae Lunes a Viernes
        total_horas = calcular_total_horas(horas_dias)
        clasificacion = clasificar_jornada(total_horas)
        resultados.append({
            "nombre": nombre,
            "horas_dias": horas_dias,
            "total_horas": total_horas,
            "clasificacion": clasificacion,
        })
    return resultados


def mostrar_reporte(resultados):
    """Muestra el reporte estructurado en consola."""
    print("=====================================================================")
    print("      REPORTE DE CONTROL DE JORNADA LABORAL SEMANAL                  ")
    print("=====================================================================\n")

    print(
        f"{'Nombre del Recurso':<20} | {'Lun':<4} {'Mar':<4} {'Mie':<4} "
        f"{'Jue':<4} {'Vie':<4} | {'Total Horas':<12} | {'Clasificacion':<18}"
    )
    print("-" * 82)

    for r in resultados:
        dias_str = " ".join([f"{h:<4.1f}" for h in r["horas_dias"]])
        print(
            f"{r['nombre']:<20} | {dias_str} | "
            f"{r['total_horas']:<12.1f} | {r['clasificacion']:<18}"
        )

    print("-" * 82)
    print(
        "Criterio de evaluacion: > 40.0 hrs -> 'Sobretiempo' | "
        "<= 40.0 hrs -> 'Horario estandar'"
    )
    print("=====================================================================\n")


def main():
    # Matriz inicial con 4 recursos y horas de Lunes a Viernes
    # Formato: [Nombre del recurso, Lunes, Martes, Miercoles, Jueves, Viernes]
    matriz_proyecto = [
        ["Carlos Gomez", 8.5, 9.0, 8.5, 9.0, 8.0],   # Total: 43.0 hrs -> Sobretiempo
        ["Ana Martinez", 8.0, 7.5, 8.0, 8.0, 7.5],   # Total: 39.0 hrs -> Horario estandar
        ["Luis Rodriguez", 9.0, 9.5, 9.0, 8.5, 9.0], # Total: 45.0 hrs -> Sobretiempo
        ["Marta Lopez", 8.0, 8.0, 8.0, 8.0, 8.0],    # Total: 40.0 hrs -> Horario estandar
    ]

    resultados = procesar_jornada_equipo(matriz_proyecto)
    mostrar_reporte(resultados)


if __name__ == "__main__":
    main()