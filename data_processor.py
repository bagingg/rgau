def input_integers(prompt="Введите целые числа через пробел: "):
    raw = input(prompt)
    return list(map(int, raw.split()))


def input_floats(prompt="Введите вещественные числа через пробел: "):
    raw = input(prompt)
    return list(map(float, raw.split()))


def input_string(prompt="Введите строку: "):
    return input(prompt)


def sum_integers(numbers):
    return sum(numbers)


def average_integers(numbers):
    if not numbers:
        raise ValueError("Список пуст")
    return sum(numbers) / len(numbers)


def max_integer(numbers):
    return max(numbers)


def min_integer(numbers):
    return min(numbers)


def filter_even(numbers):
    return [n for n in numbers if n % 2 == 0]


def filter_odd(numbers):
    return [n for n in numbers if n % 2 != 0]


def sort_integers(numbers, reverse=False):
    return sorted(numbers, reverse=reverse)


def median_integers(numbers):
    if not numbers:
        raise ValueError("Список пуст")
    s = sorted(numbers)
    n = len(s)
    mid = n // 2
    return (s[mid - 1] + s[mid]) / 2 if n % 2 == 0 else float(s[mid])


def count_unique(numbers):
    return len(set(numbers))


def round_floats(numbers, decimals=2):
    return [round(n, decimals) for n in numbers]


def sum_floats(numbers):
    return sum(numbers)


def average_floats(numbers):
    if not numbers:
        raise ValueError("Список пуст")
    return sum(numbers) / len(numbers)


def reverse_string(s):
    return s[::-1]


def count_words(s):
    return len(s.split())


def to_upper(s):
    return s.upper()


def to_lower(s):
    return s.lower()


def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_char(s, char):
    return s.count(char)


def words_list(s):
    return s.split()


def capitalize_words(s):
    return " ".join(w.capitalize() for w in s.split())


def main():
    print("=== Модуль обработки данных ===\n")
    print("Выберите тип данных:")
    print("  1 - Целые числа")
    print("  2 - Вещественные числа")
    print("  3 - Строки")
    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        numbers = input_integers()
        print(f"\nВведённые числа : {numbers}")
        print(f"Сумма           : {sum_integers(numbers)}")
        print(f"Среднее         : {average_integers(numbers):.2f}")
        print(f"Максимум        : {max_integer(numbers)}")
        print(f"Минимум         : {min_integer(numbers)}")
        print(f"Чётные          : {filter_even(numbers)}")
        print(f"Нечётные        : {filter_odd(numbers)}")
        print(f"Сортировка (↑)  : {sort_integers(numbers)}")
        print(f"Сортировка (↓)  : {sort_integers(numbers, reverse=True)}")

    elif choice == "2":
        numbers = input_floats()
        print(f"\nВведённые числа : {numbers}")
        print(f"Сумма           : {sum_floats(numbers):.4f}")
        print(f"Среднее         : {average_floats(numbers):.4f}")
        print(f"Округление до 2 : {round_floats(numbers)}")

    elif choice == "3":
        s = input_string()
        print(f"\nСтрока          : {s}")
        print(f"Инверсия        : {reverse_string(s)}")
        print(f"Верхний регистр : {to_upper(s)}")
        print(f"Нижний регистр  : {to_lower(s)}")
        print(f"Кол-во слов     : {count_words(s)}")
        print(f"Слова           : {words_list(s)}")
        print(f"Палиндром?      : {'Да' if is_palindrome(s) else 'Нет'}")

    else:
        print("Неверный выбор.")


if __name__ == "__main__":
    main()
