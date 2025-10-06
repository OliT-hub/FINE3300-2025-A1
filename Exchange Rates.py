import csv #module for python to read csv fie easier
#file name: "BankOfCanadaExchangeRates.csv"
#only works if this file is in the same folder as the code file

class ExchangeRates:
    def __init__(self, filename):
        self.__filename = filename
        self.rate = self.getusdcad()

    def getusdcad(self):
        with open(self.__filename, 'r') as file:
            reader = csv.reader(file) 
            data = list(reader) #convert to list so i can index and reference later
            
            header = data[0] #use to check header columns
            last_row = data[-1] #use to check latest numbers

            usd_index = header.index("USD/CAD")
            return float(last_row[usd_index])
        
    def convert(self, amount, from_currency, to_currency):
            if from_currency == "USD" and to_currency == "CAD":
                return amount * self.rate
            elif from_currency == "CAD" and to_currency == "USD":
                return amount / self.rate
            else:
                raise ValueError("Conversion not supported. Use USD or CAD only.")

print ("-"*50)
print ("Welcome to Oli's (USD/CAD) Exchange Rate Calculator!")
print ("Make sure you have the BankOfCanadaExchangeRates.csv file in the same parent folder as this file for this to work")
print ("-"*50)

amount= float(input("Amount: "))
from_currency= input("From(USD/CAD): ").upper()
to_currency= input("To(USD/CAD): ").upper()

Xchange = ExchangeRates("BankOfCanadaExchangeRates.csv") #call class
Xchange_convert = round(Xchange.convert(amount,from_currency,to_currency),2)
get_rate = Xchange.getusdcad

if from_currency == "USD" and to_currency == "CAD": #check to print out personalized message depending on which way conversion
     print(f"Your USD to CAD conversion is: ${Xchange_convert} with an exchange rate of {round(get_rate(),2)}")
elif from_currency == "CAD" and to_currency == "USD":
    print(f"Your CAD to USD conversion is: ${Xchange_convert} with an exchange rate of {round(get_rate(),2)}")
print ("-"*50)