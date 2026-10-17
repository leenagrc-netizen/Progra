nombre = input("Nombre: ").upper().strip()
kit = input("Tipo de kit: ").lower() .strip()
autorizacion = input("Tiene autorización (si/no)? ").lower() .strip() == 'si'
try:
    cantidad = int(input("Cantidad de Kits?: "))
except ValueError:
    print ("Cantidad de kits invalida, digite del 1 al 100")
    cantidad = -1


try:
  dias = int(input("Días de préstamo: "))
  
except ValueError:
    print ("Cantidad de dias invalida, digite del 1 al 100")
    dias = -1
    
if not nombre or not kit or cantidad < 1 or dias < 1:
    resultado = "Registro rechazado, revise los datos"
    
elif autorizacion and cantidad <= 3 and not dias > 7:
    print (f"Solicitud aprobada para {nombre}: {cantidad} kits de {kit}")
    
else:
    resultado = "Solicitud enviada a revision"
    
    
    
print ("-" * 50)
print (resultado)