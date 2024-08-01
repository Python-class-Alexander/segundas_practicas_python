# BUCLES DEL TIPO WHILE

# 1. Escribe las lineas que faltan en el codigo para que se escriba del 1 al 12
a = 0
while a < 12:
    a = a + 1
    print(a)

# 2. Modifica el codigo anterior para que se cree un contadoe infinito
# a = 0
# while a == a:
#     a = a + 1
#     print(a)

# 3. Escriba la linea de codigo que falta de forma que el prograama pregunte por el nombre, hasta que que se escriba carlos
nombre = ""
while nombre != "carlos":
    nombre = input("Escribe tu nombre: ")
print("Hola Carlos")