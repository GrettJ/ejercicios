tasa_litros = 0.05

x1= float(input("Indique el alto de la habitacion a pintar en m: "))
x2= float(input("Indique el largo de la habitacion a pintar en m: "))
dimensiones = x1*x2
litros = tasa_litros*dimensiones
botes = litros//5

botes += 1 if litros % 5 > 0 else 0

print ("Necesitaras {} litros para pintura {} metros cuadrados de techo.".format(round(litros,2), round(dimensiones,2)))
print ("Debes comprar {} botes de pintura".format(botes))
