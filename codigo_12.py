#Desarrollar un programa que se base en un sorteo de estudiantes; y de forma aleatoria generar otra lista que indique el orden en el que deben pasar a exponer.

import random
stud=["Pepe","Carlos","Juan","Tito","Ignacio"]
x=[]
for i in range(len(stud)):
  n=random.randint(0,len(stud)-1)
  x.append(stud[n])
  del(stud[n])
print(f"The winner is: {x}")