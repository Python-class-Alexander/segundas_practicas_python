# BIFURCACIONES
# Es una estructura de control que permite que le programa ejecuete una condicion especifica

# 1. Completa el codigo siguiente par que diga Buenos dias siempre y cuando se introduzca el nombre de Ana
nombre = input("Introduce tu nombre: ")
if nombre == "Ana":
    print("Buenos dias")

# 2. Completa el codigo siguinte para que diga "Coge un pastel" siempre y cuando se introduzca Pastel. De lo contrario has qui le ofrezaca una Galleta
comida = input("¿Cual es tu comida favorita?: ")
if comida == "pastel":
    print("Coge un pastel")
else:
     print("Coge un galleta")

# 3. Añade el codigo necesario al programa anterior par que ofreza una taza de chocolate sea cual sea la comida favorita
comida1 = input("¿Cual es tu comida favorita?: ")
if comida1 == "pastel":
    print("Coge un pastel")
else:
     print("Taza de chocolate")
