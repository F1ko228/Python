import random 

list = []
CONST_N = 10
for i in range(CONST_N):
    list.append(round((random.uniform(10, 100)), 2))
print(list)

openfile = open("laba4.txt", "+w")
changesFile = open("laba4.txt", "a")

maxValue = list.index(max(list))
minValue = list.index(min(list))

try:
    openfile.write(str(list) + '\n')
finally:
    openfile.close()

try:
    list[maxValue], list[minValue] = list[minValue], list[maxValue]
    changesFile.write(str(list))
finally:
    openfile.close()
