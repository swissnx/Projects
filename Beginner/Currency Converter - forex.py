
#pip install forex-python

from forex_python.converter import CurrencyRates
import pycountry


# list the available currencies
try:
    currency_rates = CurrencyRates()
    rates = currency_rates.get_rates('USD')  # replace with any valid currency code
    currencies = list(rates.keys())
    print(list(currencies))

    user = input("\nWould you like to know Currency Code countries? (y/n): ")
    print()
    if user == "y":
        try:
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
    rates = CurrencyRates()
    amount = int(input("\nEnter amount: "))
    from_currency = input("From Currency: ").upper()
    to_currency = input("To Currency: ").upper()
    result = rates.convert(from_currency, to_currency, amount)

    print(f"\n{amount} {from_currency} = {result:.2f} {to_currency}\n")

except Exception as e:
    print(f"Problem is: {e}")
