import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("400x300")
        
        # Etiqueta y campo para el correo electrónico
        self.label_email = ttk.Label(root, text="Correo Electrónico:")
        self.label_email.pack(pady=10)
        self.entry_email = ttk.Entry(root, width=30)
        self.entry_email.pack()
        
        # Etiqueta y campo para la contraseña
        self.label_password = ttk.Label(root, text="Contraseña:")
        self.label_password.pack(pady=10)
        self.entry_password = ttk.Entry(root, width=30, show="*")
        self.entry_password.pack()
        
        # Selección del tipo de usuario
        self.user_type = tk.StringVar()
        self.radio_student = ttk.Radiobutton(root, text="Alumno", variable=self.user_type, value="alumno")
        self.radio_teacher = ttk.Radiobutton(root, text="Docente", variable=self.user_type, value="docente")
        self.radio_student.pack(pady=5)
        self.radio_teacher.pack(pady=5)
        
        # Botón de inicio de sesión
        self.button_login = ttk.Button(root, text="Iniciar Sesión", command=self.login)
        self.button_login.pack(pady=10)
        
        # Enlace para crear un nuevo correo electrónico para alumnos
        self.label_new_email = tk.Label(root, text="Si no tiene un correo institucional, haga clic aquí para crear uno.", fg="blue", cursor="hand2")
        self.label_new_email.pack(pady=10)
        self.label_new_email.bind("<Button-1>", self.create_new_email)
        
    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        user_type = self.user_type.get()
        
        if not email or not password or not user_type:
            messagebox.showwarning("Error de Entrada", "Por favor, complete todos los campos y seleccione un tipo de usuario.")
            return
        
        # Aquí puedes agregar la lógica de autenticación
        
        messagebox.showinfo("Inicio de Sesión", f"Sesión iniciada como {user_type.capitalize()}")
        
    def create_new_email(self, event):
        new_email_window = tk.Toplevel(self.root)
        new_email_window.title("Crear Nuevo Correo")
        new_email_window.geometry("400x300")
        
        # Lógica para la creación de un nuevo correo
        label_info = ttk.Label(new_email_window, text="Ingrese los datos para crear un nuevo correo institucional:")
        label_info.pack(pady=10)
        
        label_new_email = ttk.Label(new_email_window, text="Nuevo Correo:")
        label_new_email.pack(pady=10)
        entry_new_email = ttk.Entry(new_email_window, width=30)
        entry_new_email.pack()
        
        label_password = ttk.Label(new_email_window, text="Contraseña:")
        label_password.pack(pady=10)
        entry_password = ttk.Entry(new_email_window, width=30, show="*")
        entry_password.pack()
        
        button_create = ttk.Button(new_email_window, text="Crear", command=lambda: self.create_email(entry_new_email.get(), entry_password.get(), new_email_window))
        button_create.pack(pady=10)
    
    def create_email(self, email, password, window):
        if not email or not password:
            messagebox.showwarning("Error de Entrada", "Por favor, complete todos los campos.")
            return
        
        # Conectar a la base de datos
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        
        # Insertar el nuevo usuario en la base de datos
        cursor.execute('''
        INSERT INTO usuarios (correo, contrasena, tipo_usuario)
        VALUES (?, ?, ?)
        ''', (email, password, 'alumno'))
        
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Correo Creado", "¡Nuevo correo institucional creado con éxito!")
        window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
