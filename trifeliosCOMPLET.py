def trifeli(paraula1,paraula2):
    paraula1=paraula1.lower() #convertim a minuscules
    paraula2=paraula2.lower()
    listaParaula1=list(paraula1)
    listaParaula2=list(paraula2)
    #print(paraula1)
    #maxim silabes de 3
    #calculem tots els conjunts per exempla de monja es :  mo , mon ,nja,ja , de jamon es: ja, jam, mon,on
    conjunt1=[]
    conjunt2=[]

    contador=0
    i=len(paraula1)
    if paraula1 == paraula2:
        return "NO"

    while contador <= len(paraula1):
        while i>contador:
            #print(" -- dins whileee  --- contador val :", contador)
            #print("i val : ", i)
            aAfegir=listaParaula1[contador:i]
            #print(aAfegir)
            conjunt1.append("".join(list(aAfegir)))
            i-=1

        #print("fi del while")
        contador+=1
        #print("contador val : ",contador)
        i=len(paraula1)
        #print("len paraula 1 val: ", i)
        convinacionsP1 = ''.join(conjunt1)
   # print("la paraula :",paraula1,"te aquesta cadena de convinacions :", convinacionsP1)



    contador = 0
    i = len(paraula2)
    while contador <= len(paraula2):
        while i > contador:
       #     print(" -- dins whileee  --- contador val :", contador)
        #    print("i val : ", i)
            aAfegir = listaParaula2[contador:i]
         #   print(aAfegir)
            conjunt2.append(''.join(list(aAfegir)))
            i -= 1

        #print("fi del while")
        contador += 1
        #print("contador val : ", contador)
        i = len(paraula2)
        #print("len paraula 2 val: ", i)
    convinacionsP2=''.join(conjunt2)
   # print("la paraula :",paraula2,"te aquesta cadena de convinacions :", convinacionsP2)

    if paraula1 in convinacionsP2:
      #  print("convinacio yes")
        return "SI"
    else:
       # print("convinacio no")
        return "NO"


#numeroCasos=int(input("numero de casos ?"))
numeroCasos=int(input())
for i in range(numeroCasos):
    #p1 = input("paraula1")
    #p2 = input("paraula2")
    entrada=input()
    p1=entrada.split(" ")[0]
    p2 = entrada.split(" ")[1]

    #p2=input()
    print(trifeli(p1,p2))

