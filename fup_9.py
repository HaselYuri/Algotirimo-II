vlr_idade = int(input("Informe a sua idade: "))

if(vlr_idade>0 and vlr_idade<=12):
    print('Sua classificação é infantil.')
elif(vlr_idade>=13 and vlr_idade<=17):
    print('Sua classificação é adolescente.')
elif(vlr_idade>=18):
    print('Sua classificação é adulto.')
else:
    print('Informe uma idade válida.')