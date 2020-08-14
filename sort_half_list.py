a = [1 ,5 ,3 ,6 ,2 ,7 ,12 ,8 ,9 ,4]

l = len(a)

if(l%2!=0):
    print("-1")
else:
    first_half = a[:l//2]
    second_half = a[l//2:]
    res = []
    res = sorted(first_half) + sorted(second_half, reverse = True)
    print(res)