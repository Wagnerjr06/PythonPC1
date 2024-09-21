# Solicitar hora al usuario
hora= input("Ingrese la hora en formato 24 horas (HH:MM): ")

# Horas y minutos
horas, minutos= map(int, hora.split(':'))

# Verificar si corresponde desayuno, almuerzo o cena
if (7 <= horas < 8) or (horas == 8 and minutos == 0):
    print("Es la hora del desayuno")
elif (12 <= horas < 13) or (horas == 13 and minutos == 0):
    print("Es la hora del almuerzo")
elif (18 <= horas < 19) or (horas == 19 and minutos == 0):
    print("Es la hora de la cena")
else:
    print("")