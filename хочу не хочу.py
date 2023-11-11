def strmas(mas):
    d = ''
    for i in range(len(mas)):
        d = d + str(mas[i]) + ' '
    return d


n = open('negat', 'r')
p = open('pol', 'r')
pol = p.read()
neg = n.read()
polo = 0
Truemas = []
Falsemas = []
for i in range(len(pol)):
    if pol[i] == ' ':
        Truemas.append(polo)
        polo = 0
    else:
        polo = polo * 10 + int(pol[i])
if polo != 0:
    Truemas.append(polo)
polo = 0
for i in range(len(neg)):
    if neg[i] == ' ':
        Falsemas.append(polo)
        polo = 0
    else:
        polo = polo * 10 + int(neg[i])
if polo != 0:
    Falsemas.append(polo)
n.close()
p.close()

p = 1111111
n = 1111111
f = open('negat', 'w')
t = open('pol', 'w')
Falsemas.append(n)
Truemas.append(p)

f.write(strmas(Falsemas))
t.write(strmas(Truemas))

f.close()
t.close()
