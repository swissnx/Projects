#pip install forex-python

from forex_python.converter import CurrencyRates

try:
    rates = CurrencyRates()
    amount = int(input("Enter amount: "))
    from_currency = input("From Currency: ").upper()
    to_currency = input("To Currency: ").upper()
    result = rates.convert(from_currency, to_currency, amount)

    print(f"\n{amount} {from_currency} = {result:.2f} {to_currency}\n")

except Exception as e:
    print(f"Problem is: {e}")
