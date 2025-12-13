from tkinter import *
from tkinter import messagebox
def saludar():
    nombre = txt_nombre.get()
    print(f"Hola, {nombre}!")
    messagebox.showinfo("Saludo", f"Hola, {nombre}!")

#creamos la ventana principal
app = Tk()
#metodo title para el titulo de la ventana
app.title("Mi primera aplicacion con Tkinter")
#metodo geometry para el tamano de la ventana
app.geometry("300x100")

#frame es un contenedor
frame = Frame(app)
frame.grid(row=0, column=0,padx=10, pady=10)
lb_nombre = Label(frame, text="Nombre:")
lb_nombre.grid(row=0, column=0,padx=5, pady=5)
txt_nombre = Entry(frame)
txt_nombre.grid(row=0, column=1,padx=5, pady=5)
btn_saludar = Button(frame, text="Saludar",command=saludar)
btn_saludar.grid(row=1, column=0, columnspan=2,padx=5, pady=5)


#mostramos la ventana
app.mainloop()
