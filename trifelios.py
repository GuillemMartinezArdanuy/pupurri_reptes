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
    while(len(paraula1)>=contador):
        if len(listaParaula1[contador:contador+2]) ==2:
            conjunt1.append("".join(listaParaula1[contador:contador+2])) # de 2 en 2 les silabes
        if len(listaParaula1[contador:contador+3]) ==3:
            conjunt1.append("".join(listaParaula1[contador:contador+3])) # de 3 en 3 les silabes
        contador += 1
    #print("conjunt1 :", conjunt1)

    contador=0
    while(len(paraula2)>=contador):
        if len(listaParaula2[contador:contador + 2]) ==2:
            conjunt2.append("".join(listaParaula2[contador:contador+2])) # de 2 en 2 les silabes
        if len(listaParaula2[contador:contador + 3]) ==3:
            conjunt2.append("".join(listaParaula2[contador:contador+3])) # de 3 en 3 les silabes
        contador += 1
    #print("conjunt2 :", conjunt2)


    repeticioDeConjunts=0;
    listaConjunta=[]



    for i in conjunt1:
        if i in conjunt2:
            listaConjunta.append(i)
            repeticioDeConjunts+=1

    #print("total Repeticions= :", repeticioDeConjunts)
    #print("lista Conjunta= : ", listaConjunta)

    # tamany paraules iguals i numero repeticions conjunts = tamanyparaula-1, llavors es trifelio

    if len(paraula2) == len(paraula1) and repeticioDeConjunts%2==0 and len(listaConjunta) >0: # si es parell la repeticio de conjunt vol dir que les silabes de una i altra tenen sentit ja mon , mon ja
        #print("@@@@@@ paraules trifelies", paraula1, "  ", paraula2)
        return "SI"
    else:
       # print("------ paraules NO trifelies", paraula1, "  ", paraula2)
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
