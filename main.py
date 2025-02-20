#finding first none repeated letter in word
def findFirst(wr):
        
    word = wr
    target = ""
    found = False

    word = list(word)

    for letter in range(len(word)):
        for i in range(len(word)):
            if letter != i and word[letter] == word[i]:
                
                found = True
                break
        if found == False:
            target = word[letter]
            break
        if found == True:
            found = False


    return target

print(findFirst("swiss"))
