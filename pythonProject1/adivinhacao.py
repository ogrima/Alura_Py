print("Bem vindo ao Jogo!")

numero_secreto = 42
max_tentativas = 5
tentativa = 1
while(tentativa <= max_tentativas):
    mensagem = "Tentativa " + str(tentativa) + "/5 Digite seu numero: "
    chute = int(input(mensagem))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Voce Acertou!")
        break
    else:
        if(maior):
            print("Errou, o chute foi maior que o numero secreto")
        elif(menor):
            print("Errou, o chute foi menor que o numero secreto")
    tentativa = tentativa + 1

print("Fim da Linha")