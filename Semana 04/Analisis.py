
#cuenta = float (input("Ingrese el monto total de la cuenta: "))
#tip = float (input("Ingrese el porcentaje de propina que desee pagar:"))

#propina = (cuenta * tip) / 100


#print(f"la cuenta es de ₡{cuenta}")
#print(f"La propina es de ₡{propina}")


#--------------------------------------------


#numero = int(input("Ingrese un número : "))

#if numero % 2 == 0:
   # print(f"El número {numero} es par")
#else:
   # print(f"El número {numero} es impar")


#--------------------------------------------
   
   
   
#edad = int(input("Ingrese su edad: "))


# if edad < 18:
#     mensaje = "Usted es menor de edad"
#     print (mensaje)
#     
# elif edad >= 18 and edad <= 65:
#     
#     mensaje = "Usted es un adulto"
#     print (mensaje)
#     
# else:
#     print ("Usted es un adulto mayor")

#----------------------------------------------

compra = float (input("Ingrese el monto total de la compra: "))
descuento =  input("Aplica descuento (si/no): ").lower()



if descuento == 'si':
    monto =  float(input("Cual es el porcentaje del descuento: "))
    num = (compra * monto) / 100
    total= compra - num
    print (f"Su total a pagar con descuento es de: ₡{total}")

else:
    print(f"Su compra no aplica descuento, el total de su compra es: ₡{compra}")













