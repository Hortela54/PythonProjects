import random

def jogar():
    
    print("###############################")
    print("Bem vindo ao jogo de advinhação")
    print("###############################")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 3
    pontos = 100

    print("Qual nível de dificuldade?")
    print("(1) Facíl (2) Médio (3) Difícil")

    nivel = int(input("Define o nível"))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel ==2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}". format(rodada,total_tentativas))
        chute = int(input("Digite um número entre 1 e 100 numero: "))
        
        acertou = chute == numero_secreto
        maior = chute >= numero_secreto
        menor = chute <= numero_secreto
        
        if(chute<1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if(acertou):
            print("Você acertou e fez {} pontos".format(pontos))
        else:
            if(maior):
                print("Você errou, bobão cara de mamão, um numero maior que o numero secreto")
            elif(menor):
                print("Você errou, bobão cara de mamão, um numero menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim do jogo")
