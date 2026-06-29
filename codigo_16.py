#Hacer un programa que invierta un array de forma horizontal, ej:[1,2,3] -> [3,2,1]
A=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(A)):
    for j in range(len(A[i])//2):
        aux=A[i][j]
        A[i][j]=A[i][-1]
        A[i][-1]=aux

print(A)
