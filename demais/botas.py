botas = list() # total de todos os pés a serem contados
qtd = int(input()) # quantidade de pés que serão inseridos
cont_pares = 0 # total de pares
pes_possiveis = list() # lista que armazena cada variação de pé que é inserida
pares = list() # lista que armazena os pares possiveis a partir da lista acima

# inserção dos pés
for i in range(qtd):
    inp = input()
    botas.append(inp.upper()) # uppercase para evitar problemas de duplicação indevida
    if inp not in pes_possiveis: # armazena cada pé/tamanho que ainda não foi computado
        pes_possiveis.append(inp.upper())

pes_possiveis.sort() # ordena a lista de pés possiveis para registrar os pés

# itera sobre a lista de pés possiveis e retorna tuplas dos pares que existem
for i, e in enumerate(pes_possiveis):
    if (i + 1 < len(pes_possiveis)):
        if pes_possiveis[i][0:2] == pes_possiveis[i+1][0:2] and pes_possiveis[i] != pes_possiveis[i+1]:
            pares.append((pes_possiveis[i], pes_possiveis[i+1]))
print('\nPares possíveis:')
for x, y in pares:
    print(f'{x}, {y}')

# navega as tuplas de pares e calcula a quantidade de cada pé para contabilizar
# quais deles formam pares
print('\nCalculando pares...\n')
for (x, y) in pares:
    ld1 = botas.count(x)
    ld2 = botas.count(y)
    print(f'{x}: {ld1}, {y}: {ld2}')
    if ld1 == ld2:
        cont_pares += ld1
    elif ld1 > ld2:
        cont_pares += ld2
    else:
        cont_pares += ld1

print(f'Num de pares: {cont_pares}') 
