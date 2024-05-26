import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Crear la tabla de usuarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    correo TEXT NOT NULL,
    contrasena TEXT NOT NULL,
    tipo_usuario TEXT NOT NULL
)
''')

# Confirmar cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos y tabla creadas con éxito.")
