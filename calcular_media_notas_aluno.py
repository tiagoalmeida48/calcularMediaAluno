notas = float(input('Digite uma nota do aluno: '))
lista_notas = []

while notas != -1:
    lista_notas.append(notas)
    notas = float(input('Digite uma nota do aluno: '))

print(f'A lista possui {len(lista_notas)} quantidades')
print(' '.join([str(nota) for nota in lista_notas]))

lista_notas.reverse()
for i in lista_notas:
    print(i)

print(f'A soma dos valores é: {sum(lista_notas)}')
media = sum(lista_notas) / len(lista_notas)
print(f'A media dos valores é {media}')

media_calculada_acima = valor_abaixo_7 = []

for i in lista_notas:
    if i > media:
        media_calculada_acima.append(i)
    if i < 7:
        valor_abaixo_7.append(i)

print(f'Quantidade de valores acima da media é:')
print(' '.join([str(nota) for nota in lista_notas if nota > media]))
print(f'Quantidade de valores abaixo de 7 é:')
print(' '.join([str(nota) for nota in lista_notas if nota < 7]))

print('Final do calculo das notas do aluno')