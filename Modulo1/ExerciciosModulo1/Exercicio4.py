soma = 0
quantidadeNumeros = int(
    (input("Digite a quantidade de números a serem somados:")))
for indice in range(quantidadeNumeros):
    numeros = int((input("Digite um número para ser somado: ")))
    soma = soma + numeros

print("O resultado da soma é:", soma)
