contatos = []


#Função adicionar contato
def adicionar_contato(lista, nome):
    try:
        
        if not nome.strip():  # verifica se é vazio
            raise ValueError("O nome do contato não pode ser vazio.")
        lista.append(nome)
        print(f' Contato "{nome}" adicionado com sucesso!')
    except ValueError as e:
        print(f" Erro: {e}")


# Função para remover contato
def remover_contato(lista, nome):
    try:
        lista.remove(nome)  # remove se existir
        print(f' Contato "{nome}" removido com sucesso!')
    except ValueError:
        print(f" Erro: O contato '{nome}' não existe na lista.")

# Função para buscar contato
def buscar_contato(lista, nome):
    try:
        posicao = lista.index(nome)  # pega posição na lista
        print(f' Contato "{nome}" encontrado na posição {posicao + 1}.')
    except ValueError:
        print(f" Erro: O contato '{nome}' não existe na lista.")

# Função para mostrar todos os contatos
def mostrar_contatos(lista):
    if lista == 0:
        print(" Nenhum contato cadastrado.")
    else:
        print("\n=== Lista de Contatos ===")
        for i, contato in enumerate(lista, start=1):
            print(f"{i}. {contato}")

while True:
    print("------Menu-----")
    print("1. Adicionar contato ")
    print("2. Remover contato")
    print("3. Buscar contato")
    print("4. Mostrar contatos")
    print("5. Sair ")
    opcao = input('Qual ação gostaria de executar?? ')

    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        adicionar_contato(contatos, nome)
    elif opcao == "2":
        nome = input("Digite o nome do contato a remover: ")
        remover_contato(contatos, nome)
    elif opcao == "3":
        nome = input("Digite o nome do contato a buscar: ")
        buscar_contato(contatos, nome)
    elif opcao == "4":
        mostrar_contatos(contatos)
    elif opcao == "5":
        print(" Saindo do programa...")
        break
    else:
        print(" Opção inválida, tente novamente.")