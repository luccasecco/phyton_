# pylint: disable=C0103

print('Jogo do adivinhe o número')

palpite = 0
numero = 9

while True:
    palpite = int(input("Qual seu palpite?: "))
    if palpite == numero:
        print("Parabens! Voce acertou :)")
        break
    print("Voce errou... tente novamente")
