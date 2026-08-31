# 1. Contadores iniciales
total_p = 0
total_f = 0
racha = 0
mejor_racha = 0

print("Ingresa P (Presente) o F (Falta). Escribe FIN para terminar.")

# 2. Creamos una variable vacía para empezar
letra = ""

# 3. El ciclo se repite mientras el usuario NO escriba "FIN"
while letra != "FIN":
    letra = input("Asistencia: ").upper()
    
    if letra == "P":
        total_p += 1
        racha += 1
        if racha > mejor_racha:
            mejor_racha = racha
            
    elif letra == "F":
        total_f += 1
        racha = 0

# 4. Resultados finales
print("Total de asistencias:", total_p)
print("Total de faltas:", total_f)
print("Mayor racha de asistencias consecutivas:", mejor_racha)