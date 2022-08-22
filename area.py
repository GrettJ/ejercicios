
x1 = input("Ingrese la profundidad en metros a medir: ")
x2 = input("Ingrese la anchura en metros a medir: ")
try:
    flx1 = float(x1)
    flx2 = float(x2)
    
    yx1 = flx1*0.914
    yx2 = flx2*0.914
    print(("en m2: {} y en yd2: {}").format(flx1*flx2, yx1*yx2))
except ValueError:
    print("debe introducir un número")


