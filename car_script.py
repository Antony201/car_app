import sys


def get_reversed_string(string):
    return string[::-1]

print("------1_TASK-------")
print(get_reversed_string("string"))



print("------2_TASK-------")
"""
Декораторы нужны для оптимизации кода, они позволяют запихнуть функцию в функцию-обертку
позволяя перед/после запуска функции выполнить код из функции-обертки.

Декоратор — это функция, которая позволяет обернуть другую функцию
для расширения её функциональности без непосредственного изменения её кодa
"""

def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper

@decorator_function
def hello_world():
    print('Hello world!')

hello_world()


print("------3_TASK-------")
# car_app
def exchange(price: int, valute: str):
    if valute == "EUR":
        price = round(price /0.85)

    elif valute == "GBP":
        price = round(price *1.31)

    return price


def find_car(car_name):
    f = open("cars.txt", "r")
    cars = f.read().split("\n")

    for car_param in cars:
        car_param = car_param.split()
        file_car_name, car_price = car_param[0], car_param[1]

        if file_car_name == car_name:
            return int(car_price)

    return False




def write_car(name, price, valute):
    f = open("cars.txt", "a")
    price = exchange(int(price), valute)
    f.write("\n" +name +"  " +str(price))
    f.close()



while True:
    car_name = input("Введите название машины (Чтобы выйти, введите \q) : ")
    if car_name == "\q":
        sys.exit()


    is_price = find_car(car_name)

    if is_price:
        print("Цена данного автомобиля :", is_price, "USD")


    else:
        car = input("Ваша машина не найдена в нашей базе, пожалуйста введите текст в стиле 'цена валюта'\n:").split()


        price = car[0]
        valute = car[1]

        write_car(car_name, price, valute)

        print("Машина успешно записана")

