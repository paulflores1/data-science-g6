from tkinter import *
from tkinter import messagebox as Messagebox


def ingresar():
    dni = txt_dni.get()
    nombre = txt_nombre.get()
    email = txt_email.get()
    Messagebox.showinfo("Datos Ingresados", f"DNI: {dni}\nNombre: {nombre}\nEmail: {email}")

app = Tk()
app.title("Gestion Alumnos")
app.geometry("320x150")


frame = Frame(app)
frame.grid(row=0, column=0,padx=10, pady=10)
lb_dni = Label(frame, text="DNI:")
lb_dni.grid(row=0, column=0,padx=5, pady=5)
txt_dni = Entry(frame, width=35)
txt_dni.grid(row=0, column=1,padx=5, pady=5)



lb_nombres = Label(frame, text="Nombre:")
lb_nombres.grid(row=1, column=0,padx=5, pady=5)
txt_nombre = Entry(frame, width=35)
txt_nombre.grid(row=1, column=1,padx=5, pady=5)

lb_email = Label(frame, text="Email:")
lb_email.grid(row=2, column=0,padx=5, pady=5)
txt_email = Entry(frame, width=35)
txt_email.grid(row=2, column=1,padx=5, pady=5)

btn_ingresar = Button(frame, text="Mostrar",command = ingresar,width=30)
btn_ingresar.grid(row=3, column=0, columnspan=2,padx=5, pady=5,)


    




app.mainloop()