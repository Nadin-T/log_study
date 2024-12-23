from datetime import datetime, timedelta


def calculate_future_date(days):
    # Получаем текущую дату
    current_date = datetime.now()

    # Создаем объект timedelta, который представляет интервал времени
    delta = timedelta(days=days)

    # Вычисляем будущую дату
    future_date = current_date + delta

    # Преобразуем будущую дату в строку в формате YYYY-MM-DD
    formatted_date = future_date.strftime('%Y-%m-%d')

    return formatted_date


if __name__ == '__main__':
    days_ahead = 10
    future_date = calculate_future_date(days_ahead)
    print(f"Дата через {days_ahead} дней: {future_date}")
