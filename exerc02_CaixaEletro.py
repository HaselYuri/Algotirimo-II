#2 – Simulador de caixa eletrônico
#Crie um programa que simule um caixa eletrônico. O usuário inicia com um saldo de R$ 1000,00 e pode escolher no menu:

#1. Ver saldo
#2. Depositar dinheiro
#3. Sacar dinheiro
#4. Sair

#O programa deve garantir que:
# O saque não pode ser maior que o saldo disponível.
# O depósito deve ser um valor positivo.
# Apenas valores numéricos são aceitos.
#Utilize funções para cada operação e implemente tratamento de exceção para evitar erros. 

saldo = 1000

def verSaldo(saldo):
    print(f"\nSeu saldo é de: R${saldo}")

def depositarDinheiro(valorParaDeposito):
    global saldo
    saldo = saldo + valorParaDeposito
    print(f"\nSeu saldo é de: R${saldo}")

def sacarDinheiro(valorSacar):
    global saldo
    saldo = saldo - valorSacar
    print(f"\nSeu saldo é de: R${saldo}")
  
opcao1 = 0

while opcao1 != 1:

    print("\n\n==== CAIXA ELETRÔNICO ====")
    print("1 - VER SALDO")
    print("2 - DEPOSITAR DINHEIRO")
    print("3 - SACAR DINHEIRO")
    print("4 - SAIR")
    print("==========================")

    opcao2 = int(input("\nEscolha uma opção: "))

    while opcao2 <= 4:
        if opcao2 == 1:
            verSaldo(saldo)
            break
        elif opcao2 == 2:
            try:
                valorParaDeposito = float(input("Informe o valor para deposito: "))
                depositarDinheiro(valorParaDeposito)
                break
            except ValueError:
                print("Informe um valor válido")
            continue
                
        elif opcao2 == 3:
            try:
                valorParaSaque = float(input("Informe o valor para saque: "))
                sacarDinheiro(valorParaSaque)
                break
            except ValueError:
                print("Informe um valor válido")
            continue
        elif opcao2 == 4:
            print("Obrigado por utilizar nosso programa!")
            print("Saindo...")
            opcao1 = 1
            break