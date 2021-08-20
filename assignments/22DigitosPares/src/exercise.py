def main():
    #escribe tu código abajo de esta línea
    count = 0
    num = int(input("Dame un número: "))
    nnum = num
    snum = num.__str__
    
    for x in range(10):
        if (nnum-2000) <= 2000 and (nnum-2000) < 1000 and (nnum -2000) >= 0:
            count = 1
            #print("par",nnum)
            nnum = nnum + 2000
            for x in range(30):
                #print(nnum)
                if (nnum-200) <= 200 and (nnum-200) < 100 and (nnum -200) >= 0:
                    #print("par",nnum)
                    count =2
                    nnum = nnum + 200
                    for x in range(30):
                        if (nnum-20) <= 20 and (nnum-20) < 10 and (nnum -20) >= 0:
                            #print("par",nnum)
                            count =3
                            nnum = nnum + 20
                            for x in range(30):
                                if (nnum-2) <= 2 and (nnum-2) < 1 and (nnum -2) >= 0:
                                    #print("par",nnum)
                                    count =4
                                    break
                                elif (nnum - 2) <= -1:
                                    count = 3
                                    #print("impar",nnum)
                                    break
                                else:
                                    nnum = nnum - 2
                            break
                        elif (nnum - 20) <= -10:
                            count = 2
                            #print("impar",nnum)
                            nnum = nnum + 20
                            for x in range(30):
                                if (nnum-2) <= 2 and (nnum-2) < 1 and (nnum -2) >= 0:
                                    #print("par",nnum)
                                    count =3
                                    break
                                elif (nnum - 2) <= -1:
                                    count = 2
                                    #print("impar",nnum)
                                    break
                                else:
                                    nnum = nnum - 2
                            break
                        else:
                            nnum = nnum - 20
                    break
                elif (nnum - 200) <= -100:
                    count = 1
                    nnum = nnum + 200
                    for x in range(30):
                        if (nnum-20) <= 20 and (nnum-20) < 10 and (nnum -20) >= 0:
                            #print("par",nnum)
                            count =2
                            nnum = nnum + 20
                            for x in range(30):
                                if (nnum-2) <= 2 and (nnum-2) < 1 and (nnum -2) >= 0:
                                    #print("par",nnum)
                                    count =3
                                    break
                                elif (nnum - 2) <= -1:
                                    count = 2
                                    #print("impar",nnum)
                                    break
                                else:
                                    nnum = nnum - 2
                            break
                        elif (nnum - 20) <= -10:
                            count = 1
                            #print("impar",nnum)
                            nnum = nnum + 20
                            for x in range(30):
                                if (nnum-2) <= 2 and (nnum-2) < 1 and (nnum -2) >= 0:
                                    #print("par",nnum)
                                    count =2
                                    break
                                elif (nnum - 2) <= -1:
                                    count = 1
                                    #print("impar",nnum)
                                    break
                                else:
                                    nnum = nnum - 2
                            break
                        else:
                            nnum = nnum - 20
                    break
                else:
                    nnum = nnum - 200
            break

        elif (nnum - 2000) < 0:
            count = 0
            #print("par",nnum)
            nnum = nnum + 2000
            for x in range(30):
                #print(nnum)
                if (nnum-200) <= 200 and (nnum-200) < 100 and (nnum -200) >= 0:
                    #print("par",nnum)
                    count =1
                    nnum = nnum + 200
                    for x in range(30):
                        if (nnum-20) <= 20 and (nnum-20) < 10 and (nnum -20) >= 0:
                            #print("par",nnum)
                            count =2
                            nnum = nnum + 20
                            for x in range(30):
                                if (nnum-2) <= 2 and (nnum-2) < 1 and (nnum -2) >= 0:
                                    #print("par",nnum)
                                    count =3
                                    break
                                elif (nnum - 2) <= -1:
                                    count = 2
                                    #print("impar",nnum)
                                    break
                                else:
                                    nnum = nnum - 2
                            break
                        elif (nnum - 20) <= -10:
                            count = 1
                            #print("impar",nnum)
                            nnum = nnum + 20
                            for x in range(30):
                                if (nnum-2) <= 2 and (nnum-2) < 1 and (nnum -2) >= 0:
                                    #print("par",nnum)
                                    count =2
                                    break
                                elif (nnum - 2) <= -1:
                                    count = 1
                                    #print("impar",nnum)
                                    break
                                else:
                                    nnum = nnum - 2
                            break
                        else:
                            nnum = nnum - 20
                    break
                elif (nnum - 200) <= -100:
                    count = 0
                    nnum = nnum + 200
                    for x in range(30):
                        if (nnum-20) <= 20 and (nnum-20) < 10 and (nnum -20) >= 0:
                            #print("par",nnum)
                            count =1
                            nnum = nnum + 20
                            for x in range(30):
                                if (nnum-2) <= 2 and (nnum-2) < 1 and (nnum -2) >= 0:
                                    #print("par",nnum)
                                    count =2
                                    break
                                elif (nnum - 2) <= -1:
                                    count = 1
                                    #print("impar",nnum)
                                    break
                                else:
                                    nnum = nnum - 2
                            break
                        elif (nnum - 20) <= -10:
                            count = 0
                            #print("impar",nnum)
                            nnum = nnum + 20
                            for x in range(30):
                                if (nnum-2) <= 2 and (nnum-2) < 1 and (nnum -2) >= 0:
                                    #print("par",nnum)
                                    count =1
                                    break
                                elif (nnum - 2) <= -1:
                                    count = 0
                                    #print("impar",nnum)
                                    break
                                else:
                                    nnum = nnum - 2
                            break
                        else:
                            nnum = nnum - 20
                    break
                else:
                    nnum = nnum - 200
            break
        else:
            nnum = nnum-2000
    
    print("El número de dígitos pares es:",count)
            
            
            
        
        
    
        
        
        

    
    #print(num.split(4,-1))
    
    #count = int()
    
    #nmil = num/2000
    #ncien = num/200
    #ndiez = num/20
    #n1 = num/2

    #if (nmil >= 1 and nmil <=1.5) or (nmil >= 2 and nmil <=2.5) or (nmil >= 3 and nmil <=3.5) or (nmil >= 4 and nmil <=4.5):
    #    count + 1

    
    #if (ncien >= 1 and ncien <=1.5) or (ncien >= 2 and ncien <=2.5) or (ncien >= 3 and ncien <=3.5) or (ncien >= 4 and ncien <=4.5):
    #    count +1

    
            
        





if __name__ == '__main__':
    main()
