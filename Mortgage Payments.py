PaymentOptions = {
    "Monthly":12,
    "Semi-monthly":24,
    "Bi-weekly":26,
    "Weekly": 52,
    "Rapid Bi-weekly":1, #1 is a placeholder because these will just use the monthly payments to divide by 2 and 4 respecitively
    "Rapid Weekly":1
    }

while True: 
    #Class iniatilization
    class MortgagePayment:
        def __init__(self, lv=(), r=(), n=(), frequency=()):
            self.__loanvalue = lv
            self.__interest = r
            self.__amoritization = n
            self.__frequency = frequency
            pass
        def calculate(self):
            i = ((1 + (self.__interest/2))**(2/self.__frequency))-1  #convert to effective rate depending on payment schedule as given interest is given APR with semi-annual compounding
            pmt = self.__loanvalue / ((1-(1+i)**(-self.__amoritization*self.__frequency))/(i))
            return pmt

    #Front-end code
    print ("-"*50)
    print ("Welcome to Oli's Mortgage Payment Calculator!")
    print ("-"*50)

    LoanAmt = float(input("Loan Amount($): "))
    Interest = float(input("Interest Rate(%): "))/100
    Amoritization = int(input("Amoritization Period: "))

    print ("-"*50)
    print ("PAYMENT OPTIONS AVAILABLE:")

    #monthly payment calculation just for use in rapid weekly and bi-weekly payments
    monthly_result = MortgagePayment(LoanAmt, Interest, Amoritization, PaymentOptions["Monthly"])
    monthly_payment = monthly_result.calculate()

    for key, freq in PaymentOptions.items():
        result = MortgagePayment(LoanAmt, Interest, Amoritization, frequency=freq)
        payment = result.calculate()

        if "Rapid Bi-weekly" in key: #overide the class calculation with hardcode due to simplicity in calculating the rapid payments
            payment = monthly_payment / 2
        elif "Rapid Weekly" in key:
            payment = monthly_payment / 4

        print (f"{key}: ${payment:.2f}")

    print ("-"*50)

    #loop i learned from Khan Academy for users to rerun code until stopped
    repeat = input("Would you like to calculate payments for another mortgage? (y/n): ").lower()
    if repeat != "y":
        print("Thank you for using Oli's Mortgage Calculator! Goodbye 👋")
        break

#Exchange Rate Program ----------------------------------
print ("-"*50)
print ("Mortgage Payment Calculator terminated")
print ("-"*50)

