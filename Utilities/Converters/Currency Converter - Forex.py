
from forex_python.converter import CurrencyRates
import pycountry


class Currency:
    def __init__(self):
        self.__currency_rates = CurrencyRates()
        self.__rates = self.__currency_rates.get_rates('USD')
        self.__currencies = list(self.__rates.keys())

    def __list_currencies(self):
        print(list(self.__currencies))

    def __list_currency_countries(self):
        for currency in self.__currencies:
            country = pycountry.currencies.get(alpha_3=currency)
            if country:
                print(f"{currency} - {country.name}")

    def __convert_currency(self, amount, from_currency, to_currency):
        result = self.__currency_rates.convert(from_currency, to_currency, amount)
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
                    return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"
                
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

        try:
            amount = int(input("\nEnter amount: "))
            from_currency = input("From Currency: ").upper()
            to_currency = input("To Currency: ").upper()

            self.__convert_currency(amount, from_currency, to_currency)

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    currency = Currency()
    currency.run()


# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
#pip install forex-python