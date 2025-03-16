vlr_carrinho = float(input("Informe o valor da sua compra: "))

if(vlr_carrinho>100):
    print('Você desbloqueou um desconto adicional de 10% em cima da sua compra.')
    vlr_carrinho_desconto = vlr_carrinho*0.9
    print('Valor final de R$',vlr_carrinho_desconto,'.')
else:
    print('Valor final de R$',vlr_carrinho,'.')