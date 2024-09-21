# Edad del cliente
Edad= int(input("Ingrese su edad: "))
# Calculo de precio de entrada
if Edad < 4:
    precio= 0
elif 4 <= Edad <= 18:
    precio= 5
else:
    precio= 10
print(f"El precio de su entrada es {precio}")