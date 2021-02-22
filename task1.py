"""
    1.
    Создать файл file_practice.txt
    Записать в него строку 'Starting practice with files'
    Файл должен заканчиваться пустой строкой
"""

"""
    2.
    Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
    Затем прочесть весь файл от начала до конца, вывести содержимое на экран
"""

"""
    3.
    Прочесть файл files/text.txt
    В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
    иначе - заменить все буквы 'e' на 'i'
    Полученный текст дописать в файл file_practice.txt
"""

"""
    4.
    Если в файле file_practice.txt четное количество элементов
    - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
    Прочесть весь файл и вывести содержимое
"""


import re
import fileinput
from pathlib import Path

path = Path(__file__).resolve().parent

file_practice = path / "file_practice.txt"
text = path / "text.txt"

with open(file_practice) as f:
    f.write("Starting practice with files")
    data = f.read()
    print(data)

with open(file_practice) as f:
    up = f.read(5)
    print(up.upper())
    f.seek(0)
    print(f.read())

with open(text) as t:
    data = t.read()
    count1 = 0
    count2 = 0
    if "i" in data:
        count1 += 1
    elif "e" in data: 
        count2 += 1

    if count1 > count2:
        data = re.sub("i", "e", data)
        with open(file_practice, "a+") as fl:
            fl.write(data)
            if len(data) % 2 == 0:
                fl.write('the end')
            else:
                fl.write('bye')              
    elif count2 > count1:
        data = re.sub("e", "i", data)
        with open(file_practice, "a+") as fl:
            fl.write(data)
            if len(data) % 2 == 0:
                fl.write('the end')
            else:
                fl.write('bye')
