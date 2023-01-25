import string
import secrets
import base64


def passgen(pass_len=12):
    letters = string.ascii_letters
    numbers = string.digits
    special_char = string.punctuation

    alphabet = letters + numbers + special_char
    password = ''
    pass_strong = False

    while not pass_strong:
        password = ''
        for i in range(pass_len):
            password += ''.join(secrets.choice(alphabet))
        if (any(char in special_char for char in password) and
                sum(char in numbers for char in password) >= 2):
            pass_strong = True
    with open("passwords.text", "a") as file:
        file.write(f"{base64.b64encode(title.encode('utf-8'))}:{base64.b64encode(password.encode('utf-8'))} \n")

    return password


while True:
    user_login = int(input("what you gunna do ? \t 1-Generate a password      2-List of passwords \n >>>> "))
    if user_login == 1:
        len1 = int(input("How long is the password : "))
        title = input("Which site's password is it? (or other password) : ")
        print(passgen(len1))
        a = input("are you wanna do ir one more time (yes or no) : ")
        if a.lower() == "yes":
            continue
        else:
            break
    elif user_login == 2:

        with open("passwords.text", "r") as file:
            for line in file:
                lx = line.split(":")
                # print(base64.b64decode(lx[0][2:-1]))
                print(
                    f"Title of password : {base64.b64decode(lx[0][2:-1]).decode('utf-8')} The password : {base64.b64decode(lx[1][2:-1]).decode('utf-8')}")
        a = input("are you wanna do ir one more time (yes or no) : ")
        if a.lower() == "yes":
            continue
        else:
            break
