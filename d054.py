# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - nasc
    print(f'Essa pessoa tem {idade} anos.')
    if idade >= 18:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print(f'Ao todo, tivemos {totmaior} pessoas maiores de idade.')
print(f'E também tivemos {totmenor} pessoas menores de idade.')
