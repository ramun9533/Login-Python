from tkinter import *
from tkinter import messagebox
import sqlite3

# Crear la base de datos y la tabla si no existen
conn = sqlite3.connect('credenciales_usuarios.db')
cursor = conn.cursor()
#cursor.execute('''
#    CREATE TABLE IF NOT EXISTS users (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        username TEXT UNIQUE,
#        password TEXT
#    )
#''')
conn.commit()
conn.close()

def login():
    uname = e1.get()
    password = e2.get()

    if uname == "" or password == "":
        messagebox.showinfo("", "Blank Not allowed")
    else:
        # Conectar a la base de datos
        conn = sqlite3.connect('credenciales_usuarios.db')
        cursor = conn.cursor()

        # Consultar la base de datos para encontrar el usuario y la contraseña
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (uname, password))
        result = cursor.fetchone()

        conn.close()

        if result:
            messagebox.showinfo("", "Acceso Correcto")
            root.destroy()
        else:
            messagebox.showinfo("", "Password o Usuario Incorrecto ")

# Crear la interfaz gráfica
root = Tk()
root.title("Login")
root.geometry("400x200")

Label(root, text="Login form using Python Tkinter").place(x=5, y=10)

Label(root, text="UserName").place(x=10, y=40)
Label(root, text="Password").place(x=10, y=60)

e1 = Entry(root)
e1.place(x=140, y=40)

e2 = Entry(root)
e2.place(x=140, y=60)
e2.config(show="*")

Button(root, text="Login", command=login, height=2, width=13).place(x=10, y=100)

root.mainloop()
