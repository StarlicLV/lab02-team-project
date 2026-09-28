import math


def get_number(prompt):
    """Просить число, поки користувач не введе коректне значення."""
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Помилка: введіть число.")


def calculate(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе.")
        return a / b
    if op == "//":
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе.")
        return a // b
    if op == "%":
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе.")
        return a % b
    if op == "**":
        return a ** b
    raise ValueError("Невідома операція.")


def main():
    print("=== Калькулятор ===")
    print("Операції: +  -  *  /  //  %  **  sqrt")
    print("Для виходу введіть 'q'\n")

    while True:
        op = input("Операція: ").strip().lower()

        if op in ("q", "quit", "exit"):
            print("До побачення!")
            break

        try:
            if op == "sqrt":
                a = get_number("Число: ")
                if a < 0:
                    raise ValueError("Не можна взяти корінь з від'ємного числа.")
                result = math.sqrt(a)
            elif op in ("+", "-", "*", "/", "//", "%", "**"):
                a = get_number("Перше число: ")
                b = get_number("Друге число: ")
                result = calculate(a, op, b)
            else:
                print("Невідома операція, спробуйте ще раз.\n")
                continue

            # Прибираємо зайве ".0" у цілих результатах
            if result == int(result):
                result = int(result)
            print(f"Результат: {result}\n")

        except (ZeroDivisionError, ValueError, OverflowError) as e:
            print(f"Помилка: {e}\n")


if __name__ == "__main__":
    main()
