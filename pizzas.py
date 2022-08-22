people = int(input("¿Cuantas personas? "))
pizzas = int(input("¿Cuantas pizzas? "))
if people <=0 or pizzas <=0:
    print ("Debe ser un numero positivo")
porciones = ""
if people % 2 == 1:
    porciones = people + 1
else:
    porciones = people

print("{} personas toman {} pizzas".format(people, pizzas))
print("Cada persona toma {} porciones".format(pizzas))
print("Sobran {} porciones".format((porciones * pizzas) % people))