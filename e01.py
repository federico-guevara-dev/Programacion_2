#Utilizar la función input() y print() para preguntar el nombre de usuario. Saludar y luego preguntar el año de nacimiento y el actual; calcular la edad del usuario. En mi caso hize algo parecido.

from datetime import *
it_date=date.today()#.strftime('%d/%m/%Y')

try:
  name=input("Enter your name: ")
  print(f'Hi {name}')
  age_year=input("Enter your date of birth(d/m/y): ")
  current_age=int(input("Enter your current age: "))
  date=datetime.strptime(age_year,'%d/%m/%Y').date()

  if((it_date-date).days>=current_age*365):
      print(f"Your age({current_age}) is true")
  else:
      print(f"Your age({current_age}) is false because from your birth year until now it's been {it_date} year")
except:
  print("You set the wrong date")
