#Escribir una función que calcule el aréa de un círculo. Luego escribir una función que calcule el volumen de un cilindro llamando a la primera función.
import math

def area(rad):
  ar=math.pi*(rad**2)
  print(f"The area is: {ar}")
  x=ar
  return x


y=area(int(input("Enter the radio: ")))
def vol(h):
  vo=y*h
  print(f"The volumen is: {vo}")
vol(int(input("Enter the height: ")))