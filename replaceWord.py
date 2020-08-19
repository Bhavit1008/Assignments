s = "hi hello"
word="hi"
replacement = "hey"


l = s.split(" ")

if word in l:
    pos = l.index(word)
    l[pos] = replacement

l = " ".join(l)
print(l)

