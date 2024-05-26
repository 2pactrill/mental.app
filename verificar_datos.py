import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Ejecutar una consulta para obtener todos los registros de la tabla usuarios
cursor.execute('SELECT * FROM usuarios')
rows = cursor.fetchall()

# Imprimir los datos
for row in rows:
    print(f"ID: {row[0]}, Correo: {row[1]}, Contraseña: {row[2]}, Tipo de Usuario: {row[3]}")

conn.close()
