import math
import os
from collections import Counter
def entrop():
    data = file_finder()
    entropy = 0
    letters = 0
    a = list(Counter(data).values())
    for item in a:
        freq = item / len(data)
        log2 = math.log2(freq) * freq
        entropy = entropy + log2
    return -entropy
def file_finder():
    print('введите путь до директории с вашим файлом с расширением .txt.')
    print('пример:/home/user/Desctop/shennon')
    dir =(input(': '))
    files = os.listdir(str(dir))
    txt = list(filter(lambda x: x.endswith('.txt'),files))
    print(txt)
    file = (input('введите название файла,который вы хотите использовать: '))
    use = (dir+'/'+file)
    print(file)
    file_open = open(use,'rb')
    file_print = file_open.read()
    data = list(file_print)
    return data
print(entrop())

