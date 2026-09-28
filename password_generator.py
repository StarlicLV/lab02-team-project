"""Генератор паролів.

Створює випадковий пароль заданої довжини з літер, цифр і символів.
Використовує модуль secrets, який призначений для криптографічно
стійкої генерації випадкових значень (на відміну від random).

Приклади запуску:
    python password_generator.py                 # інтерактивний режим
    python password_generator.py -l 16           # пароль довжиною 16
    python password_generator.py -l 16 --no-symbols
    python password_generator.py -l 12 -n 5      # п'ять паролів
"""

import argparse
import secrets
import string

MIN_LENGTH = 4
MAX_LENGTH = 16
DEFAULT_LENGTH = 12
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?"


def build_pools(use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    """Повертає список наборів символів, які увімкнені."""
    pools = []
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append(SYMBOLS)
    return pools


def generate_password(length=DEFAULT_LENGTH, use_lower=True, use_upper=True,
                      use_digits=True, use_symbols=True):
    """Генерує пароль.

    Гарантує, що в паролі є принаймні один символ з кожного
    увімкненого набору.

    Raises:
        ValueError: якщо довжина поза допустимим діапазоном
            або не обрано жодного набору символів.
    """
    if not MIN_LENGTH <= length <= MAX_LENGTH:
        raise ValueError(
            f"Довжина має бути від {MIN_LENGTH} до {MAX_LENGTH} символів."
        )

    pools = build_pools(use_lower, use_upper, use_digits, use_symbols)
    if not pools:
        raise ValueError("Потрібно обрати хоча б один тип символів.")

    # По одному символу з кожного набору, щоб пароль був різноманітним.
    password = [secrets.choice(pool) for pool in pools]

    # Решту довжини добираємо з усіх наборів разом.
    all_chars = "".join(pools)
    password += [secrets.choice(all_chars) for _ in range(length - len(password))]

    # Перемішуємо, щоб обов'язкові символи не стояли на початку.
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def ask_yes_no(question, default=True):
    """Ставить запитання «так/ні» і повертає True або False."""
    hint = "Т/н" if default else "т/Н"
    answer = input(f"{question} [{hint}]: ").strip().lower()
    if not answer:
        return default
    return answer in ("т", "так", "y", "yes")


def interactive_mode():
    """Запитує параметри у користувача і виводить пароль."""
    print("=== Генератор паролів ===")

    raw = input(f"Довжина пароля [{DEFAULT_LENGTH}]: ").strip()
    if raw:
        try:
            length = int(raw)
        except ValueError:
            print("Помилка: довжина має бути цілим числом.")
            return
    else:
        length = DEFAULT_LENGTH

    use_lower = ask_yes_no("Малі літери (a-z)?")
    use_upper = ask_yes_no("Великі літери (A-Z)?")
    use_digits = ask_yes_no("Цифри (0-9)?")
    use_symbols = ask_yes_no("Спецсимволи (!@#...)?")

    try:
        print("Ваш пароль:", generate_password(
            length, use_lower, use_upper, use_digits, use_symbols
        ))
    except ValueError as error:
        print(f"Помилка: {error}")


def parse_args():
    """Розбирає аргументи командного рядка."""
    parser = argparse.ArgumentParser(description="Генератор випадкових паролів.")
    parser.add_argument("-l", "--length", type=int,
                        help=f"довжина пароля ({MIN_LENGTH}-{MAX_LENGTH})")
    parser.add_argument("-n", "--count", type=int, default=1,
                        help="кількість паролів (за замовчуванням 1)")
    parser.add_argument("--no-lower", action="store_true", help="без малих літер")
    parser.add_argument("--no-upper", action="store_true", help="без великих літер")
    parser.add_argument("--no-digits", action="store_true", help="без цифр")
    parser.add_argument("--no-symbols", action="store_true", help="без спецсимволів")
    return parser.parse_args()


def main():
    args = parse_args()

    # Без аргументу --length працюємо в інтерактивному режимі.
    if args.length is None:
        interactive_mode()
        return

    try:
        for _ in range(max(args.count, 1)):
            print(generate_password(
                args.length,
                use_lower=not args.no_lower,
                use_upper=not args.no_upper,
                use_digits=not args.no_digits,
                use_symbols=not args.no_symbols,
            ))
    except ValueError as error:
        print(f"Помилка: {error}")


if __name__ == "__main__":
    main()
