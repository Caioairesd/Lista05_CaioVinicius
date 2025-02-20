"""01 - Faça um programa que leia os números digitados pelo usuario,
a cada número digitado ele deve ser somado ao anterior digitado e a cada soma exibida na tela,
quando a soma for superior a 50 deve exibir a mensagem “ O total é... [total] ” e parar o programa."""
total = 0
while total <= 50:
    num =  int(input("Insira um valor:"))
    total += num
   
   
print("O total é: {}".format(total))
print("")

print("----------------------------------------------------")
print("Programa finalizado!")
print("Caio Vinicius Aires da Silva")