"""04 - Faça um programa que peça o nome do convidado que o usuario deseja convidar para uma festa.
Depois disso, exiba a mensagem "[nome] foi adicionado(a) com sucesso no convite!" e adicione 1 à contagem.
Em seguida, pergunte se ele quer convidar outra pessoa.
Continue repetindo isso até que ele não queira mais convidar ninguém para a festa e, em seguida, mostre quantas pessoas foram convidas para a festa."""
contador = 0
decisao = True

while decisao == True:
    convidado = input("Insira o nome do convidado: ") 
    print("{} foi adicionado(a) com sucesso no convite!".format(convidado))

    contador += 1

    decisao = input("Você deseja adiconar mais convidados?\nS/s para sim ou N/n para Não: ").lower()
    if decisao != 's':
        decisao = False
    else: 
        decisao = True
        

print("Você covidou {} pessoas".format(contador))
print("----------------------------------------------------")
print("Programa finalizado!")
print("Caio Vinicius Aires da Silva")