
def main():
    print("This program converts Naira to US dollars")

    naira = eval(input("Enter amount in Naira: "))

    dollars = convert_to_dollars(naira)

    print("That is", dollars, "dollars")


convert_to_dollars = lambda naira: naira * 0.0022

main()
