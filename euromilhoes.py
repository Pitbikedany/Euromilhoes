import random
import os


NumerosUser = []
EstrelasUser = []
repeticao = 0
contadornumero = 0
contadorestrela = 0
contador = 0
euros = 0
vencedoreuromilhoes = 0

print("********************")
print("*   EURO MILHOES   *")
print("********************")

print("Introduza um Saldo(Min 2€):", euros)
euros = float(input())
while euros<2:
    
    print("O saldo depositado é demasiado baixo\n")
    print("Tente Introduzir um saldo mais alto:")
    euros = float(input())

os.system('cls')

print("Deseja apostar no Euro Milhões? Terá um custo de 2€(Sim/Não)")
euros = euros - 2
inicio = input()
os.system('cls')

if inicio == "Sim" or inicio == "sim" or inicio == "SIM":
    
    print("*********************")
    print("*      Numeros      *")
    print("*********************")

    while len(NumerosUser) <= 4:
        print("Insira um numero(1-50): ")
        num = int(input())
        NumerosUser.append(num)
        os.system('cls')

    print("********************")
    print("*     Estrelas     *")
    print("********************")

    while len(EstrelasUser) <= 1:
        print("Insira uma estrela(1-12): ")
        num2 = int(input())
        EstrelasUser.append(num2)
        os.system('cls')
        
    print("Os numeros escolhidos foram: " , NumerosUser)
    print("As estrelas escolhidas foram: " , EstrelasUser)
    os.system('cls')


    while(repeticao <= 100):

        numeros = []
        estrelas = []
        GanhosEstrelas = []
        GanhosNumeros = []

        repeticao = repeticao + 1

        while len (numeros) <= 4:
            NumerosAleatorios = random.randrange(1,51)

            if NumerosAleatorios not in numeros:
                numeros.append(NumerosAleatorios)

        while len (estrelas) <=1:
            EstrelasAleatorias = random.randrange(1,13)

            if EstrelasAleatorias not in estrelas:
                estrelas.append(EstrelasAleatorias)
                
        print("Os numeros sao: " , numeros)
        print("As estrelas sao: " , estrelas)

        for num in NumerosUser:
            if num in numeros:
                GanhosNumeros.append(num)

        for num2 in EstrelasUser:
            if num2 in estrelas:
                GanhosEstrelas.append(num2)
                
        if len (GanhosNumeros) > 0:
            print(f"Você acertou pelo menos: {GanhosNumeros}")
            contadornumero = contadornumero + 1
        else:
            print("Nenhum numero acertado")  
            
        if len (GanhosEstrelas) > 0:
            print(f"Você acertou pelo menos: {GanhosEstrelas}")
            contadorestrela = contadorestrela + 1
        else:
            print("Nenhuma estrela acertada")
            
        if len (GanhosEstrelas) > 0 and len (GanhosNumeros) > 0:
            contador = contador + 1
            euros = euros + 5
            
        if len (GanhosEstrelas) == 2 and len (GanhosNumeros) == 5:
            vencedoreuromilhoes = vencedoreuromilhoes + 1
            euros = euros + 100000000

    print("\nAcertou um numero" , contadornumero , "vezes")
    print("\nAcertou uma estrela" , contadorestrela , "vezes")
    print("\nAcertou um numero e uma estrela\n" , contador , "vezes")
    print("\nGANHOU O EURO MILHÕES\n" , vencedoreuromilhoes , "vezes")
    
    print("Deseja ver o seu saldo?(Sim/Nao)")
    versaldo = input()
    os.system('cls')
    
    if versaldo == "Sim" or versaldo == "sim" or versaldo == "SIM":
        print("O seu saldo é: ", euros , "€")
    else:
        print("Muito Obrigado , volte sempre")
    
else:
    print("Veio aqui só para chatear")