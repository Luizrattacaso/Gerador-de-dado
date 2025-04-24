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
def principal(lista,soma,dados):
     vezes = int(input("Digite quantos dados você quer sortear: "))
     for x in range(vezes): 
          lista.append(randint(1 , 6))
          soma += lista[x]
     print()

     print(f"Os valores dos dados foram: {lista}\n")

     for linha in range(5):
          for i in lista:
               print(dados.get(i)[linha], end = "")
          print()

     print(f"\nO somatório dos valores é igual a {soma} ")

if __name__ == "__main__":
     principal(lista,soma,dados)