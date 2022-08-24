import string

codigo = input() # mensagem codificada
chave = input() # chave para decodificação
opers = list() # lista que armazena os numeros da decodificação
letras = list(string.ascii_lowercase) # lista de todos caracteres minusculos para indexação
soma = True
nova_str = '' # string de retorno
cont = 0 # contador para navegar pela chave

for x in chave: # navega pela chave
    if x == '+': # se encontra um +, salva cada digito em int positivo
        soma = True
    elif x == '-': # se encontra um -, salva cada digito em int negativo
        soma = False
    else:
        if soma:
            n = int(x)
            opers.append(n)
        else:
            n = - int(x)
            opers.append(n)

for letra in codigo: # navega pela mensagem codificada
    if letra == 'w': # se encontra w, insere espaço em branco
        nova_str += ' '
    else:
        x = letras.index(letra) # recebe o valor numerico da letra na lista de chars
        if x + opers[cont] > 25:
            """
            x = valor numero da letra
            opers[cont] = posição a ser lida na chave de decodificação
            se a soma de x e opers[cont] for > 25 (indice final da lista),
            a contagem deve retornar a 0 (letra 'a') e encontrar a letra no
            indice remanescente
            """
            dif = (x + opers[cont]) - 25
            nova_str += letras[dif - 1]
            print(f'Letra lida: {letra} : Local de {letra} no alfabeto: {x} : Oper.: {opers[cont]} Pos. nova letra: {dif} : Nova letra: {letras[dif - 1]}')
        else:
            """
            se o valor calculado não ultrapassar o limite da lista de caracteres,
            inserir o caracter encontrado na string
            """
            nova_str += letras[(x) + opers[cont]]
            print(f'Letra lida: {letra} : Local de {letra} no alfabeto: {x} : Oper.: {opers[cont]} Pos. nova letra: {x + opers[cont]} : Nova letra: {letras[(x) + opers[cont]]}')
        cont += 1 # contador so avanca se o numero da chave foi lido e calculado
print(nova_str)
