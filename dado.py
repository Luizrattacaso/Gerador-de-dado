from random import randint

lista = []
soma = 0 

dados = {
    1 : ("╔-------╗",
         "|       |",
         "|   •   |",
         "|       |",
         "╚-------╝"),

    2 : ("╔-------╗",
         "|  •    |",
         "|       |",
         "|    •  |",
         "╚-------╝"),

    3 : ("╔-------╗",
         "|  •    |",
         "|   •   |",
         "|    •  |",
         "╚-------╝"),
         
    4 : ("╔-------╗",
         "| •   • |",
         "|       |",
         "| •   • |",
         "╚-------╝"),

    5 : ("╔-------╗",
         "| •   • |",
         "|   •   |",
         "| •   • |",
         "╚-------╝"),

    6 : ("╔-------╗",
         "| •   • |",
         "| •   • |",
         "| •   • |",
         "╚-------╝"),
}

vezes = int(input("Digite quantos dados você quer sortear: "))

for x in range(vezes): 
    d = randint(1 , 6)
    lista.append(d)
    soma += d
print()

print(f"Os valores dos dados foram: {lista}\n")

for linha in range(5):
    for i in lista:
        print(dados.get(i)[linha], end = "")
    print()

print(f"\nO somatório dos valores é igual a {soma} ")