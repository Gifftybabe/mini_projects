
def main():
    print("Welcome to the email slicer")

    email_input = input("Enter your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username : ", username)
    print("Domain : ", domain)
    print("Extension : ", extension + "\n")


while True:
    main()
