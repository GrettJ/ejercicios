n1= input("Introduzca un número: ")
n2= input("Introduzca otro número: ")

if n1 != "" or n2 != "":
    while True:
        try:
            intn1= int(n1)
            intn2= int(n2)
            print("{} + {} = {}\n{} - {} = {}\n{} · {} = {}\n{} / {} = {}\n".format(n1, n2, n1+n2, n1, n2, n1-n2, n1, n2, n1*n2, n1, n2, n1/n2))
            break
        except ValueError:
            print("Debe ingresar un número")
            

 