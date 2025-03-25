#3- Crie um programa que solicite ao usuário uma frase e conte quantas vogais
#(A, E, I, O, U) existem nela. O programa deve:

#1. Solicitar ao usuário que digite uma frase ou palavra.
#2. Contar e exibir o número total de vogais na frase.
#3. Permitir que o usuário escolha entre executar novamente ou sair.
#4. Ignorar maiúsculas e minúsculas (ou seja, "A" e "a" contam da mesma forma).
#5. Utilizar funções e incluir tratamento de exceção. 

def checarVogais(frase):
    vogais = "aeiouAEIOUãõÃÕáÁÚúÍíÚúÓó"
    totalVogal = 0

    for i in frase:
        if i in vogais:
            totalVogal += 1
    print(f"A um total de {totalVogal} de vogais na frase.")


opcao1 = 0

while opcao1 != 1:

    print("\n\n====== CONTADOR DE VOGAIS ======")
    print("1 - CONTAR VOGAIS EM UMA FRASE")
    print("2 - SAIR")
    print("================================")
    
    opcao2 = int(input("\nEscolha uma opção: "))

    while opcao2 <= 2:
        if opcao2 == 1:
            try:
                frase = input("\nInforme a frase para checagem: ")
                checarVogais(frase)
            
                opcao3 = int(input("\nDeseja checar mais alguma frase?\n01-SIM\n02-NÃO\nInforme aqui: "))
                
                if opcao3==1:
                    continue
                
                elif opcao3==2:
                    print("\nObrigado por utilizar nosso programa!")
                    print("Saindo...")
                    opcao1=1
                    break
            except NameError:
                print("Informe um texto válido")
            continue
        
        elif opcao2 == 2:
            print("\nObrigado por utilizar nosso programa!")
            print("Saindo...")
            opcao1=1
            break
            