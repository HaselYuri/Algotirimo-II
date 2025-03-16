n1 = float(input("Informe o 1° número: "))
n2 = float(input("Informe o 2° número: "))
n3 = float(input("Informe o 3° número: "))

if(n1>n2 and n1>n3):
    print('O 1° valor é o maior.')
elif(n2>n1 and n2>n3):
    print('O 2° valor é o maior.')
elif(n3>n1 and n3>n2):
    print('O 3° valor é o maior.')
else:
    print('Os valores são iguais.')