def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    
    mensajes = int(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    min = int(input("Dame el número de minutos: "))

    cm = (mensajes+megas+min)*0.8

    print("El costo mensual es:",cm)


if __name__ == '__main__':
    main()
