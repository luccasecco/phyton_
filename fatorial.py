# pylint: disable=C0103

print("Fatorial...!")

fatorial = 1
numero = int(input("Digite um numero e descubra seu valor fatorial: "))

if numero < 0:
    print("Nao existe fatorial de numeros negativos")
elif numero == 0:
    print(f"O fatorial de {numero} eh 1")
else:
    for i in range(1, numero + 1):
        fatorial = fatorial * i


print(30 * '-')
print(f"O fatorial de {numero} eh => {fatorial}")
