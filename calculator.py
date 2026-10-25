print("КАЛЬКУЛЯТОР")

a = float(input("Введіть перше число: "))
znak = input("Введіть дію (+, -, *, /): ")
b = float(input("Введіть друге число: "))

if znak == "+":
    print("Результат:", a + b)
elif znak == "-":
    print("Результат:", a - b)
elif znak == "*":
    print("Результат:", a * b)
elif znak == "/":
    if b != 0:
        print("Результат:", a / b)
    else:
        print("Помилка: на нуль ділити не можна!")
else:
    print("Невідома дія!")

input("Натисніть Enter, щоб закрити програму...")
