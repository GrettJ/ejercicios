entrada_1 = float(input("precio 1: "))
entrada_2 = float(input("precio 2: "))
entrada_3 = float(input("precio 3: "))

impuesto_a_añadir = 5.5

def impuestos():
    tasa_1= entrada_1%impuesto_a_añadir
    tasa_2= entrada_2%impuesto_a_añadir
    tasa_3= entrada_3%impuesto_a_añadir
