import random
import string
import os

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check_pass_len(pass_len):
    if 8 <= pass_len <= 32:
        generated_password = generate_password(pass_len)
        result = f"Сгенерированный пароль: {generated_password} + {pass_len}"
        print(result)
        with open("result.txt", "w") as f:
            f.write(result)
    else:
        print(f"{pass_len} Некорректная длина пароля! Длина должна быть от 8 до 32 символов.")

if __name__ == "__main__":
        password_length = int(os.environ.get("len_int"))
        check_pass_len(password_length)
