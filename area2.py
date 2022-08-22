exit = False
while exit != True:
        
    entrada = input("Indique si la medición sera en metros o yardas (M/Y): ").upper()
    try:
        if entrada == "M" or entrada == "Y":
            while exit != True:
                try:

                    x1 = int(input("Ingrese la profundidad a medir: "))
                    x2 = int(input("Ingrese la anchura a medir: "))
                                                       
                    if entrada == "M":
                        print(("en m2: {} y en yd2: {}").format(x1*x2, x1*x2*0.914))
                        exit = True
                    elif entrada == "Y":
                        print(("en m2: {} y en yd2: {}").format(x1*x2/0.914, x1*x2))
                        exit = True
                    else:
                        print("Ha ingresado un valor incorrecto, por favor ingrese un número")

                except ValueError:
                    print("Ingrese un número, idiota")
        else:
            print("Ha ingresado", entrada, "Ingrese M o Y")

    except ValueError:
        print("Debe ingresar la letra M o Y")

