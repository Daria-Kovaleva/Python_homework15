import logging

# Логирование
logging.basicConfig(filename='my_log_2.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def divide_numbers(x, y):
    try:
        result = x / y
        logging.info(f'Division result: {result}')
        return result
    except ZeroDivisionError:
        logging.error('Division by zero!')
    except Exception as e:
        logging.error(f'Error during division: {e}')


divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "5")
divide_numbers(10, [1, 2, 3])