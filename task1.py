import logging

# Логирование
logging.basicConfig(filename='my_log_1.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def sum_numbers(numbers):
    try:
        result = sum(numbers)
        logging.info(f'Сумма чисел в списке {numbers} равна {result}.')
        return result
    except TypeError:
        indices = [index for index, value in enumerate(numbers) if isinstance(value, str)]
        return logging.error(f'Ошибка: передан неверный тип данных находиться на позиции {indices}')


# Пример использования
sum_numbers([1, 2, 3, 4, 5])
sum_numbers([6, 7, 8, "A", 10])
sum_numbers([1, 2, 3, 4, "5"])
sum_numbers(["ssaoncasl"])