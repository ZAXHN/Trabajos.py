'''
Zariel Carmelo Hernández Neri  n° 1218100436 GDS0152
'''
def cels_a_fahr(c):
    f = (c* 1.8) + 32
    return f

def fahr_a_cels(f):
    c = (f - 32) / 1.8
    return c


def menu():
        print("______________________")
        print("Conversor de temperatura")
        print("1- Fahrenheit a Celsius")
        print("2- Celsisus a Fahrenheit")
        print("3- salir")
        opcion = input("-->")
        if(opcion == 1):
            grados = float(input("Introduce °F:"))
            c = (grados - 32) / 1.8
            print("Son", c, " Celsius")

def pedir_grados(escala):
    if escala == "1":
        grados = float(input("Introduce °F: "))
    elif escala == "2":
        grados = float(input("Introduce °C: "))
    return grados

def mostrar_resultado(escala, grados):
    if escala == "1":
        print("Son,",grados, "Celsius")
    elif ecala == "2":
        print("Son", grados, "Fahrenheit")
            
            
while True:
    op = menu()
    if op == "3":
        break
    elif op == "1" or op == "2":
        gr = pedir_grados(op)
        if op == "1":
            conversion = fahr_a_cels(gr)
        if op == "2":
            conversion = cels_a_fahr(gr)
        mostrar_resultado(op, conversion)
    else:
        print("Introduce una opcion correcta.")
    
