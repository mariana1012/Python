numeros = []  # Lista para armazenar os números

while True:
    entrada = int(input("Digite um número (0 para encerrar): "))
    if entrada == 0:
        break
    numeros.append(entrada)

soma_total = sum(numeros)
print(f"A soma total dos números digitados é: {soma_total}")