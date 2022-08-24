num_aluno = int(input())
cont = 1
linhas = 1
bom_trab = True

while linhas <= num_aluno:
    recit = int(input())
    if recit != cont:
        bom_trab = False
        for i in range(cont, recit):
            print(i)
        cont = recit + 1
    else:
        linhas += 1
        cont += 1
        continue
    linhas += 1
if bom_trab:
    print('bom trabalho')
