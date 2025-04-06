def AddCadastroAgenda():
  while True:
    try:
      nome = input("\nDigite o seu Nome: ").strip()
    except ValueError:
      print("Por favor, digite apenas letras.")
      continue
    break

  while True:
    try:
        telefone = int(input("Digite o seu Telefone: "))
    except ValueError:
        print("Por favor, digite apenas números.")
        continue
    existe = False
  
    for i in agenda:
        if i["telefone"] == telefone:
            print("\nTelefone já existente. \nTente outro!\n")
            existe = True
            break

    if not existe:
        break

  agenda.append({
      "nome": nome if nome else None,
      "telefone": telefone if telefone else None
  })  

def RemoveCadastroAgenda():
  try:
    telefone = int(input("\nDigite o telefone a ser removida: "))
  except ValueError:
    print("Por favor, digite um número válido.")
    return

  for i in agenda:
    if i["telefone"] == telefone:
        agenda.remove(i)
        print(f"Telefone {telefone} removido com sucesso.")
        return

  print("Nr telefone não existente.")

def ListCadastroLista():
  print("\n--- Lista ---")
  if not agenda:
      print("Nenhum cadastro registrado.")
      return

  for i, item in enumerate(agenda, start=1):
      nome = item['nome'] if item['nome'] else "-"
      telefone = item['telefone'] if item['telefone'] else "-"
      print(f"{i}° - {nome} | {telefone}")

opcao = -1
agenda = []
while opcao != 0:
  print("\n-------------------")
  print("Escolha uma opção:")
  print("1. Adicionar")
  print("2. Remover")
  print("3. Listar")
  print("0. Sair")
  print("-------------------\n")

  opcao = int(input("Opção: "))

  if opcao == 1:
      AddCadastroAgenda()

  elif opcao == 2:
      RemoveCadastroAgenda()

  elif opcao == 3:
      ListCadastroLista()

  elif opcao == 0:
      print("Saindo...")

  else:
      print("Opção inválida.\nTente novamente...")