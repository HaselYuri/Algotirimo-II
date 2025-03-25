#1 - Crie um programa em Python que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
#O usuário deverá informar seu peso (kg) e altura (m). 
#O programa deve calcular o IMC utilizando a fórmula:

#IMC = peso / (altura **2)

def calcIMC(peso,altura):
    imc = peso / (altura**2)
    print(f"O IMC é: {imc}")
 
opcao1 = 0

while opcao1 != 1:
  
    print("\n=== CALCULADORA DE IMC ===")
    print("1 - CALCULAR IMC")
    print("2 - SAIR")
    print("==========================")

    opcao2 = int(input("\nEscolha uma opção: "))

    while opcao2 <= 2:
        if opcao2 == 1:
            try:
                peso = float(input("\nInforme o peso: "))
                altura = float(input("Informe a altura: "))
                calcIMC(peso,altura)
                break
            except ValueError:
                print("Informe um valor válido")
            continue
      
        elif opcao2 == 2:
            print("Obrigado por utilizar nosso programa!")
            print("Saindo...")
            opcao1 = 1
            break