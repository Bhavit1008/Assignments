r=6
c = 0
for i in range(r):
    for j in range(i):
        c +=1  
        if(j!=0):
            print("* "+str(c),end=" ")
        else:
            print(c,end=" ")
    print()

c = c + 1
for i in range(r,0,-1):
    for j in range(i-1):
        c -=1  
        if(j!=0):
            print("* "+str(c),end=" ")
        else:
            print(c,end=" ")
    print()
        