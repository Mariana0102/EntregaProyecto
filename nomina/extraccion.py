import sqlite3

def obtener_correos():
    # Conexión a la base de datos SQLite
    conexion = sqlite3.connect('db.sqlite3')
    cursor = conexion.cursor()
    
    # Consulta para obtener los correos de la tabla auth_user
    cursor.execute("SELECT email FROM auth_user")
    correos = [registro[0] for registro in cursor.fetchall()]
    
    # Cerrar conexión y retornar los correos
    conexion.close()
    return correos

def obtener_usuarios():
    # Conexión a la base de datos SQLite
    conexion = sqlite3.connect('db.sqlite3')
    cursor = conexion.cursor()
    
    # Consulta para obtener los correos de la tabla auth_user
    cursor.execute("SELECT first_name FROM auth_user")
    nombre = [registro[0] for registro in cursor.fetchall()]
    cursor.execute("SELECT last_name FROM auth_user")
    apellido = [registro[0] for registro in cursor.fetchall()]
    nombrecompleto=[]
    for i in range(0, len(nombre)):
        nombrecompleto.append(f"{nombre[i]} {apellido[i]}")
    # Cerrar conexión y retornar los correos
    conexion.close()
    return nombrecompleto

def guardar_correos_en_archivo(correos, archivo):
    with open(archivo, 'w') as f:
        for correo in correos:
            f.write(correo + '\n')
