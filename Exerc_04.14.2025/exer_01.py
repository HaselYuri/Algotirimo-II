# 1- 
# Crie um programa que solicite ao usuário digitar números e armazene-os em uma lista. 
# Pode ser 5 números. 
# Deverá estar em uma função, depois, crie uma função que pergunte ao usuário qual número deseja procurar 
# e diga se ele está ou não na lista. 
# 
# Use if e else. 
listaNumerica = []

def inserirValor():
    valoresLista = int(input("\nInforme o valor a ser salvo na lista: "))
    listaNumerica.append(valoresLista)

def procurarValor():
    valorProcura = int(input("\nInforme o valor a ser procurado: "))
    if valorProcura in listaNumerica:
        print(f"O valor {valorProcura} está na lista!")
    else:
        print("Não está na lista.")

valor = 1

while valor != 0:
    opcao = int(input("Deseja inserir um novo número? \n[1] - SIM\n[0] - NÃO \nResposta: "))
    if opcao == 1:
        inserirValor()
    elif opcao == 0:
        valor=0

pergunta = int(input("Deseja procurar algum valor na lista?\n[1] - SIM\n[0] - NÃO\nResposta: "))
if pergunta == 1:
    procurarValor()
else:
    print("\nPrograma encerrado!")




