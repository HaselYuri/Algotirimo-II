# 3 - 
# Crie um programa que peça a idade de várias pessoas e classifique-as como :
# "Criança" (0 a 12), 
# "Adolescente" (13 a 17), 
# "Adulto" (18 a 59)
# "Idoso" (60+). 
# 
# Use funções, if/elif/else e listas. 
# No final a saída seria assim: 

# Idade 20: Adulto 
# Idade 52: Adulto 
# Idade 15: Adolescente 
# Idade 45: Adulto 
# Idade 58: Adulto 

idadesPessoas = []

def inserirValor():
    valoresLista = int(input("\nInforme a idade a ser salvo na lista: "))
    idadesPessoas.append(valoresLista)

valor = 1

while valor != 0:
    opcao = int(input("Deseja inserir uma nova idade? \n[1] - SIM\n[0] - NÃO \nResposta: "))
    if opcao == 1:
        inserirValor()
    elif opcao == 0:
        valor=0

print("---------------------+")
for idades in idadesPessoas:
    if 0 <= idades <= 12:
        faixaEtaria = "Criança"

    elif 13 <= idades <= 17:
        faixaEtaria = "Adolescente"

    elif 18 <= idades <= 59:
        faixaEtaria = "Adulto"

    elif idades >= 60:
        faixaEtaria = "Idoso"
    print(f"Idade {idades}: {faixaEtaria}")

print("---------------------+")


