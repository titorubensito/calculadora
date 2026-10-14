def calculadora(operador, tnum, onum):

    if operador == "+":
        resultado = onum + tnum
        
    elif operador == "-":
        resultado = onum - tnum

    elif operador == "*":
        resultado = onum * tnum

    elif operador == "/":
        if tnum == 0:
            print("No se puede dividir por cero.")
            return None
        resultado = onum / tnum
        
    else:
        print("Operador no valido")
        return None
    
    print(onum, operador, tnum, "=", resultado)
    return resultado
    
while True: 
    try:
        onum = int(input("Ingrese un numero: "))
    except ValueError:
        print("No has introducido un numero entero.")
    else: 
        print("Has introducido: ", onum)
        break
    
while True:
    operador = input("Elegir operador: +, -, *, / : ")
    
    while True: 
        try:
            tnum = int(input("Ingrese otro numero: "))
            break
        except ValueError:
            print("No has introducido un numero entero.")
            
            
    resultado = calculadora(operador, tnum, onum)

    eleccion = input("¿Quieres seguir calculando? y/n")

    if eleccion != "y":
        break

    onum = resultado


