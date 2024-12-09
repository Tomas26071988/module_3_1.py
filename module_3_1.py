
# Глобальная переменная для подсчета вызовов
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    global calls
    count_calls()  # Увеличиваем счетчик вызовов
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (length, upper_case, lower_case)

def is_contains(string, list_to_search):
    global calls
    count_calls()  # Увеличиваем счетчик вызовов
    # Приводим строку и все элементы списка к одному регистру (нижнему)
    string_lower = string.lower()
    return string_lower in [item.lower() for item in list_to_search]

# Примеры вызова функций
print(string_info('Capybara'))  # Пример вызова первой функции
print(string_info('Armageddon'))  # Пример вызова первой функции
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Пример вызова второй функции
print(is_contains('cycle', ['recycling', 'cyclic']))  # Пример вызова второй функции
print(calls)  # Выводим количество вызовов функций