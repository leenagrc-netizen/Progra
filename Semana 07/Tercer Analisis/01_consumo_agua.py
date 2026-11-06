"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

# TODO: Calcule el consumo total y el promedio diario.

total_consumo = sum(consumos_litros)
promedio_diario = total_consumo / len(consumos_litros)
print("Total de consumo:", total_consumo)
print("Promedio diario:", promedio_diario)
# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
primer_dia = consumos_litros[0]
ultimo_dia = consumos_litros[-1]
ahorro_litros = primer_dia - ultimo_dia
reduccion_porcentaje = (ahorro_litros / primer_dia) * 100
print("Litros ahorrados:", ahorro_litros)
print("Reducción porcentual:", reduccion_porcentaje)


#       de reducción respecto al primer día.
# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
if reduccion_porcentaje >= 15:
    clasificacion = "Reducción alta"
elif reduccion_porcentaje > 0:
    clasificacion = "Reducción moderada"
else:
    clasificacion = "Sin reducción"
#       de lo contrario, sin reducción.
# TODO: Muestre los cinco resultados.
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
console_output = f"Clasificación: {clasificacion}"
print(console_output)

#          reducción alta.
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
