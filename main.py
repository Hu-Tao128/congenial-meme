import sqlite3

conn = sqlite3.connect("veterinaria.db")

cursor = conn.cursor()


print("Paso 1 conexion de base de datos")



cursor.execute(
    """CREATE TABLE IF NOT EXISTS clientes(
    id integer primary key autoincrement,
    name varchar(50) not null,
    telefono text)
"""
)
print("Paso 2 la tabla creada!!")

cursor.execute("""
    DROP TABLE IF EXISTS user
""")
print("Tabla eliminada")


cursor.execute("""insert into clientes (name, telefono) values ('Alejandro Diaz','664 235 7636')""")
print("INgresaste a almejandro")

conn.commit()

conn.close()

