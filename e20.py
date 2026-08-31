import tkinter as tk

app=tk.Tk()
entrada1=tk.StringVar(app)
entrada2=tk.IntVar(app)

CifradoCesar=tk.StringVar(app)
resultado=tk.StringVar(app)

def cifrado():
  stri=""
  msg=entrada1.get()
  msg=msg.lower()
  desp=entrada2.get()

  for i in msg:
     if "a"<=i and "z">=i:
        # 97 es el valor ASCII de 'a'
        # Se resta 97 para llevar el rango de 0 a 25, se aplica el desplazamiento,
        # se usa % 26 para la rotación y se vuelve a sumar 97.
        asc=(ord(i)-97+desp)%26+97
        stri+=chr(asc)
  
  CifradoCesar.set('Cifrado Cesar: '+stri)

  return stri

# Anchura y altura
app.geometry("400x500")
app.configure(background='#4fa')
# Título de la ventana
tk.Wm.wm_title(app, "Cifrado Cesar")

#Botón que cifra la frase ingresada
tk.Button(
    app,
    text='Cifralo',
    font=('sans-serif', 16),
    bg='#f8a',
    command=cifrado

).pack(expand=True)

# Frase convertida
tk.Label(
    app,
    textvariable=CifradoCesar,
    bg='#de2',
    justify='center'
).pack(expand=True)

# entrada 1 es la frase
tk.Entry(
    app,
    bg='#de2',
    fg='#04e',
    font=('Arial',14),
    justify='center',
    textvariable=entrada1
).pack(expand=True)

# entrada 2 es el dezplazamiento
tk.Entry(
    app,
    bg='#de2',
    fg='#04e',
    font=('Arial',14),
    justify='center',
    textvariable=entrada2
).pack(expand=True)

app.mainloop() 