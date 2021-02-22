import re
from pathlib import Path

users = Path(__file__).resolve().parent
errors = Path(__file__).resolve().parent

def main():
    phone = get_phone()
    email = get_email()
    password = get_password()

    users_list(phone, email, password)

    print(
        f"\nПоздравляем с успешной регистрацией!"
        f"\nВаш номер телефона: +{phone}"
        f"\nВаш email: {email}"
        f'\nВаш пароль: {"*"*len(password)}'
    )


def get_phone():
    phone = input("Введите номер телефона: ")
    phone = re.sub(r"\D", "", phone)
    if len(phone) > 8:
        return "380" + phone[-9:]
    else:
        errors_list(phone)
        get_phone()



def get_email():
    email = input("Введите email: ")
    if len(email) < 6 or email.count("@") != 1 or email.startswith("@"):
        print("Неверный формат. Повторите ввод.")
        errors_list(email)
        return get_email()
    return email


def get_password():
    password = input("Введите пароль: ")
    if len(password) < 8 or re.findall(r"\s", password):
        print("Пароль слишком простой. Придумайте более надежный пароль.")
        errors_list(password)
        return get_password()

    u_counter = l_counter = d_counter = s_counter = 0
    for i in password:
        if i.isupper():
            u_counter += 1
        elif i.islower():
            l_counter += 1
        elif i.isdigit():
            d_counter += 1
        else:
            s_counter += 1

    if min(u_counter, l_counter, d_counter, s_counter) == 0:
        print("Пароль слишком простой. Придумайте более надежный пароль.")
        errors_list(password)
        return get_password()

    if input("Повторите пароль: ") != password:
        print("Пароли не совпадают.")
        errors_list(password)
        return get_password()
    return password


def users_list(phone, email, password):
    with open(users / "users.txt", "a") as f:
        print(f"Phone: {phone} \nEmail: {email} \nPassword: {password}", file = f)


def errors_list(error):
    with open(errors / "errors.txt", "a") as f:
        f.write(f"Errors: {error}\n")


if __name__ == "__main__":
    main()