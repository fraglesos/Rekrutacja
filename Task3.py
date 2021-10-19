# %%
# Description
# Inserts number of spaces equal fullSpaces at the end of all but last words in a string and one additional space 
# for first leftSpaces words. Total numbers of spaces complement length of the string to maxW.
#
# Parameters
# string - string to be complemented with spaces
# maxW - number of chars in a final string
#
# Return
# Returns complemented string.

def addSpaces(string, maxW):
    numSpaces = maxW - len(string)
    wordsList = string.split()
    i = 0
    pos = 0
    positions = [];
    pos = string.find(" ")
    positions.append(pos)
    while pos != -1:
        pos = string.find(" ",pos+1)
        positions.append(pos)
    del positions[-1]
    fullSpaces = numSpaces // len(positions)
    leftSpaces = numSpaces % len(positions)
    tempWordsList = [i + (fullSpaces+1)*" " for i in wordsList[:-1]]
    wordsList = tempWordsList + [wordsList[-1]]
    tempWordsList = wordsList[:leftSpaces]
    tempWordsList = [i + " " for i in tempWordsList]
    wordsList = tempWordsList + wordsList[leftSpaces:]
    return ''.join(wordsList)

# %%
# Description
# This part creates desired output. It takes parts of the input and stores it in temp.
# Then it iterates through temp starting from the end until only whole words are chosen. Then it takes the lenght
# of the temp variable before the spaces are added and adds it to the cond variable.
# This ensures correct breaking of the last line. After this spaces are added with addSpaces function. After the 
# spaces are placed, the whole line is added to the output table. When the loop is terminated, the 
# remaining text is added to the end of out. In the end output is printed as string.
#
# Variables
# maxW - as in addSpaces function
# inp - input text. Too long text causes errors.
# out - output text
# i - points to a place in inp from which new line is taken
# cond - terminates the loop when length of the input is shorter then text taken so far + maxW
# temp - line of text which will go to output after cutting to full words and inserting spaces
# j - position at which last full word of temp ends
# char - takes a letter from temp in purpose of checking if it is a space
# 

maxW = 16
inp = "Hey there mate, it’s nice to finally meet you!"
out=[]

i = 0
cond = 0
while len(inp) > cond+maxW:
    temp = inp[i:i+maxW]

    j = maxW-1
    char = temp[j]
    while char.isspace() == False:
        j=j-1
        char = temp[j]
    
    temp = temp[:j]
    cond = cond + len(''.join(temp))
    temp = addSpaces(temp,maxW)
    out.append(temp)
    temp=[]
    i=i+j+1
else:
    out.append(inp[i:])
print("\n".join(out))

# %%
