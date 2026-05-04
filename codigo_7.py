#Diseñar un programa que pida la fecha de nacimiento del usuario, e indique su edad en 2 formatos: cantidad de días totales, años-meses-dias. Mostrar en pantalla la fecha de nacimiento,en formato Epoch/Timestamp.
from datetime import *

today=date.today()
def date(d,m,y):
  formatted_date=datetime.strptime(f'{d}/{m}/{y}','%d/%m/%Y').date()
  difference=(today-formatted_date).days
  if(formatted_date>today):
    print("You cannot enter a date in the future")
  else:
    print(f'Your date of birth is {formatted_date} you have {difference} days, and you have {int(difference//365.25)} years, and {int((difference%365.25)*12)} months')

day=input("Enter the date of birth d/m/y: ")
data=day.split("/")
date(data[0],data[1],data[2])