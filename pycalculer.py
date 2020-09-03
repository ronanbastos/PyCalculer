
def medidaDoisAngulos():
    
    x = 0

    l1=int(input("angulo 1: "))
    l2=int(input("angulo 2: "))
    cal = l1+l2

    while True:
       x += 1
       caltotal = x + cal
      
       
       if caltotal == 180:
           print("Achei o valor de x:" + str(x)) 
           break
    return x  
def usandoVariaveis():
        x = 0

        l1="x"
        print("angulo: x")
        l2="2x"
        print("angulo: 2x")
        l3=input("angulo 3: ")


        lbk1=l1
        lbk2=l2
        lbk3=l3

        verficaX1 =  False
        verficaX2 =  False
        verficaX3 =  False
        verficaXX1=  False
        verficaXX2=  False
        verficaXX3=  False
        if l1 not in "x":

            lbk1=str(l1+"º")
        if l1 == "x": 
            l1 = int(1)
            lbk1="x"
            verficaX1= True
        if "x"  in  str(l1):
            l1= l1[:1] # Tirando o x da variavel l1 ex(2x casa1= 2 casa2=x  2:x -> l1[:1]) )
            lbk1=str(l1+"x")
            verficaXX1=True
        if l2 not in "x":
    
            lbk2=str(l2+"º")
        if l2 == "x": 
            l2 = 1
            lbk2="x"
            verficaX2= True
        if "x" in str(l2):
            l2= l2[:1]
            lbk2=str(l2+"x")
            verficaXX2=True
        if l3 not in "x":

            lbk3=str(l3+"º")
        if l3 == "x": 
            l3 = int(1)
            verficaX3= True
        if "x" in str(l3): 
            l3= l3[:1]
            lbk3=str(l3+"x")
            verficaXX2=True


        if verficaX1 == True and verficaXX2 == True:
            cal = int(l1)+int(l2)
            calv=lbk1+"+"+lbk2+"+"+lbk3+"="+str(cal)+"x"+"+"+lbk3
            print(calv)
            calv= str(180)+"º"+"-"+"("+str(cal)+"x"+"+"+lbk3+")"+"="+"0" #formula de ativação
            print(calv)
            cal= 180-int(l3)
            x7 = cal
            print(str(cal)+"-"+str(int(l1)+int(l2))+"x"+"="+"0")
            cal= int(cal / (int(l1)+int(l2)))
            print("----------------------------")    
            print(x7)
            print("______________"+"="+str(cal))
            print(int(l1)+int(l2))   
            print("----------------------------") 
            while True:
               x += 1
               y = cal
               z = l3
               caltotal = x + int(y) + int(z) 

               
               if caltotal == 180:
                   print("Achei o valor de x:" + str(x))
                   print(str(l3)+"+"+str(cal)+"+"+str(x)+"="+str(caltotal))
                   break
            return x                            
def casoEspecial():
    x = 0

    l1=input("coloque valor angulo: ")
    cal = int(l1)+int(l1)
    print("O lado espelhado é :"+str(cal))
    while True:
               x += 1
               y = cal
               caltotal = x + int(y) 
              
               
               if caltotal == 180:
                   print("Achei o valor de x:" + str(x)) 
                   break
    return x                 
def casoEspecial90():
    x = 0

    l1=input("coloque valor angulo: ")
    l2=90
    cal = int(l1)+int(l2)
    print("O lado espelhado é :"+str(cal))
    while True:
               x += 1
               y = cal
               caltotal = x + int(y) 
             
               
               if caltotal == 180:
                   print("Achei o valor de x:" + str(x)) 
                   break
    return x
def UseOdiametro():
    print("""
    c= circumference
    Pi = 3.14
    d = diametro
         """)
    r=int(input("coloque valor Raio: "))
    d=int(input("coloque valor diametro: "))
    x = d+r+r
    c = x*3.14
    print("A circumference é: "+str(c))
    return c
def UseOraio():
    print("""
    c= circumference
    Pi = 3.14
    d = diametro
         """)
    r=int(input("coloque valor Raio: "))
    c = 2*3.14*5
    print("A circumference é: "+str(c))
    return c
def menu():
    x1=0
    while True:
        x1+=1
        if x1 == 1:
            print("Escolha uma opção!")
        else:
            print("                    ")
            print("                    ")
            print("Escolha outra opção!")    
        print("______________________")
        print("1 = Medida Dois Angulos ")
        print("2 = Usando Variaveis ")
        print("3 = Caso Especial")
        print("4 = Caso Especial 90º")
        print("5 = Calcular Circunferência Círculoº com diametro")
        print("6 = Calcular Circunferência Círculoº com raio")
        print("0 = Sair ")
        print("______________________")
        op= input("Qual opção agora> ")
        if op == "6":   
            UseOraio()
        if op == "5":   
            UseOdiametro()
        if op == "4":   
            casoEspecial90()
        if op == "3":   
            casoEspecial()
        if op == "2":   
            usandoVariaveis()
        if op == "1":
            medidaDoisAngulos()
        if op == "0":
            break

#menu()
