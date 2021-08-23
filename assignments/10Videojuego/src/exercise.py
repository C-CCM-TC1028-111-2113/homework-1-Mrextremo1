def main():
    #escribe tu código abajo de esta línea
   
    jn = int(input("Dame la cantidad de juegos nuevos: "))
    ju = int(input("Dame la cantidad de juegos usados: "))

    total = (jn*1000)+(ju*350)

    print("El total de la compra es:",total)


if __name__ == '__main__':
    main()
