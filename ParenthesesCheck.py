#parentheses check
s = "[{()]"
l = []
ol = ["{","[","("]
cl = ["}","]",")"]
for i in s:
    if(i=="{"):
        l.append("{")
    if(i=="["):
        l.append("[")
    if(i=="("):
        l.append("(")
        
    if(i=="}" or i=="]" or i==")"):
        pos = cl.index(i) 
        if ((len(l) > 0) and
            (ol[pos] == l[len(l)-1])): 
            l.pop() 
    

if len(l) == 0: 
    print("Balanced")
else: 
    print("Unbalanced")
    