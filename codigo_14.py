#Desarrollar un programa que calcule la diagonal y la contra diagonal de un array de 4x4.
m=[[1,2,3,4],
   [4,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]
count=0
sum=0
mult=1

csum=0
cmult=1
a=[]
b=[]
for i in range(len(m)):
    for j in range(len(m)):
        if(i==j):
         sum+=m[i][j]
         mult*=m[i][j]
         a.append(m[i][j])

         csum+=m[i][len(m)-count-1]
         cmult*=m[i][len(m)-count-1]
         b.append(m[i][len(m)-count-1])
    count+=1
print(f"The sum of the diagonal({a}) line is: {sum}.\n And the multiplication is: ${mult}.")
print(f"The sum of the versus diagonal({b}) line is: {csum}.\n And the multiplication is: ${cmult}.")
