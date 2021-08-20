def main():
    #escribe tu código abajo de esta línea
    saldo = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))

    Nsaldo = saldo + ingresos - egresos - (cheques*13)
    impuesto = (Nsaldo*7.5)/100

    SaldoF = Nsaldo - impuesto

    print("El saldo final de la cuenta es:",SaldoF)

if __name__ == '__main__':
    main()
