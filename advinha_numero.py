import random

numero = random.randint(1,10)
resposta = ''

while(resposta != numero):
    resposta = float(input("Advinhe um número entre 1 a 10: "))
    if resposta == numero:
        print(f"Você acertou, o número é {numero}")
        break
    else:
        print("Errou tente novamente")
