import datetime

ahora = datetime.datetime.now()
año = ahora.year

strEdad = input("¿Cuantos años tienes? ")
strJubilacion = input("¿A qué edad quieres jubilarte? ")

edad = int(strEdad)
jubilacion = int(strJubilacion)

faltan = jubilacion - edad
cuando = año + faltan
if faltan <=0:
    print("Ya puedes jubilarte")
else: 
    print("Te quedan {} años para jubilarte".format(faltan))

    print("Estamos en {}, te jubilarás en {}".format(año, cuando))