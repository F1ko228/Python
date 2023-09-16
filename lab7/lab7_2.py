flightRead = open("lab7_2.txt", "r")
flightInfo = flightRead.readlines() 
flightRead.close()

flightList = []
for i in range(len(flightInfo)):
    flightList.append((flightInfo[i].split()))
value = ""
while value != "-":
        value = input("Назовите данные рейса: ")
        for i in range(len(flightList)):
            if(flightList[i][0] == value) or (flightList[i][2] == value):
                print(" ".join(flightList[i]))
    
