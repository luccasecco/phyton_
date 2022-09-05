# pylint: disable=C0103

print("Par ou impar?")

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O numero {numero} eh par")
else:
    print(f"O numero {numero} eh impar")
