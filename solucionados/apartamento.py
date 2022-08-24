invest = float(input())
val_apart = float(input())
juros = float(input())
tot_meses = 0
valor_atual = invest

while valor_atual <= val_apart:
    valor_atual += valor_atual * (juros / 100)
    tot_meses += 1

if invest >= val_apart:
    print('pode comprar agora')
elif tot_meses == 1:
    print('possivel em %d mes' % tot_meses)
elif tot_meses < 0:
    print('pode comprar agora')
else:
    print('possivel em %d meses' % tot_meses)
