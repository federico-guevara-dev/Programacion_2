#Una bacteria se reproduce en el lapso de 1 hora. Luego, por cada hora que pasa cada bacteria se reproduce en otra. Preguntar al usuario cuantas horas pasaron e indicar cuantas bacterias habrá.

import random
hour=int(input("Enter the number of hours: "))

if(hour>0):
  bacteria=1*(2**hour);
  print(f'En {hour}hs nacieron {bacteria} bacterias')
else:
  print("Invalid value entered")