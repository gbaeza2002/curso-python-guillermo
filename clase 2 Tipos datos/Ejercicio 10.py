# ==========================================
# 1. DATOS DEL SISTEMA (No modificar)
# ==========================================
robot = "Rider-5"          # String (Texto)
bateria = 84.5             # Número (Float)
oxigeno = False            # Booleano (True/False)

# ==========================================
# 2. COMPLETA LAS TRES LÍNEAS DE CÓDIGO
# ==========================================

# PARTE 1: Usa el operador + para unir el texto y las variables.
# (Recuerda convertir la batería a string)
parte_1 = "El robot " + + " reporta una batería del " +  + "%."

# PARTE 2: Usa el método .format() con llaves {} para rellenar los datos.
parte_2 = "Alerta: ¿Hay oxígeno? R: {}. Estado de {}: Operativo.".format()

# PARTE 3: Usa una f-string (f"") e introduce las variables en las llaves.
parte_3 = f"Decisión: Con {}% de energía, {} inicia la misión."


# ==========================================
# 3. IMPRESIÓN DE RESULTADOS
# ==========================================
print("--- RESULTADO FINAL DE LA HISTORIA ---")
print(parte_1)
print(parte_2)
print(parte_3)

"""
--- RESULTADO FINAL DE LA HISTORIA ---
El robot Rider-5 reporta una batería del 84.5%.
Alerta: ¿Hay oxígeno? R: False. Estado de Rider-5: Operativo.
Decisión: Con 84.5% de energía, Rider-5 inicia la misión.
"""