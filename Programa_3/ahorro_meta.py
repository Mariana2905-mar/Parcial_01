Meta = 0
Meta = float(input("Meta de ahorro: "))

Ahorro_mensual = 0
Ahorro_mensual = float(input("Ahorro mensual: "))

#acumulador y contador
Ahorro_acumulado = 0
Mes = 0

print() 

while Ahorro_acumulado < Meta:
    Mes += 1
    Ahorro_acumulado += Ahorro_mensual
    
    #Imprime todos los meses
    print(f"Mes {Mes}: ${Ahorro_acumulado:,.2f}")

print(f"Meta alcanzada en {Mes} meses.")
