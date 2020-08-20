from itertools import permutations
def anagram(sOriginal,cOriginal):
    l = ["".join(p) for p in permutations(sOriginal)]
    if cOriginal in l:
        return "True"
    else:
        return "False"


def anagram1(sOriginal,cOriginal):
    s = sorted(sOriginal)
    s = "".join(s)
    t = sorted(cOriginal)
    t = "".join(t)
    if(s == t):
        return "True"
    else:
        return "False"

s = "eat"
toCheck = "tea"
print(anagram1(s,toCheck))