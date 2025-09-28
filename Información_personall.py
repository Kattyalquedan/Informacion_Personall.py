# informacion_personal.py
"""
Tarea: Trabajando con Diccionarios en Python
Autor: (tu nombre)
"""

# Diccionario inicial con las claves requeridas
informacion_personal = {
    "nombre": "Ariadna Luna",    # Nombre ficticio
    "edad": 29,                  # Edad inicial (se eliminará más adelante)
    "ciudad": "Quito",           # Ciudad inicial
    "profesion": "Ingeniera"     # Profesión inicial
}

# 1) Acceder y modificar la ciudad
# Guardamos el valor actual (opcional) y lo cambiamos
ciudad_actual = informacion_personal["ciudad"]
informacion_personal["ciudad"] = "Guayaquil"  # nueva ciudad

# 2) Agregar/actualizar la clave 'profesion'
# Para dar más detalle, actualizamos el valor de 'profesion'
informacion_personal["profesion"] = "Ingeniera de Datos"

# 3) Verificar existencia de 'telefono' y agregar si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593-99-123-4567"  # número ficticio

# 4) Eliminar la clave 'edad' porque no es necesaria
if "edad" in informacion_personal:
    informacion_personal.pop("edad")

# 5) Imprimir el diccionario final
print(informacion_personal)
