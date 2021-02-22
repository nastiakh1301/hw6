"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) данные владельцев,
    чьи имена начинаются на букву "m" либо заканчиваются на "а"
    (регистр не имеет значения).
    В файл записывать данные в таком формате:
    1. +380501234561 - Имя
    2. +380501234562 - Имя
    3. +380501234563 - Имя
    4. +380501234564 - Имя
    
    Julia (73) 184-34-98
 Patrick 380993889900
  mary +38(073)176-21-00
Cavin 063 789 55 67
 Helena 38(066) 123  33 77
Michael 38050 789 90 21
anna   +380 99 364 66 73
-mason-073-111-22-33-
Jacob ++38050 122 56 12
,aMaNdA 999999999"""


from pathlib import Path
import re
import string

path = Path(__file__).resolve().parent

phone_book = path / "phone_book.txt"
edited_phone_book = path / "edited_phone_book.txt"


def main():
    with open(phone_book) as f:
        count = 0
        for line in f.readlines():
            phone = re.sub(r'\D', "", line)
            phone = '+380' + phone[-9:]
            name = re.sub('[^a-zA-Z]', '', line).capitalize()
            if len(phone) == 13 and (name[0] == 'M' or name[-1] == 'a'):
                name =  re.sub('[^a-zA-Z]', '', line).capitalize()
                count += 1
                with open(edited_phone_book, "a") as f:
                    f.write(f"{count}. {phone} - {name}\n")



if __name__ == "__main__":
    main()