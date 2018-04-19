def ransom_note(magazine, ransom):
    hist = {}
    for word in magazine:
        hist.setdefault(word,0)
        hist[word]+=1
    for word in ransom:
        if word in hist:
            hist[word]-= 1
        else:
            return False

    return all([x >= 0 for x in hist.values()])


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
