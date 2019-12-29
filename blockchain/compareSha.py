'''
Сравните хэши полученные в предыдущем задании, определите отличия
'''


def compare_sha(list_of_sha: list):
    part1 = list_of_sha[0:3:1]
    part2 = list_of_sha[3:6:1]

    for i in range(0, part1.__len__(), 1):
        if part1[i] == part2[i]:
            print('равныe sha1')
        else:
            print('не равныe sha1')
            print(difference(part1[i], part2[i]))


'''
так так sting это строка - то сравним каждый элемент по символьно

примерный вывод 

1 sha отлючается от 2 в столько то позициях  
выводим c22b5f9178342609428d6f51b2c5af4c0bde6a42 и где не совпало делаем _ 
'''


def difference(first: str, second: str):
    list_first = list(first)
    list_second = list(second)
    not_in = 0
    for i in range(0, first.__len__()):
        if first[i] != second[i]:
            list_first[i] = '_'
            not_in += 1
    return first + '\n' + ''.join(list_first) + ': ' + ' кол-во не совпавших элементов ' + str(not_in) + ' из ' + str(first.__len__())
