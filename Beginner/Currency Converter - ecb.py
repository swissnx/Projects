
#pip install CurrencyConverter
#https://pypi.org/project/CurrencyConverter/

from currency_converter import CurrencyConverter
import pycountry


# list the available currencies
try:
    rates = CurrencyConverter()
    currencies = rates.currencies
    print(list(currencies))

    user = input("\nWould you like to know Currency Code countries? (y/n): ")
    print()
    if user == "y":
        try:
            currencies = rates.currencies
            for currency in currencies:
                country = pycountry.currencies.get(alpha_3=currency)
                if country:
                    print(f"{currency} - {country.name}")
    
        except Exception as e:
            print(f"Problem is: {e}")

except Exception as e:
    print(f"Problem is: {e}")


# conversion
try:
    rates = CurrencyConverter()
    amount = int(input("\nEnter amount: "))
    from_currency = input("From Currency: ").upper()
    to_currency = input("To Currency: ").upper()
    result = rates.convert(amount, from_currency, to_currency)

    print(f"\n{amount} {from_currency} = {result:.2f} {to_currency}\n")

except Exception as e:
    print(f"Problem is: {e}")
