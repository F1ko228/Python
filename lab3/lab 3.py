# lab3
def square(a, b, c): 
    D = b**2 - 4*a*c
    if D < 0:
        print("Дискриминант меньше 0")
    elif D == 0:
        x = (-b)/(2*a)
        print(f"Корень уравнения равен {x}")
    else:
        x1 = (-b + (D ** 0.5))/(2*a)
        x2 = (-b - (D ** 0.5))/(2*a)
        print(f"Корни уравнения равны {x1} и {x2}")  
    

def setupValues():
    while(True):
        try:
            a = int(input("Введите переменную a: "))
            b = int(input("Введите переменную b: "))
            c = int(input("Введите переменную c: "))
            return {"a": a, "b": b, "c": c}
        except: 
            print("Некорректно")

values = setupValues()

square(values['a'], values['b'], values['c'])
        
    

    

    