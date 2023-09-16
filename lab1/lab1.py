from math import pi, sin, cos

# Laba 1.1

degL = int(input("Введите градусы ==> "))
minL = int(input("Введите минуты ==> "))
secL = int(input("Введите секунды ==> "))
desDeg = degL + (minL + secL/60)/60

radL = (desDeg*pi)/180

print("Градусы:", degL, "Минуты:", minL, "Секунды:", secL, sep="\n")
print("Радианы:", round(radL, 4))
print("Десятичные градусы:", round(desDeg, 4))
 
# Laba 1.2
x = float(input("Введите вещественное число ==> "))
print("Градусы:", round(x, 3), sep="\n")
print("Синус:", round(sin(x), 3), sep="\n")
print("Косинус:", round(cos(x), 3), sep="\n")
print("Квадрат:", round(x**2, 3), sep="\n")