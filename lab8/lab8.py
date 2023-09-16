import numpy as np


ndarray = np.random.randint(200, size=(3, 5))


print(f'Исходный двумерный массив:\n {ndarray}\n')


def sortMatrix(matrix):
    currentColumn = []
    nextColumn = []
    for sort in range(len(matrix[0])):
        for j in range(len(matrix[0]) - 1): #4  
            for i in range(len(matrix)): #3
                currentColumn.append(matrix[i][j])
                nextColumn.append(matrix[i][j + 1])
            if sum(currentColumn) > sum(nextColumn):
                for k in range(len(matrix)):
                    matrix[k][j], matrix[k][j + 1] = matrix[k][j + 1], matrix[k][j]
            currentColumn =  []
            nextColumn = []


sortMatrix(ndarray)

print(f'Отсортированный двумерный массив:\n {ndarray}\n')


for j in range(len(ndarray[0])): #5
    maxValueColumn = 0
    for i in range(len(ndarray)): #3
        if ndarray[maxValueColumn][j] < ndarray[i][j]:
            maxValueColumn = i
    ndarray[maxValueColumn][j], ndarray[len(ndarray) - 1][j] = ndarray[len(ndarray) - 1][j], ndarray[maxValueColumn][j]

ndarray = np.delete(ndarray, len(ndarray) - 1, 0)


print(f'Измененный двумерный массив:\n {ndarray}\n')

sortMatrix(ndarray)

print(f'Измененный и отсортированный двумерный массив:\n {ndarray}\n')