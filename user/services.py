import random
import string


def add_password():
    """Функция для создания пароля"""
    pwd_length = 12

    UPPERCASE_CHARACTERS = string.ascii_uppercase
    LOWERCASE_CHARACTERS = string.ascii_lowercase
    DIGITS = string.digits
    SYMBOLS = string.punctuation

    combined_list = UPPERCASE_CHARACTERS + LOWERCASE_CHARACTERS + DIGITS + SYMBOLS

    rand_upper = random.choice(UPPERCASE_CHARACTERS)
    rand_lower = random.choice(LOWERCASE_CHARACTERS)
    rand_digit = random.choice(DIGITS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pwd = random.sample(combined_list, pwd_length - 4) + [
        rand_upper,
        rand_lower,
        rand_digit,
        rand_symbol,
    ]
    random.shuffle(temp_pwd)
    password = "".join(temp_pwd)
    return password
