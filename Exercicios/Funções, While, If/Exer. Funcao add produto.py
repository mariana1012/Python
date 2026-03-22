produtos = []

# Função para adicionar produto
def adicionar_produto(lista, nome, preco):
    try:
        if not nome.strip():  # Verifica nome vazio
            raise ValueError("O nome do produto não pode ser vazio.")
        
        preco = float(preco)  # Converte para número (pode gerar erro)
        novo_id = len(lista) + 1
        produto = {"id": novo_id, "nome": nome, "preco": preco}
        lista.append(produto)
        print(f'✅ Produto "{nome}" adicionado com sucesso!')
    except ValueError as e:
        print(f"⚠️ Erro: {e}")

# Função para mostrar produtos
def mostrar_produtos(lista):
    if not lista:
        print("📭 Nenhum produto cadastrado.")
    else:
        print("\n=== Lista de Produtos ===")
        for p in lista:
            print(f'ID: {p["id"]} | Nome: {p["nome"]} | Preço: R$ {p["preco"]:.2f}')

# Função para alterar produto
def alterar_produto(lista, id_produto, novo_nome, novo_preco):
    try:
        for p in lista:
            if p["id"] == id_produto:
                if not novo_nome.strip():
                    raise ValueError("O nome do produto não pode ser vazio.")
                novo_preco = float(novo_preco)  # Converte para número
                p["nome"] = novo_nome
                p["preco"] = novo_preco
                print(f'🔄 Produto ID {id_produto} alterado com sucesso!')
                return
        # Se não encontrar o produto
        raise LookupError(f"Nenhum produto encontrado com ID {id_produto}.")
    except ValueError as e:
        print(f" Erro: {e}")
    except LookupError as e:
        print(f" Erro: {e}")

# Programa principal (menu)
while True:
    print("""
===== MENU =====
1 - Adicionar produto
2 - Mostrar produtos
3 - Alterar produto
4 - Sair
""")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        preco = input("Digite o preço do produto: ")
        adicionar_produto(produtos, nome, preco)

    elif opcao == "2":
        mostrar_produtos(produtos)

    elif opcao == "3":
        try:
            id_produto = int(input("Digite o ID do produto a alterar: "))
            novo_nome = input("Digite o novo nome: ")
            novo_preco = input("Digite o novo preço: ")
            alterar_produto(produtos, id_produto, novo_nome, novo_preco)
        except ValueError:
            print("⚠️ ID inválido! Digite um número inteiro.")

    elif opcao == "4":
        print("👋 Saindo do programa...")
        break

    else:
        print("⚠️ Opção inválida, tente novamente.")