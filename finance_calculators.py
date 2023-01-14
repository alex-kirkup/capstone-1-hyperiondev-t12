# a program that allows the user to access two
# different financial calculators: an investment 
# calculator and a home loan repayment calculator

import math

#initial user selection
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
print()
print("Enter either 'investment' or 'bond' from the menu above to proceed:")
user_selection = input().lower()

#validate
if user_selection != "investment" and user_selection != "bond":
    raise ValueError("You need to type either 'investment' or 'bond'")

#investment selected
if user_selection == "investment":

    #get user inputs
    print("Please enter the amount of money you are depositing")
    deposit = float(input())
    print(f"Please enter the interest rate (without the % sign)")
    interest_rate = float(input())
    print("Please enter the number of years you plan to invest")
    years = int(input())
    print("Please enter whether you want 'simple' or 'compound' interest")
    interest_type = input().lower()

    #calculate return on investment + validate
    if interest_type == "simple":
        return_on_investment = deposit * (1 + interest_rate/100*years)
    elif interest_type == "compound":
        return_on_investment = deposit * (1 + interest_rate/100)**years
    else:
        raise ValueError("You need to type either 'simple' or 'compound'")

    #output
    print("------------------------------------------------")
    print(f"  Deposit value:              R{deposit}")
    print(f"  Interest rate:              {interest_rate}%")
    print(f"  Number of years:            {years}")
    print(f"  Type of interest:           {interest_type}")
    print("------------------------------------------------")
    print(f"  Total return on investment: R{round(return_on_investment,2)}")
    print("------------------------------------------------")
    
#bond selected
else:
    
    #get user inputs
    print("Please enter the present value of the house")
    value = float(input())
    print(f"Please enter the interest rate (without the % sign)")
    interest_rate = float(input())
    print("Please enter the number of months you plan to take to repay the bond")
    months = int(input())

    #calculate monthly repayment
    monthly_interest_rate = interest_rate/100/12
    monthly_repayment = (monthly_interest_rate * value) / (1 - (1 + monthly_interest_rate)**(-months))

    #output
    print("--------------------------------------")
    print(f"  Value of house:     R{value}")
    print(f"  Interest rate:      {interest_rate}%")
    print(f"  Number of months:   {months}")
    print("--------------------------------------")
    print(f"  Monthly repayments: R{round(monthly_repayment,2)}")
    print("--------------------------------------")
    


