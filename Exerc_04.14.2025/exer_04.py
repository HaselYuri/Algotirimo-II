# 4 - 
# Crie um programa que leia números até que o usuário digite 0. 
# Armazene os números em uma lista e, ao final, mostre a soma total usando uma função. 
# A variável que armazena a lista deve ser global. 

listaNumerica = []

def inserirValor():
    valoresLista = int(input("\nInforme o valor a ser salvo na lista: "))
    listaNumerica.append(valoresLista)

def somarValores():
    soma = 0
    for valores in listaNumerica:
        soma = valores+soma

    print(f"\nA soma dos valores dentro da lista equivale a: {soma}")

valor = 1

while valor != 0:
    opcao = int(input("Deseja inserir um novo número? \n[1] - SIM\n[0] - NÃO \nResposta: "))
    if opcao == 1:
        inserirValor()
    elif opcao == 0:
        valor=0

somarValores()