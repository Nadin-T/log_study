from datetime import datetime

def display_current_time():
    # Получаем текущее время и дату
    now = datetime.now()

    # Форматирование даты и времени в нужный формат
    formatted_datetime = now.strftime('%Y-%m-%d %H:%M:%S')

    # Получаем день недели
    day_of_week = now.strftime('%A')

    # Получаем номер недели в году
    week_number = now.isocalendar()[1]

    # Вывод результатов
    print(f"Текущая дата и время: {formatted_datetime}")
    print(f"День недели: {day_of_week}")
    print(f"Номер недели в году: {week_number}")

if __name__ == '__main__':
    display_current_time()