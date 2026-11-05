from sedes import sedes

print('Sedes registradas:', len(sedes))
print("Primera sede:", sedes[0]['nombre'])
print('Ventas de la primera sede:',(sedes[0]['ventas']))


print('ANALISIS SEMANAL DE EMPRENDIMIENTOS')

for sede in sedes:
    total=sum(sede['ventas'])
    porcentaje =  total /  sede ['meta'] * 100
    
    
    #clasificacion
    if porcentaje >= 100:
        estado = 'Meta alcanzada'
    elif porcentaje >= 80:
        estado = 'Cerca de la meta'
    else:
        estado = 'Requiere atencion'
        
    print(
        f"{sede['nombre']} Total: {total:,.2f}"
        f"Cumplimiento: {porcentaje:.2f}% : {estado}"
        
    )
    