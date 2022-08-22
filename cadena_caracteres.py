
carac= input("Ingrese una secuencia de caracteres: ")
print(carac)
print(len(carac))
lcarac= list(carac)  

#Obligar a completar el espacio
def rechazo():
    char= input("Ingrese una secuencia de caracteres: ")
    if char == 0:
        print("debe ingresar algun caracter")
    else:
        print(char,len(char))
    return char 


#sin comando len
def longitud(lcarac):
    contador = 0
    for n in lcarac:
        contador += 1
    return contador

print("Longitud cadena: ", longitud(carac))