"""Semana 8: informe de atenciones hospitalarias ficticias.

Complete las fases con el docente. La lectura de datos ya está preparada.
"""

# FASE 0: CONSUMIR LA CONEXIÓN PREPARADA
# conexion_api.py se encuentra junto a este archivo.
from conexion_api import cargar_datos

registros = cargar_datos()
print("Fuente: JSON público de GitHub")
print("Atenciones recibidas:", len(registros))

# La muestra solicitada usa range(3): deben existir las posiciones 0, 1 y 2.
if len(registros) < 3:
    raise SystemExit("Se necesitan al menos 3 registros. Publique la etapa 3.")
for indice in range (3):
    print(indice)

# FASE 1: MOSTRAR Y CONTAR LOS MEDICAMENTOS DE TRES ATENCIONES
conteo_medicamentos = {}
total_medicamentos = 0

print("\nANALISIS FASE #1 MUESTRA 3")
for indice in range (3):
    registro = registros[indice]
    
    print("\n\t\t INFORMACION DEL PACIENTE")
    print("Cedula: ")
    print(registro['codigo'])
    print("Nombre: ")
    print(registro['paciente_nombre']) #cedula, nombre, diagnostico, medicamentos -> type (list)
    print("Diagnóstico: ")
    print(registro['diagnostico'])
    print("Medicamentos: ")
    print(registro['medicamentos'])

    for medicamento in registro['medicamentos']:
        print(medicamento)
        total_medicamentos += 1
    
    
print("\nTotal de medicamentos recetados:", total_medicamentos)
# FASE 2: CONTAR LOS MEDICAMENTOS DE TODAS LAS ATENCIONES


print("\nANALISIS FASE #2 MEDICAMENTOS Y ATENCIONES")

for indice in range (3):
    registro = registros[indice]

    
    

# FASE 3: CONTAR ATENCIONES POR HOSPITAL

# FASE 4: CONTAR ATENCIONES POR ENFERMEDAD DIAGNOSTICADA

