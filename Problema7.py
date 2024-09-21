menu="""
    Bienvenidos al programa trainee
    1. Sumar números
    2. Restar números
    3. Multiplicar números
    4. Salir
"""
print(menu)
opcion=int(input("Ingrese la opcion deseada: "))

if opcion == 1:
    Numerone=float(input("Ingrese el numero 1: "))
    Numertwo=float(input("Ingrese el numero 2: "))
    Resultado= Numerone + Numertwo
    print(f"La suma de ambos numeros es {Resultado}")
elif opcion == 2:
    Numerone=float(input("Ingrese el numero 1: "))
    Numertwo=float(input("Ingrese el numero 2: "))
    Resultado= Numerone - Numertwo
    print(f"La resta de ambos numeros es {Resultado}")
elif opcion == 3:
    Numerone=float(input("Ingrese el numero 1: "))
    Numertwo=float(input("Ingrese el numero 2: "))
    Resultado= Numerone * Numertwo
    print(f"La multiplicación de ambos numeros es {Resultado}")
else:
    print("Opcion no valida")