file = open('Данные', 'a', encoding="UTF-8")
g = 0
for nine in open('Данные', 'r', encoding="UTF-8"):
    g = nine[0]
if g == 'Н':
    g = 0

naz = input("Название достопремечательности ")
opisan = input("Название описание ")
naz.lower()
nazvan = naz
opisan.lower()
vowels = "бвгджзйклмнпрстфхцчшщъь"
for letter in naz:
    if letter in vowels:
        naz = naz.replace(letter, "@")
vowels = "аеёиоуыэюя"
for letter in naz:
    if letter in vowels:
        naz = naz.replace(letter, "№")


while naz.count('\t') or opisan.count('\t') or '@@@' in naz or '№№№' in naz:
    if naz.count('\t'):
        naz = input("Название достопремечательности без таба ")
        naz.lower()
        nazvan = naz
        opisan.lower()
        vowels = "бвгджзйклмнпрстфхцчшщъь"
        for letter in naz:
            if letter in vowels:
                naz = naz.replace(letter, "@")
        vowels = "аеёиоуыэюя"
        for letter in naz:
            if letter in vowels:
                naz = naz.replace(letter, "№")
    elif opisan.count('\t'):
        opisan = input("Название описание без таба ")
    elif '@@@' in naz:
        print("Название достопремечательности правильное")
        naz = input()
        naz.lower()
        nazvan = naz
        opisan.lower()
        vowels = "бвгджзйклмнпрстфхцчшщъь"
        for letter in naz:
            if letter in vowels:
                naz = naz.replace(letter, "@")
        vowels = "аеёиоуыэюя"
        for letter in naz:
            if letter in vowels:
                naz = naz.replace(letter, "№")
    elif '№№№' in naz:
        print("Название достопремечательности правильное")
        naz = input()
        naz.lower()
        nazvan = naz
        opisan.lower()
        vowels = "бвгджзйклмнпрстфхцчшщъь"
        for letter in naz:
            if letter in vowels:
                naz = naz.replace(letter, "@")
        vowels = "аеёиоуыэюя"
        for letter in naz:
            if letter in vowels:
                naz = naz.replace(letter, "№")


file.write(str(int(g) + 1) + '\t' + nazvan + '\t' + opisan + ' 1' + ' ' + '1'+'\n')

file.close()
l = 0
for nine in open('Данные', 'r', encoding="UTF-8"):
    if l == 0:
        l = 1
    else:
        print(nine[2:nine.find('\t', 2)], end=' ')
        print(nine[nine.find('\t', 2)+1:-4], nine[-4], nine[-2])
l = 0
