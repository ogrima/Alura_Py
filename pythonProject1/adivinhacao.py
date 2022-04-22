print("Bem vindo ao Jogo!")

numero_secreto = 42

chute = int(input("Digite seu numero: "))

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if(acertou):
    print("Voce Acertou!")
else:
    if(maior):
        print("Errou, o chute foi maior que o numero secreto")
    elif(menor):
        print("Errou, o chute foi menor que o numero secreto")
