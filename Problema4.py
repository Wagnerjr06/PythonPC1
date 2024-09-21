# Ingresar numero
N= int(input("Ingrese un entero positivo: "))
# Verificar si es positivo
if N <= 0:
    print("Por favor ingresar un número entero positivo")
else:
    suma= sum(range(1, N + 1))
print(f"La suma de los enteros positivos desde 1 hasta la {N} es {suma}")
