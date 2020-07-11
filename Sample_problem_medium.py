def revWord(word):
    newword=""
    for i in range(0,len(word)):
        newword+=word[len(word)-i-1]
    return newword
    
print(revWord("buddy"))

sentence="My name is Aditya."
revSent=""
tempWord=""
for j in sentence:
    if j==" " or j==".":
        revSent+=revWord(tempWord)+j
        tempWord=""
        
    
    else:
        tempWord+=j
        
print(revSent)
