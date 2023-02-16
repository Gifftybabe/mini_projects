
def main():
    print(" This is a monthly payment loan calculator " + '\n')

    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input amount of years: "))

# Calculating the monthly payment
    monthly_interest_rate = apr / 1200
    total_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-total_months))

    print(" The monthly payment for this transaction is:%.2f" % monthly_payment)


main()
