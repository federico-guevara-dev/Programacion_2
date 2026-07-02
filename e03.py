#Conversor Decimal-Binario Hex. Diseñar un programa que el usuario ingresa un número y desde que sistema hacia que sistema de numeración. Además mostrar el carácter ASCII que corresponde al número.

def converter(num,a,b):
  a=a.lower()
  b=b.lower()
  if((a==b)&(num>0)):
    print(num)
  elif((a!=b)&(num>0)&(a=='b')&(b=='d')):
    num=str(num)
    dec=int(num,2)
    print(f'The binary {num} to decimal is: {dec}')
  elif((a!=b)&(num>0)&(a=='b')&(b=='h')):
    num=str(num)
    num=int(num,2)
    print(f'The binary to {hex(num)}')
  elif((a!=b)&(num>0)&(a=='d')&(b=='b')):
    num=str(num)
    print(f'The decimal {num} to binary is: {bin(int(num))}')
  elif((a!=b)&(num>0)&(a=='h')&(b=='b')):
    num=str(num)
    print(f'The hex {num} to binary is: {bin(int(num,16))}')
  elif((a!=b)&(num>0)&(a=='d')&(b=='h')):
    num=str(num)
    print(f'The decimal {num} to hex is: {hex(int(num))}')
  elif((a!=b)&(num>0)&(a=='h')&(b=='d')):
    num=str(num)
    print(f'The hex {num} to decimal is: {int(num,16)}')

n=int(input("Enter a number: "))
a=input("Enter the initial system: ")
b=input("Enter the final system: ")
converter(n,a,b)