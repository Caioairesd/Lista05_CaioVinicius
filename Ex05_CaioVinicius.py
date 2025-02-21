"""05 - Crie uma variável chamada “adivinha” e defina o valor como 50. 
Peça ao usuário para inserir um número.
Embora o palpite não seja o mesmo que o valor do “adivinha”, diga a ele se o palpite é muito baixo ou muito alto e peça que ele dê outro palpite. 
Se ele inserir o mesmo valor que “adivinha”, exiba a mensagem "Parabéns! Você acertou o número em {} tentativas!"."""
contador = 0
advinha = False

while advinha == False:
    
    contador += 1
    try:

        resposta = int(input("Tente advinhar o valor de um número real:"))
    
        if resposta == 50:
            print("Parabéns! Você acertou o número em {} tentativas!".format(contador))
            advinha = True
        elif resposta > 50:
            print("Valor muito alto tente novamente!")
        elif resposta < 50:
            print("Valor muito baixo tente novamente!")
    except:
        print("Valor inserido é inválido!")

print("----------------------------------------------------")
print("Programa finalizado!")
print("Caio Vinicius Aires da Silva")