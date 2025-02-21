"""06 - Peça ao usuário para inserir um número entre 15 e 20.
Se ele inserir um valor abaixo de 15, exiba a mensagem "Muito baixo" e peça que tentem novamente.
Se ele inserir um valor acima de 20, exiba a mensagem "Muito alto" e peça que tentem novamente.
Continue repetindo isso até que ele insira um valor entre 15 e 20 e, em seguida, exibam a mensagem "Obrigado"."""

valor = False
try:


    while valor == False:

        valor = int(input("Insira um valor entre 15 e 20: "))

        if valor < 15:
            print("Valor muito baixo! Tente novamente.")
            valor = False
        elif valor > 15:
            print("Valor muito alto! Tente novamente.")
            valor = False
        else:
            valor = True
            
            print("Obrigado!")
            print("----------------------------------------------------")
            print("Programa finalizado!")
            print("Caio Vinicius Aires da Silva")   
except:
    print("Valor inserido é inválido!")
