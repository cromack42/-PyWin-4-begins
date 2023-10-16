media = 5

if(media >= 7.0):
    situacao = "Aprovado"

elif(media >= 5):
    situacao = "Recuperação"

else:
    situacao = "Reprovado"

print(f'O estudante está: {situacao}')
