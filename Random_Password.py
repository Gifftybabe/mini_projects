import string
import random

# A list of different characters that can be used to generate the password

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()*+,-./")


def generate_password():
    password_length = int(input("How long do you want your password to be: "))

    random.shuffle(characters)

    password = []

    # To pick random character from the list of characters

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)


option = input("Do you want to generate a new password? (yes/no): ").lower()

if option == "yes":
    generate_password()

elif option == "no":
    print("Program ended")
    quit()

else:
    print("Error: Unknown option, please input yes or no")
    quit()
