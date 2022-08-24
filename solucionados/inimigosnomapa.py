qin = int(input())
cont = 1
x = []
y = []
i = 0
ii = 0
iii = 0
iv = 0

while cont <= qin:
    coord = input().split()
    x.append(int(coord[0]))
    y.append(int(coord[1]))
    cont += 1
    
    if int(coord[0]) > 0 and int(coord[1]) > 0:
        i += 1
    elif int(coord[0]) > 0 and int(coord[1]) < 0:
        ii += 1
    elif int(coord[0]) < 0 and int(coord[1]) < 0:
        iii += 1
    elif int(coord[0]) < 0 and int(coord[1]) > 0:
        iv += 1

print('I = %d' % i)
print('II = %d' % ii)
print('III = %d' % iii)
print('IV = %d' % iv)
