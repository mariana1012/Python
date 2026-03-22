## Exercícicios para Revisão

# 1) A saída será: 1,2,3,4,5

# 2) A saída será: 5 pois se inicia a contagem no 0

# 3) A lista é mutavél, podem adicionar elementos, ou retira-los. Já na Tupla, ela seria imutável, nçao podendo realizar alterações em seu conteúdo.

# 4) Irá printar o número 20, pois inicia em 0 a contagem em python.


# 5) -- Dicionário de Notas ---
notas = {
    "Ana": 8.5,
    "Bruno": 6.0,
    "Carlos": 9.0
}
print("Nota do Bruno")
print(notas["Bruno"]) # Para puxar a informação:


#6) Dicionário  --- Cidades
dicionario_cidades = {
    "RS":["Gravatai", "Pelotas","Erechim"],
    "SC":["Joinville", "Jaraguá","Blumenau"],
    "PR":["Curitiba", "Toledo","Maringá"]
}
print(dicionario_cidades)


# 7) Imprimindo cidade de joinville
print(dicionario_cidades["SC"][0])


# 8) --- Armazenar nomes ----
lista_nomes = []


def adicionar_nomes(lista_nomes,nomes):
    lista_nomes.append(nomes)
    print(f'✅"{nomes}" adicionado com sucesso!')

for i in range(5):
    nomes = input("Digite um nome: ")
    adicionar_nomes(lista_nomes,nomes)

print(lista_nomes)

tupla_nomes = tuple(lista_nomes)
print(tupla_nomes)



# 9) --- Menu para concontrole de nomes  ----
lista = []

def adicionar_nomes(lista,nomes):
    lista.append(nomes)
    print(f'✅"{nomes}" adicionado com sucesso!')

def remover_nomes(lista,nomes):
    try:
        lista_nomes.remove(nomes)
    except ValueError:
        print("⚠️ Nome inválido! Digite um nome presente na lista.")

def alterar_nomes(lista,nomes,novo_nome):
    try:
        for p in lista:
            if p["nome"] == nomes:
                if not novo_nome.strip():
                    raise ValueError("O nome não pode ser vazio.")
                p["nome"] = novo_nome
                print(f'🔄 Nome {nomes} alterado com sucesso!')
                return
        # Se não encontrar o nome
        raise LookupError(f"Nenhum nome encontrado {nomes}.")
    except ValueError as e:
        print(f"⚠️ Erro: {e}")
    except LookupError as e:
        print(f"⚠️ Erro: {e}")

def mostrar_nomes(lista):
    if not lista:
        print("📭 Nenhum nome cadastrado.")
    else:
        print("Lista de nomes")
        for nomes in lista:
            print(f'Nome: {nomes}')

while True:
    print("""
===== MENU =====
1 - Adicionar nome
2 - Remover nome
3 - Alterar nome
4 - mostrar listas de nomes
5 - Sair
""")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome para adiciona-lo: ")
        adicionar_nomes(lista, nomes)

    elif opcao == "2":
         nome = input("Digite o nome do contato a remover: ")
         remover_nomes(lista, nomes)

    elif opcao == "3":
        try:
            nome_desejado = int(input("Digite nome desejado a alterar: "))
            novo_nome = input("Digite o novo nome: ")
            novo_preco = input("Digite o novo preço: ")
            alterar_nomes(lista, novo_nome)
        except ValueError:
            print("⚠️ Nome inválido! Digite um nome válido.")

    elif opcao == "4":
        mostrar_nomes(nomes)

    elif opcao == "5":
        print("👋 Saindo do programa...")
        break

    else:
        print("⚠️ Opção inválida, tente novamente.")