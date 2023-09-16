def checkDone(list):
    if len(list) > 255:
        return print("Слишком много символов")
    return print("Подходящее количество символов", "\n")

def clearSpace(list):
    clearedText = []
    for i in range(len(list)):
        clearedText.append(" ".join(list[i].split()))
    print(clearedText)
    return clearedText

openFirstFile = open("FirstLaba5_1.txt", "+w")
try:
    openFirstFile.write(str("There   is  a   hut  at  the edge    with  skewed   porch   and an old woman lives in the hut  with a kind sunny face."))
finally:
    openFirstFile.close()

readFirstFile = open("FirstLaba5_1.txt", "r")

textFile = readFirstFile.readlines()
readFirstFile.close()
print(textFile)

checkDone(textFile)
textFile = clearSpace(textFile)

openSecondFile = open("SecondLaba5_1.txt", "+w")

try:  
    openSecondFile.write(str(textFile) + "\n")
finally:
    openSecondFile.close()


