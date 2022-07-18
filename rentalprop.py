class RentalProperty():
    def __init__(self,rental_income=0):
        self.rental_income = rental_income


    def income(self):
        self.rental_income = int(input("What is your rental income? "))
        misc_input = input("Do you have have any other rental-related incomes? [y/n] ").lower()
        if misc_input == 'y':
            misc_income = int(input("How much misc. rental-related income do you receive? " ))
            self.total_income = int(self.rental_income) + int(misc_income)
            return f"You total monthly income is {str(self.total_income)}"
        elif misc_input == 'n':
            self.total_income = int(self.rental_income) 
            return f"Your total monthly income is {str(self.total_income)}"
        else:
            return "Invalid input, please try again."

    def expenses(self):
        mortgage = int(input("What is your monthly mortgage? "))
        taxes = int(input("What do you pay in property taxes? "))
        userinput = input("Would you like us to estimate your other monthly expenses? [y/n] ").lower()
        if userinput == 'y':
            propertymgmt = int(self.rental_income) * .01
            insurance = int(self.rental_income) *.01
            prop_repairs = int(self.rental_income) * .01
            vacancy = int(self.rental_income) *.02
            self.total_expenses = mortgage + taxes + propertymgmt + insurance + prop_repairs + vacancy
            return f"Your total monthly expenses are {int(self.total_expenses)}"
        elif userinput == 'n':
            misc_expenses = input("How much do you pay total in additional monthly expenses? ")
            self.total_expenses = int(mortgage) + int(taxes )+ int(misc_expenses)
            return f"Your total monthly expenses are {int(self.total_expenses)}"
        else:
            return "Invalid Input, please try again."

    def cashflow(self):
        self.cashflow = int(self.total_income) - int(self.total_expenses)
        return f"Your total monthly cash flow is {int(self.total_income) - int(self.total_expenses)}"


    def cash_on_cash(self):
        down_payment = int(input("How much did you pay for the down payment? "))
        closing = int(input("What were the closing costs? "))
        userinput2 = input("Was there a rehab budget? [y/n] ").lower()
        if userinput2 == 'y':
            rehab_budget = int(input("What was the amount? "))
        elif userinput2 == 'n':
            pass
        else:
            return "Invalid Input, please try again."
        userinput3 = input("Did you have any other misc costs? [y/n] ").lower()
        if userinput3 == 'y':
            misc_cost = int(input("What was the amount? "))
        elif userinput3 == 'n':
            pass
        else:
            return "Invalid Input, please try again."
        if userinput2 == 'y' and userinput3 == 'y':
            total_cost = down_payment + closing + rehab_budget + misc_cost 
        elif userinput2 == 'y' and userinput3 != 'y':
            total_cost = down_payment + closing + rehab_budget
        elif userinput2 != 'y' and userinput3 == 'y':
            total_cost = down_payment + closing + misc_cost 
        else:
            total_cost = down_payment + closing 
        print(f"Your total cost of investment is {total_cost}")
        annual_cashflow = int(self.cashflow) * 12
        print(f"Your annual cash flow is {annual_cashflow}")
        return f"Your cash on cash ROI for this property is {int((annual_cashflow / total_cost)* 100)}%"


def runROISim():
    house = RentalProperty()
    while True:
        prompt = input("\nWould you like to start ROI simulation? [y/n] ").lower()

        if prompt == 'y':
            print("\n==== Welcome to our ROI estimator =====")
            print("\nPlease answer the following prompts:")
            print(house.income())
            print(house.expenses())
            print(house.cashflow())
            print(house.cash_on_cash())


        elif prompt == 'n':
            print("\nThank you for using our ROI estimator.")
            break
        
        else:
            print("Invalid input.")

runROISim()

