# lab2.1

year = int(input("Введите ваш возраст: "))

if 11 <= year <= 14:
    print(f"{year} лет")
elif 2 <= year % 10 <= 4:
    print(f"{year} года")
elif year % 10 == 1:
    print(f"{year} год")
else: 
    print(f"{year} лет")


# lab2.2

cmd = 0
flag = True
while (flag):
    value = int(input("Введите число: "))
    cmd += value
    if(value == 0):
        flag = False
print(f"Сумма введенных чисел равна {cmd}")