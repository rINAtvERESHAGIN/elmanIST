import hashlib

'''
Задание 1а|б - сверните последовательно несколько строк используя хэш функции, 
затем измените исходные строки и повторите процесс свертки написать программу 
работающую с текстовым документом) """

1) функция преобразования в sha-1

- передаем массив строк 
- переводим каждую строку
- записываем строку 
-  
'''


def convert_to_sha1(phrases: str) -> object:
    encode_phrase = phrases.encode('utf-8')
    h = hashlib.sha1(encode_phrase)
    return h.hexdigest()


def list_to_sha1(some_strings):
    converted_strings = []
    for string in some_strings:
        converted_strings.append(convert_to_sha1(string))
    return converted_strings


def change_strings(some_strings: list) -> list:
    new_strings = []
    for string_to_upper in some_strings:
        new_strings.append(string_to_upper.upper())
    return new_strings


def main_convert_sha1():
    some_strings = [
        'Прогресс человечества основывается на желании каждого человека жить не по средствам.',
        'Зависть - основа демократии.',
        'Больше всего мы благодарны за благодарность.'
    ]
    converted_strings = list_to_sha1(some_strings)

    # changed_strings = some_strings
    changed_strings = change_strings(some_strings)
    converted_strings += list_to_sha1(changed_strings)

    return converted_strings
