from datetime import date
 
opcao = excluir= 0
 
opcao_dos_produtos = ""
 
certeza = certeza_02 = ""
 
nome_dos_produtos = []
 
data_dos_produtos = []
 
 
print(30 * "-")
print(f"{'VALIDAÇÃO DATA DE PRODUTOS':^30}")
print(30 * "-")
 
while opcao != 6:
    print("\n1ª opção adicionar novo produto")
    print("2ª opção verificar se produto venceu")
    print("3ª opção ver produtos adicionados")
    print("4ª opção remover último produto adicionado")
    print("5ª opção para remover um produto por posição")
    print("6ª opção sair do programa")
   
    opcao = int(input("Digite alguma opção válida: "))
 
    if opcao == 1:
        print("\n" + 30 * "-")
        print(f"{'Área de Adicionar produtos':^30}")
        print(30 * "-")
        while True:
            nome_dos_produtos.append(str(input("\nDigite o nome do seu produto: ")))
            data_dos_produtos.append(int(input("Digite a data do ano do produto (xxxx):")))
 
            print("\n" + 30 * "-")
            print("\033[32mPRODUTO ADICIONADO COM SUCESSO!!\033[m")
            print(f"\nProduto: {nome_dos_produtos} data: {data_dos_produtos}")
            print(30 * "-")
 
            opcao_dos_produtos = str(input("\nQuer continuar adicionando produtos?[S/N] ")).strip().upper()[0]
 
            if opcao_dos_produtos not in ["S","N"]:
                print(f"Opção {opcao_dos_produtos} inválida")
                print("Digite [S/N]")
 
                opcao_dos_produtos = str(input("\nQuer continuar adicionando produtos?[S/N] ")).strip().upper()[0]
 
                if opcao_dos_produtos not in ["S", "N"]:
                    print("Você digitou uma opção inválida encerrando, Voltando ao menu")
                    break
 
            if opcao_dos_produtos == "N":
                break
 
    elif opcao == 2:
        print("\n" + 30 * "-")
        print(f"{'Área De Vencimentos':^30}")
        print(30 * "-")        
        for posicao,valor in enumerate(data_dos_produtos):
            if valor < date.today().year:
                print(f"\n\033[31mO produto {nome_dos_produtos[posicao]} está vencido a {date.today().year - valor} anos\033[m")
   
    elif opcao == 3:
        print(f"\nOs produtos adicionados até agora foram {nome_dos_produtos} com a data {data_dos_produtos}")
 
    elif opcao == 4:
        print("\nVocê clicou para excluir o último item da sua lista")
        certeza = str(input("Você tem certeza que quer excluír o último item? [S/N]")).strip().upper()[0]
 
        if certeza == "S":
            nome_dos_produtos.pop()
            data_dos_produtos.pop()
            print("\n\033[32mPRODUTO REMOVIDO COM SUCESSO\033[m")
        elif certeza == "N":
            print("\nVoltando para o menu")
        else:
            print("Opção inválida tente novamente")
            continue
 
    elif opcao == 5:
        print("\nVocê clicou para excluir um item na posição desejada da sua lista")
        certeza_02 = str(input("Você tem certeza que quer excluír? [S/N]")).strip().upper()[0]
 
        if certeza_02 == "S":
            for a,b in enumerate(nome_dos_produtos):          
                print(f"\nPosição: {a + 1}ª produto {b} data {data_dos_produtos[a]}")
            excluir = int(input("Digite o número da posição mostrada: "))
 
            nome_dos_produtos.pop(excluir - 1)
            data_dos_produtos.pop(excluir - 1)
 
            print("\n\033[32mPRODUTO REMOVIDO COM SUCESSO\033[m")
        elif certeza == "N":
            print("\nVoltando para o menu")
        else:
            print("Opção inválida tente novamente")
            continue  
 
    else:
        print("OPÇÃO")  