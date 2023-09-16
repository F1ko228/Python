from operator import itemgetter

dataRead = open("lab7_1.txt", "r")

dataWorkers = dataRead.readlines()
dataRead.close()
workersMan = []
workersWoman = []
SalaryMan = []
SalaryWoman = []
averageSalaryMan = 0
averageSalaryWoman = 0


for worker in dataWorkers:
    worker = worker.split()
    if worker[2] == "man":
        workersMan.append(worker)
        SalaryMan.append(int(worker[1]))
    else:
        workersWoman.append(worker)
        SalaryWoman.append(int(worker[1]))

workersMan.sort(key=itemgetter(1), reverse=True)
workersWoman.sort(key=itemgetter(1), reverse=True)  

for worker in SalaryMan:
    averageSalaryMan += worker 
averageSalaryMan = averageSalaryMan/ len(SalaryMan)

for worker in SalaryWoman:
    averageSalaryWoman += worker 
averageSalaryWoman = averageSalaryWoman/ len(SalaryWoman)

print(f"Высшая зарплата мужчины: {workersMan[0][0]}")
print(f"Высшая зарплата женщины: {workersWoman[0][0]}" + "\n")

print(f"Средняя зарплата мужчин: {averageSalaryMan}")
print(f"Средняя зарпалата женщин: {averageSalaryWoman}")
