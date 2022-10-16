# Zadanie1
"""
while True:
    def Zadanie1():
        n = int(input("\nВведите значение n = "))
        if (n < 1):
            print("Меньше одного быть не может")
        elif (n > 1001):
            print("Больше ста быть не может")
        else:
            for i in range(1, n + 1):
                a = [int(input())]
            x = max(a)
            print("Наибольшее число массива: ", x)
    Zadanie1()
"""

# Zadanie3

while True:
    def Zadanie3():
        n = int(input("\nВведите значение n = "))
        if (n < 0):
            print("Меньше нуля быть не может")
        elif (n > 100):
            print("Больше ста быть не может")
        else:
            for i in range(1, n + 1):
                a = [int(input())]
            if (a % 2 == 0):
                print(a)
    Zadanie3()


