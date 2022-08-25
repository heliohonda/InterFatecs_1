# variaveis de entrada
bh = list()
bh = input().split() # recebe a boca B e o calado H
g= int(input()) # recebe o grau de polinomio
fator1 = list()
fator1 = input().split() # recebe o coeficiente de cada expoente 1 até g+1
qtd_ptos = int(input()) # recebe a quantidade de pontos x da série

espcx = float(bh[0]) / (2 * (qtd_ptos - 1)) # calculo do espaçamento entre pontos
ftotal = 0 # variavel que vai multiplicar os coeficientes por cada termo no polinomio

for x in range(qtd_ptos): # laço para carregar os valores de x de cada ponto (x*espcx)
    ftotal = ftotal + float(fator1[g]) # soma o valor do último coeficiente (c0) do polinomio "fx=c4x^4+...c2x^2+c1x+c0"
    for y in range(1, g + 1): # laço para carregar os valores do expoente do maior para o menor
        if x == 0 or x == (qtd_ptos - 1): # verifica se é o primeiro ou o último ponto x da série
            ftotal = ftotal + float(fator1[y - 1]) * ((espcx * x) ** ((g + 1) - y))
        elif x% 2 == 0: # verifica se é par
            ftotal = ftotal + float(fator1[y - 1]) * 2 * ((espcx * x) ** ((g + 1) - y))
        else: # se for ímpar
            ftotal = ftotal + float(fator1[y - 1]) * 4 * ((espcx * x) ** ((g + 1) - y))

acinza = 2 * (espcx / 3) * ftotal # calculo da area cinza
ams = (float(bh[0]) * float(bh[1])) - acinza # calculo do ams
cm = ams / (float(bh[0]) * float(bh[1])) # calculo do cm
print('%.4f' % cm)  # imprime resultado final
