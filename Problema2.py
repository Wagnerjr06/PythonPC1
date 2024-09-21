# Solicitar la cantidad consumida
Consumo= float(input("Ingrese la cantidad consumida: "))
# Solicitar la cantidad de propina a dejar
Propina= float(input("Ingrese el porcentaje de propina que dará: "))
# Calculo de la propina
Propina_final= Consumo * (Propina/100)
# Propina
print(f"La propina a dejar es {Propina_final}")