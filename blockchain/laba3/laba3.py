import os

# флаг для работы цикла
stop_check = True
# путь где буду находится текстовые файлы
dir = 'C:/Users/Rinat/PycharmProjects/elmanIST/blockchain/laba3/file_samples'
os.chdir(dir)
# count_file = os.listdir(dir)
count_file = os.listdir()
print(count_file )
# print('count_file', count_file)
# print(dir + '/' + count_file[0])
# file_data = []
# f = open(dir + '/' + count_file[0])
# print(f.read())


# while (stop_check):
#     for file_name in count_file:
#         f = open(dir + '/' + file_name)
#         print(f.read())
#         # file_data.append(f.read())
#         f.close()
#     print(file_data)
#     stop_check = False

# for file_name in count_file:
#     print()
#     f = open(dir + '/' + file_name)
#     print(f.read())
#     # file_data.append(f.read())
#     f.close()
# print(file_data)
# stop_check = False

# """
# * Открываем файл, берем его данные
# * Сравниваем его данные с теми что мы сохранили
# * Если они не равны
#     * Находим различия в записях
#         * Полученное различие записываем во все остальные файлы
# * Если равны переходим к следующему файлу
# """
