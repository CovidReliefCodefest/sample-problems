def revWord(word): # defining a function to reverse the word
    newword=""
    for i in range(0,len(word)):
        newword+=word[len(word)-(i+1)] 
    return newword

sentence="My name is Aditya."
revSent=""
tempWord="" # variable that stores the word until a space or full stop comes
for j in sentence: # traversing through the sentence
    if j==" " or j==".": # helps us sepraate each word individually and reverse it
        revSent+=revWord(tempWord)+j # calling  the revWord function to reverse the word
        tempWord=""
        
    
    else:
        tempWord+=j # adding on to the temporary word
        
print(revSent)
