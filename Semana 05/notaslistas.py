#Una lista es como una caja organizadora
# #            0       1    2    3       <-------- en ese orden se guardan
# milista = ["Elena", 22, 1.64, True] #puede almacenar varios tipos de datos
# print(milista[2]) #asi se imprime un dato en especifico
# print(type(milista))

notas = [85, 60, 98]
sumanotas = sum(notas)
promedio =  sumanotas / 3
if promedio >= 70:
    print ("Felicidades, aprobo!")
    
elif promedio >= 60:
    print("Va a reposicion")
else:
    print ("Reprobado!!")
    
print (f"El promedio de notas es: {promedio:.2f}")