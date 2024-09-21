# Lista original
lista= ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
#Eliminamos datos
Resultado= [lista[i] for i in range(len(lista)) if i not in (0,4,5)]
print(Resultado)