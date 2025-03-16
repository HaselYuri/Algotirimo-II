from random import randint

adivinhar = randint(1, 100)
#print(adivinhar)

while True: 
    vlr = int(input("Adivinhe o valor: "))
    
    if vlr < adivinhar:
        print('Mais pra cima')
    elif vlr > adivinhar:
        print('Mais pra baixo')
    else: 
        print("Acertou!")
        break  
