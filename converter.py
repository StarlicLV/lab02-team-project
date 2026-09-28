"""Конвертер одиниць: довжина, маса, об'єм, температура.

Запуск:
    python converter.py              # інтерактивний режим
    python converter.py 10 км миля   # швидке перетворення
"""

import argparse
import sys

# Коефіцієнти до базової одиниці категорії
FACTORS = {
    "довжина": {  # базова: метр
        "мм": 0.001, "см": 0.01, "м": 1.0, "км": 1000.0,
        "дюйм": 0.0254, "фут": 0.3048, "миля": 1609.344,
    },
    "маса": {  # базова: кілограм
        "г": 0.001, "кг": 1.0, "т": 1000.0,
        "унція": 0.028349523125, "фунт": 0.45359237,
    },
    "об'єм": {  # базова: літр
        "мл": 0.001, "л": 1.0, "м3": 1000.0,
        "галон": 3.785411784, "пінта": 0.473176473,
    },
}

TEMPERATURE = ("C", "F", "K")
TEMP_CATEGORY = "температура"


def categories() -> list:
    """Повертає список доступних категорій."""
    return list(FACTORS) + [TEMP_CATEGORY]


def units_of(category: str) -> list:
    """Повертає список одиниць для категорії."""
    if category == TEMP_CATEGORY:
        return list(TEMPERATURE)
    if category not in FACTORS:
        raise ValueError(f"Невідома категорія: {category}")
    return list(FACTORS[category])


def find_category(unit: str) -> str:
    """Визначає категорію за назвою одиниці."""
    if unit.upper() in TEMPERATURE:
        return TEMP_CATEGORY
    for name, units in FACTORS.items():
        if unit in units:
            return name
    raise ValueError(f"Невідома одиниця: {unit}")


def convert_temperature(value: float, from_u: str, to_u: str) -> float:
    """Переводить температуру між C, F та K."""
    from_u, to_u = from_u.upper(), to_u.upper()
    if from_u not in TEMPERATURE or to_u not in TEMPERATURE:
        raise ValueError("Невідома одиниця температури (C, F, K)")
    if from_u == "C":
        celsius = value
    elif from_u == "F":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15
    if celsius < -273.15:
        raise ValueError("Температура нижче абсолютного нуля")
    if to_u == "C":
        return celsius
    if to_u == "F":
        return celsius * 9 / 5 + 32
    return celsius + 273.15


def convert(value: float, from_unit: str, to_unit: str, category: str = None) -> float:
    """Переводить value з from_unit в to_unit.

    Якщо category не вказана, вона визначається за одиницею.
    """
    if category is None:
        category = find_category(from_unit)
    if category == TEMP_CATEGORY:
        return convert_temperature(value, from_unit, to_unit)
    if category not in FACTORS:
        raise ValueError(f"Невідома категорія: {category}")
    table = FACTORS[category]
    if from_unit not in table or to_unit not in table:
        raise ValueError("Невідома одиниця виміру для цієї категорії")
    return value * table[from_unit] / table[to_unit]


def _choose(prompt: str, options: list) -> str:
    print(f"{prompt}: {', '.join(options)}")
    while True:
        answer = input("> ").strip()
        if answer in options:
            return answer
        if answer.upper() in options:
            return answer.upper()
        print("Немає такого варіанту, спробуйте ще раз.")


def interactive() -> None:
    """Інтерактивний режим роботи."""
    print("=== Конвертер одиниць ===")
    while True:
        category = _choose("Категорія", categories())
        options = units_of(category)
        from_unit = _choose("З якої одиниці", options)
        to_unit = _choose("В яку одиницю", options)
        try:
            value = float(input("Значення: ").replace(",", "."))
            result = convert(value, from_unit, to_unit, category)
            print(f"{value:g} {from_unit} = {result:.6g} {to_unit}\n")
        except ValueError as err:
            print(f"Помилка: {err}\n")
        if input("Ще раз? (т/н): ").strip().lower() != "т":
            break


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Конвертер одиниць")
    parser.add_argument("value", nargs="?", type=float, help="число")
    parser.add_argument("from_unit", nargs="?", help="з одиниці")
    parser.add_argument("to_unit", nargs="?", help="в одиницю")
    args = parser.parse_args(argv)

    if args.value is None:
        interactive()
        return 0
    if args.from_unit is None or args.to_unit is None:
        parser.error("потрібно: число, з_одиниці, в_одиницю")
    try:
        result = convert(args.value, args.from_unit, args.to_unit)
    except ValueError as err:
        print(f"Помилка: {err}", file=sys.stderr)
        return 1
    print(f"{args.value:g} {args.from_unit} = {result:.6g} {args.to_unit}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
