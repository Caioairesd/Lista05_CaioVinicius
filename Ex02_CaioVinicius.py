"""02 - Peça ao usuário para inserir um número.
Continue perguntando até que ele insira CINCO números, em seguida, exibam a mensagem
“ O último número que você digitou foi um [número] " e pare o programa."""
contador = 0
while contador <5:
    num = int(input("Insira um número:"))
    contador += 1

print("O último número que você digitou foi um {}".format(num))


print("----------------------------------------------------")
print("Programa finalizado!")
print("Caio Vinicius Aires da Silva")