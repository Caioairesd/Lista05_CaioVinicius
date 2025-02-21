"""07 - Escreva um programa que permaneça em laço lendo números inteiros. 
O laço termina quando for digitado 0 (zero).
Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que ele ainda não esteja lá, ou seja, valores repetidos não são aceitos. 
Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela. 
Ao final exiba a lista e a quantidade de elementos que ela contém"""
lista = []
valor = 1

while valor != 0:
    try:
        valor = int(input("Insira um valor:"))

        if valor in lista:
            lista.append(valor)
            i = lista.index(valor)
            lista.pop(i)
            print("Valor repetido!")

        elif valor != 0:
            lista.append(valor)
    except:
        print("Valor inválido!")   


print(lista)
print("----------------------------------------------------")
print("Programa finalizado!")
print("Caio Vinicius Aires da Silva") 


