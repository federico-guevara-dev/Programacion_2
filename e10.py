#Escribir una función para convertir temperatura de Celsius a Fahrenheit y otra función para la conversión opuesta.

def ctf(c):
  if(int(c)>0):
    c=int(c)
    print(f"The temperature in Fahrenheit is: {c*9/5+32}")
ctf(input("Enter the temperature in Celsius: "))

def ftc(f):
  if(int(f)>0):
    f=int(f)
    print(f"The temperature in Celsius is: {(f-32)*5/9}")
ftc(input("Enter the temperature in Fahrenheit: "))