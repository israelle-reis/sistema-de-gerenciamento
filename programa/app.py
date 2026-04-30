# Lógica: o usuário vai informar o nome, a quantidade e o preço. Após isso calcula se o produto está disponivel

print("SISTEMA DE GERENCIAMENTO DE PRODUTOS")

# Entrada 
nome = str(input("Digite o nome do produto: "))
quantidade = int(input("Digite a quantidade: "))
preco =float(input("Digite o preço: "))

# Processamento
disponivel = quantidade > 0
# Menu 
print("\nEscolha uma opção:") # \n faz a quebra de texto.
print("1 - Visualizar dados do produto")
print("2 - Visualizar valor total do estoque")
print("3 - Aplicar desconto")
print("4 - Ver se o estoque é suficiente")
print("5 - Atualizar quantidade")

opcao = input("Opção: ")

match opcao:
      case "1": 
        print("\n INFORMAÇÕES ")
        print("Nome:", nome)
        print("Quantidade:", quantidade)
        print("Preço:", preco)
        
        if disponivel:
            print("Status: Disponível")
        else:
            print("Status: Indisponível")
      case "2":
        total = quantidade * preco
        print("\nValor total em estoque:", total)
      case "3":
        desconto = float(input("Digite o percentual de desconto: "))
        novo_preco = preco - (preco * desconto / 100)
        print("Preço com desconto: ", novo_preco)
      case "4":
        minimo = int(input("Digite a quantidade mínima ideal: "))

        if quantidade >= minimo:
           print("Estoque suficiente")
        else: 
           print("Estoque baixo! Repor produto.")

      case "5":
        print("Estoque atual ", quantidade)
        nova_quantidade = int(input("Digite a nova quantidade:"))
        quantidade = nova_quantidade

        if quantidade > 0:
           disponivel = True
        else:
           disponivel = False
        
        print("Quantidade atualizada!")

      case _:
        print("Opção inválida!")