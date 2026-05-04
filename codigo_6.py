#Un cajero automático entrega sólo billetes de  1000yde 200. Ingresar la cantidad que desea extraer el usuario, y luego indicar cuántos billetes de  1000yde 200 se le entregan. Indicar además el saldo que no se pudo extraer porque no hay billetes.

def cashier(a,k,c):
  if(a>0 and (k>0 and k<a) or (c>0 and c<a)):
    k=a//(k*1000-c*200)
    a=a%(k*1000-c*200)
    x=a//(c*200)
    print(f'{k} bills of thousand and {x-c}')

b=int(input("Enter the amount to withdraw: "))
k=int(input("Enter the number of bills of thousand: "))
c=int(input("Enter the number of bills of two hundred: "))
cashier(b,k,c)