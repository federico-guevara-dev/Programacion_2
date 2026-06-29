#Hacer un programa que invierta un array de forma vertical, ej:[1,2,3],[4,5,6] -> [4,5,6], [1,2,4]
A=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(A)//2):
        aux=A[i]
        A[i]=A[-1]
        A[-1]=aux

print(A)
