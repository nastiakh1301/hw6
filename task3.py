import random
import string
from pathlib import Path

path = Path(__file__).resolve().parent

def main():
    print(
        "Выберите сложность пароля:"
        "\n1. Простой"
        "\n2. Средний"
        "\n3. Сложный"
        )
    a = input()
    if a == '1':
        password = simple()
        print(password)
    elif a == '2':
        password = medium()
        print(password)
    elif a == '3':
        password = hard()
        print(password)

    check(password)    

def simple():
    password = string.ascii_lowercase
    size = 8 
    simple = ''.join(random.choice(password) for i in range(size))
    password = simple
    return password


def medium():
    password = string.ascii_letters + string.digits
    size = 8 
    medium = ''.join(random.choice(password) for i in range(size))
    password = medium
    return medium


def hard():
    password = string.ascii_letters + string.digits + string.punctuation
    size = random.randint(8, 16)
    hard = ''.join(random.choice(password) for i in range(size))

    specials = ''
    counter_d = counter_l = counter_u = 0

    for char in hard:
        if char.isdigit():
            counter_d += 1
        elif char.islower():
            counter_l += 1
        elif char.isupper():
            counter_u += 1
        elif not char.isspace():
            specials += char

    while counter_d == 0 or counter_l == 0 or counter_u == 0 or specials == 0:
        hard = ''.join(random.choice(password) for i in range(size))
        for char in hard:
            if char.isdigit():
                counter_d += 1
            elif char.islower():
                counter_l += 1
            elif char.isupper():
                counter_u += 1
            elif not char.isspace():
                specials += char
    else:
        password = hard
        return password


def save(password):
    file_path = path / "password.txt"
    with open(file_path, "a") as f:
        f.write(f"{password}\n")
    return main()


def check(password):
    file_path = path / "password.txt"
    with open(file_path, "r") as f:
        data = f.read()
        if data in f:
            print("Insecure password")
            return main()
        else:
            return save(password)


if __name__ == '__main__':
    main()