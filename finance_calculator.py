# Finance Calculator
# This is a finance calculator depending on users input it will calculate total investment or bond costs.

# Printed out phrase
print("Choose either \'investment\' or \'bond\' from the menu below:\n"
      "investment    - to calculate the amount of interest you'll earn on interest:\n"
     " bond          - to calculate theamount you'll have to pay on a home loan: ")

user_choice = input(": ").lower()

# Asked user for input based on input using if elif and else statement to determine user input.
if user_choice  == "investment" :
    deposit = float(input("Enter deposit amount: "))
    rate_percentage = float(input("Enter interest rate: ")) 
    years = int(input("Enter years for investment: "))

    print("Would you like \'simple\' or \'compound interest\': ")
    user_choice_2 = input(": ")

    if user_choice_2 == "simple" :
         total_inv = deposit * years * rate_percentage / 100
         print(f"Over {years} years your total investment  will be R{total_inv:.2f}.")
    else:
        total_inv = deposit * (pow((1 + rate_percentage / 100), years))
        print(f"Over {years} years your total investment with will be R{total_inv:.2f}.")

# Determined if simple or compound interest by usage of if and else statements and did calculations
elif user_choice == "bond" :
     deposit  = float(input("Enter house value: "))
     rate = float(input("Enter your interest rate: "))
     term_years = int(input("Enter amount of months: "))

     rate = (rate / 100) / 12

# Calculated monthly rate.
     mon_payment = (rate * deposit * ((1 + rate) ** term_years ) / (((1 + rate) ** term_years ) -1))

# Worked out monthly bond repayment with formulae.
     print(f"The monthly repayment for your bond will be R{mon_payment:.2f}.")

else:
    print("You have not made a invalid selection.")
     




