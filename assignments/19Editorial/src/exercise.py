import math
def main():
    #escribe tu código abajo de esta línea
    palabras = int(input("Dame el número de palabras: "))

    ppag = (math.ceil(palabras/475))*60
    descuento = (ppag*10)/100
    costo = ppag-descuento

    print("El costo de la publicación es:",costo)


if __name__ == '__main__':
    main()
