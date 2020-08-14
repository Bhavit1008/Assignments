a = [2, 3, 4 ,5, 6, 1, 2, 3, 4]

res = []

for i in a:
    if i not in res:
        res.append(i)
print(res)
#2 3 4 5 6 1