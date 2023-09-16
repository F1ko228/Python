text = "cuckoo cuckoo bought a hood 234"

letters = 0
allSymbols = 0
notLetters = 0

for i in text:
    if i == " ":
        continue
    else: 
        allSymbols += 1
        if i.isalpha() == True:
            letters += 1
        else: 
            notLetters += 1

dict = {}

for letter in text:
    if letter in dict:
        dict[letter] += 1
    else:
        dict[letter] = 1

with open("lab6.txt", "+w") as fileForWrite:
    fileForWrite.write("string: " + text + "\n")
    fileForWrite.write("allSymbols: " + str(allSymbols) + "\n")
    fileForWrite.write("letters: " + str(letters) + "\n")
    fileForWrite.write("notLetters: " + str(notLetters) + "\n")
    fileForWrite.write("repeatingLetters: " + str(dict) + "\n")




