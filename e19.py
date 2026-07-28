import tkinter as tk
import random

secreto=random.randint(1,20)
app=tk.Tk()
vidas=6
entrada=tk.StringVar(app)
VidasSV=tk.StringVar(app)
resultado=tk.StringVar(app)

def intentar():
    global vidas
    print("Entrada: "+ entrada.get())
    if(vidas<0):
        resultado.set("Ha perdido el juego")
        return
    numero_ingresado=int(entrada.get())
    if(numero_ingresado<secreto):
        resultado.set("El número ingresado es muy bajo")
    if(numero_ingresado>secreto):
        resultado.set("El número ingresado es muy alto")
    if(numero_ingresado==secreto):
        resultado.set("Felicidades haz ganado el juego")
    VidasSV.set('Vidas: '+str(vidas))
    vidas=vidas-1


# Anchura y altura
app.geometry("400x500")
app.configure(background='#4fa')
tk.Wm.wm_title(app, "Adivina el número")

tk.Button(
    app,
    text='Adivina',
    font=('sans-serif', 16),
    bg='#f8a',
    command=intentar
).pack(expand=True)


tk.Label(
    app,
    textvariable=VidasSV,
    bg='#de2',
    justify='center'
).pack(expand=True)

tk.Entry(
    app,
    bg='#de2',
    fg='#04e',
    font=('Arial',14),
    justify='center',
    textvariable=entrada
).pack(expand=True)


tk.Label(
    app,
    textvariable=resultado,
    bg='#4fa'
).pack(expand=True)

app.mainloop()
