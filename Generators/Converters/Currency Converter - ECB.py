
from currency_converter import CurrencyConverter
import pycountry


class Currency:
    def __init__(self):
        self.__rates = CurrencyConverter()
        self.__currencies = self.__rates.currencies

    def __list_currencies(self):
        print(list(self.__currencies))

    def __list_currency_countries(self):
        for currency in self.__currencies:
            country = pycountry.currencies.get(alpha_3=currency)
            if country:
                print(f"{currency} - {country.name}")

    def __convert_currency(self, amount, from_currency, to_currency):
        result = self.__rates.convert(amount, from_currency, to_currency)
        print(f"\n{amount} {from_currency} = {result:.2f} {to_currency}\n")

    def __run(self):
        try:
            self.__list_currencies()
            user = input("\nWould you like to know Currency Code countries? (y/n): ")
            print()
            if user == "y":
                try:
                    self.__list_currency_countries()
                except Exception as e:
                    print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

        try:
            amount = int(input("\nAmount: "))
            from_currency = input("From Currency: ").upper()
            to_currency = input("To Currency: ").upper()
            self.__convert_currency(amount, from_currency, to_currency)
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    currency = Currency()
    currency.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
#pip install CurrencyConverter
#https://pypi.org/project/CurrencyConverter/