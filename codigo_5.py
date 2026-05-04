#Un profesor tiene 'X' caramelos y los quiere repartir entre 'Y' estudiantes reciben un número entero de caramelos. Preguntar al usuario X e Y. Luego indicar cuántos caramelos le tocan a cada estudiante y cuantos sobran en la bolsa.

def rest(X,Y):
  if(X>0 and Y>0 and X/Y>=0):
    print(f'The number of candy is {X} and the number of students is {Y} so for each student there are {X//Y} candies, and the rest in the bag is {X%Y}.')
  else:
    print("Amount not found or not properly specified.")
c=int(input("Enter the number of candies: "))
s=int(input("Enter the number of students: "))
rest(c,s)