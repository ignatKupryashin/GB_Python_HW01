def title(title_string):
    print("\n" + title_string + "\n")


def task1():
    title("1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.")
    day = int(input("Введите номер дня недели: "))
    if 0 < day < 8 and day % 1 == 0:
        if day in range(1, 6):
            print("Это номер буднего дня")
        else:
            print("это номер выходного дня")
        return
    else:
        print("Введено неверное число \n")
        task1()


def task2():
    title("2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.")

    def check_answer(x, y, z):
        answer = -(x or y or z) == (-x and -y and -z)
        print(f'x = {x}, y = {y}, z = {z} --> Ответ: {answer}')
    x = False
    y = False
    z = False
    while not (x and y and z):
        check_answer(x, y, z)
        if not z:
            z = True
        elif not y:
            y = True
            z = False
        else:
            x = True
            y = False
            z = False
        check_answer(x, y, z)


def task3():
    title("3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).")

    def quater(x, y):
        if x > 0:
            if y > 0:
                answer = 1
            else:
                answer = 4
        else:
            if y > 0:
                answer = 2
            else:
                answer = 3
        return answer

    x = int(input("Введите координату X точки: "))
    y = int(input("Введите координату Y точки: "))
    print("Ответ: " + str(quater(x, y)) + " четверть")


def task4():
    title("4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).")
    quater = int(input("Введите номер четверти: "))
    if quater in range(1, 5):
        if quater == 1 or quater == 4:
            x_coordinates = "[0; +∞)"
        else:
            x_coordinates = "(-∞; 0]"
        if quater == 1 or quater == 2:
            y_coordinates = "[0; +∞)"
        else:
            y_coordinates = "(-∞; 0]"

        print(f"Ответ: x \u2208 {x_coordinates};  y \u2208 {y_coordinates}")
    else:
        print("Введён несуществующий номер четверти")
        task4()


def task5():
    title("5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.")

    def distance(x1, x2, y1, y2):
        distance_x = x1 - x2
        distance_y = y1 - y2
        return abs((distance_x**2 + distance_y**2)**0.5)
    Ax = int(input("Введите координату X точки A: "))
    Ay = int(input("Введите координату Y точки A: "))
    Bx = int(input("Введите координату X точки B: "))
    By = int(input("Введите координату Y точки B: "))

    print(f"Расстояние между двумя точками: " +
          str(round(distance(Ax, Bx, Ay, By), 3)))


task1()
task2()
task3()
task4()
task5()
