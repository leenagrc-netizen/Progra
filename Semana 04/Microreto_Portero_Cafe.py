"""Microreto: el portero del café."""
nombre = input("Como te llamas?").upper() .strip()
energia = int(input("Cuanta energia tienes del 1-100:"))
traecafe = input("traes cafe? si/no") .lower() .strip() == 'si'

mensaje = "Completa las reglas del portero."

if (energia < 30) and not (traecafe):
    mensaje = "A descansar!!!!!"
    print(mensaje)
 
  
elif energia >= 30 or traecafe:
    mensaje = "Acceso permitido"
    print(mensaje)
    
else:

    mensaje = "El guarda está confundifo, revisa las respuestas."
    
    print(mensaje)
    


    