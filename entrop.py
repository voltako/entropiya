import math
import os
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
print(data)
entrop = 0
cnt = 0
logver = 1
l = len(data)
print(l)
set_list = set(data)
set_list = (list(set_list))
for item in set_list:
    ver=data.count(item)
    cnt = ver/l
    logver = math.log2(cnt) * cnt
    entrop = entrop+logver
print(-entrop)
file_open.close()