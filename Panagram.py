def panagram(s):
    alphabet = "abcdefghijklmnopqrtuvwxyz"
    for c in alphabet:
        if c not in s:
            return "False"
    return "True"

string = 'the quick brown fox jumps over the  dog'
print(panagram(string))
