listaa = [1,3,4,6,7,8,9]
listab = [3,4,5,6]
listac = []
for i in listaa:
    if i in listab:
        listac.append(i)

print(listac)
