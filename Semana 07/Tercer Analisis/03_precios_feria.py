"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]


# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
promedio = sum(precios) / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo
# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
indice = 0
contador = 0
while indice < len(precios):
    if precios[indice] > promedio:
        contador += 1
    indice += 1
# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
if rango >= 300:
    clasificacion = "variación alta"
elif rango >= 150:
    clasificacion = "variación moderada"
else:
    clasificacion = "variación baja"
# TODO: Muestre producto y todos los resultados.
print("Producto:", producto)
print("Promedio:", promedio)
print("Mínimo:", minimo)
print("Máximo:", maximo)
print("Rango:", rango)
print("Cantidad de precios sobre el promedio:", contador)
print("Clasificación del rango:", clasificacion)

# Con los datos base: promedio ₡980, mínimo ₡850, máximo ₡1200,
# rango ₡350, 2 precios sobre el promedio, variación alta.
# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.
