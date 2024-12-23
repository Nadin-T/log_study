import argparse


def main():
    # Создаем парсер
    parser = argparse.ArgumentParser(description="Обработка чисел и строки.")

    # Добавляем обязательные аргументы
    parser.add_argument('number', type=int, help='Целое число для обработки')
    parser.add_argument('text', type=str, help='Текстовая строка для повторения')

    # Добавляем необязательные аргументы
    parser.add_argument('--verbose', action='store_true', help='Выводит дополнительные сообщения')
    parser.add_argument('--repeat', type=int, default=1, help='Сколько раз повторить строку (по умолчанию 1)')

    # Парсим аргументы
    args = parser.parse_args()

    # Обработка аргументов с использованием verbose режима
    if args.verbose:
        print(f'Полученные аргументы: number={args.number}, text = "{args.text}", repeat = {args.repeat}')


    # Вывод строки в количестве указанных повторений
    print(f'Число: {args.number}, Строка: {args.text * args.repeat}')


if __name__ == "__main__":
    main()

