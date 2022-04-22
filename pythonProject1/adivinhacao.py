import random


#mensagem = "Tentativa " + str(tentativa) + "/5 Digite seu numero: "
#numero_secreto = round(random.random() * 100)


print("Bem vindo ao Jogo!")

numero_secreto = random.randrange(1, 101)
max_tentativas = 5
tentativa = 1
while(tentativa <= max_tentativas):


    mensagem = "Tentativa {}/{} - Digite seu numero: ".format(tentativa, max_tentativas)
    chute = int(input(mensagem))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabens, Voce Acertou!")
        break
    else:
        if(maior):
            print("Errou, o chute foi maior que o numero secreto")
        elif(menor):
            print("Errou, o chute foi menor que o numero secreto")
            print("Restam", max_tentativas - tentativa, "tentativas", sep=" ", end="!\n")
    tentativa = tentativa + 1

if not acertou:
    print("Fim da linha, o Numero Secreto era: {}".format(numero_secreto))
print("--")