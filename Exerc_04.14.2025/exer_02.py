# 2 - 
# Crie uma função que receba uma lista de números como parâmetro e retorne o maior número da lista. 
# No final mostrar qual o maior número da lista.
# Podem ser 5 números. 
# Use uma estrutura de repetição para percorrer os elementos 

listaNumerica = []

def inserirValor():
    valoresLista = int(input("\nInforme o valor a ser salvo na lista: "))
    listaNumerica.append(valoresLista)

def checarMaiorValor():
    print("\n----Lista----")
    print(listaNumerica)
    print(f"O maior valor de dentro da lista é: {max(listaNumerica)}")
    print("\n-------------")

valor = 1

while valor != 0:
    opcao = int(input("Deseja inserir um novo número? \n[1] - SIM\n[0] - NÃO \nResposta: "))
    if opcao == 1:
        inserirValor()
    elif opcao == 0:
        valor=0
    
checarMaiorValor()