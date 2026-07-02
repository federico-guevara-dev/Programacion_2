#Diseñar un programa que genere un número aleatorio entre 2 y 20. El jugador tiene 6 intentos para adivinar el número. En cada intento indicar si el número secreto es mayor o menor al número ingresado, si es igual el jugador gana.

from random import randint

ran=randint(1,20)

attemps=6
try:
  while(attemps>0):
    out=int(input("Enter a number from 1 to 20: "))
    if(out<=0):
      raise
    if(ran>out):
        print("The number is higher")
        attemps-=1
    elif(ran<out):
        print("The number is lower")
        attemps-=1
    if(out==ran):
      print("You win")
      break;
    elif(attemps==0&out!=ran):
      print("You lose")
except:
  print("You cannot enter letters or numbers lower than 0")