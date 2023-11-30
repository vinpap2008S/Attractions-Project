p = open('sitis.txt', 'r', encoding="utf8")
a = []
d = 0
for line in p.readlines():
    if len(line) >= 3:
        if a.count(line[:-1]) == 1:
            d+=1
        else:
            a.append(line[:-1])

print(a)
print(d)

p.close()