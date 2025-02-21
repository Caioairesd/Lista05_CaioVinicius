"""03 - Peça ao usuário para inserir um número e, em seguida, insira outro número. Some esses dois números e pergunte se ele quer adicionar outro número.
Se ele digitar “ s ", diga para inserir outro número e continuar adicionando números e somando até que ele não respondam “ s ".
Depois que o loop for interrompido, exiba o total."""

resposta = 's'

try:
    num1 = int(input("Insira um número: "))
    num2 = int(input("Insira outro número: "))
    soma = num1 + num2

    while resposta == 's':
  
        resposta = input("Você deseja adiconar mais um número?\nS/s para sim ou N/n para Não: ").lower()
        if resposta == 's':
            num3 = int(input("Insira mais um valor: "))
            soma += num3


    print("A soma total é: {}".format(soma)) 
    print("----------------------------------------------------")
    print("Programa finalizado!")
    print("Caio Vinicius Aires da Silva")
    
except:
    print("Valor inserido inválido!")