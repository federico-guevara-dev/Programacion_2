#Escribir una función donde el usuario ingresa un número entero positivo (validarlo) y calcular el factorial.

def fac(num):
  if(not num.isalpha() and int(num)>0 ):
    num=int(num)
    mult=1
    for i in range(1,num+1):
     mult=mult*i
    print(f"The factorial is: {mult}")
  else:
    print("Invalid value entered")
fac(input("Enter a number: "))