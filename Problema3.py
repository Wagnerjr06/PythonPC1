# Peso por producto
peso_payaso= 112
peso_muñeca= 75
# Cantidad de payasos y muñecas
Payasos= int(input("Ingrese la cantidad de payasos vendidos: "))
Muñecas= int(input("Ingrese la cantidad de muñecas vendidas: "))
# Calculo del peso final
Peso_final=(peso_payaso * Payasos) + (peso_muñeca * Muñecas)
print(f"El peso total del paquete a ser enviado es {Peso_final}")
