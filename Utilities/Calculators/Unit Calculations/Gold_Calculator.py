
class GoldPriceCalculator:
    def __init__(self):
        self.__conversion_factors = {'oz': 28.3495,
                                     'kg': 1000,
                                     't': 1000000,
                                     'ct': 1/5,
                                     'lb': 453.592,
                                     'mg': 1/1000,
                                     'gr': 1
                                     }
        self.__valid_units = ['oz', 'kg', 't', 'ct', 'lb', 'mg', 'gr']

    @staticmethod
    def __gold_price_calculator(gold_karat: int, gold_rate: float) -> float:
        gold_price = (gold_karat / 24) * gold_rate
        return round(gold_price, 2)

    def calculate_price(self, gold_karat: int, gold_rate: float, gold_rate_unit: str,
                        weight: float, weight_unit: str, making_cost: float, tax: float) -> dict:
        # Convert gold rate to specified weight unit
        if gold_rate_unit != weight_unit:
            gold_rate *= self.__conversion_factors[weight_unit] / self.__conversion_factors[gold_rate_unit]

        gold_price = (gold_karat / 24) * gold_rate * weight          # Calculate gold price based on karat
        making_cost_amount = making_cost / 100 * gold_price          # Add making cost
        tax_amount = (gold_price + making_cost_amount) * tax / 100   # Add tax
        total_price = gold_price + making_cost_amount + tax_amount

        return {'gold_price': round(gold_price, 2),               # round(number, 2) function call rounds the value of total_price to 2 decimal places
                'making_cost': round(making_cost_amount, 2),
                'tax': round(tax_amount, 2),
                'total_price': round(total_price, 2)
                }

    def __run(self):
        while True:
            print("\n1. Calculate Gold Price according to its Karat\n2. Calculate Gold Price with additional parameters")
            choice = input("\nChoice: ")

            if choice == "1":
                try:
                    gold_karat = int(input("Specify Gold Karat (1-24): "))
                    if not (1 <= gold_karat <= 24):
                        raise ValueError("Gold Karat must be between 1-24")

                    gold_rate = float(input("Current Gold Rate in $/unit: "))
                    if gold_rate <= 0:
                        raise ValueError("Gold rate must be a positive number")

                    price = GoldPriceCalculator.__gold_price_calculator(gold_karat, gold_rate)
                    print(f'Gold price per oz of {gold_karat}k: {price} USD')

                except ValueError as ve:
                    print(f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m")
                else:
                    break

            elif choice == "2":
                while True:
                    try:
                        gold_karat = int(input("Specify Gold Karat (1-24): "))
                        if not (1 <= gold_karat <= 24):
                            raise ValueError("Gold Karat must be between 1-24")

                        gold_rate = float(input("Current Gold Rate in $/unit: "))
                        if gold_rate <= 0:
                            raise ValueError("Gold rate must be a positive number")

                        gold_rate_unit = input("Specify Gold Rate Unit: ")
                        if gold_rate_unit not in self.__valid_units:
                            raise ValueError(f"Invalid unit. Valid units are {self.__valid_units}")

                        weight = float(input("Weight: "))
                        if weight <= 0:
                            raise ValueError("Weight must be a positive number")

                        weight_unit = input("Specify Weight Unit: ")
                        if weight_unit not in self.__valid_units:
                            raise ValueError(f"Invalid unit. Valid units are {self.__valid_units}")

                        making_cost = float(input("Making cost in %: "))
                        if making_cost < 0:
                            raise ValueError("Making cost must be a non-negative number")

                        tax = float(input("Tax in %: "))
                        if tax < 0:
                            raise ValueError("Tax must be a non-negative number")

                    except ValueError as ve:
                        print(f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m")
                    else:
                        break

                prices = self.calculate_price(gold_karat, gold_rate, gold_rate_unit, weight, weight_unit, making_cost, tax)

                print(f'\nPrice of pure gold ({gold_karat}k {weight_unit}): {prices["gold_price"]:.2f}')
                print(f'Making cost: {prices["making_cost"]:.2f}')
                print(f'Tax: {prices["tax"]:.2f}')
                print(f'Total price: {prices["total_price"]:.2f}')
                break

            else:
                print("Invalid choice. Please choose either option `1` or `2`.")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    calculator = GoldPriceCalculator()
    calculator.run()


# REFERENCE: [http://goldpricez.com/calculator/jewellery]
# [https://www.google.com/search?q=gold+price+tracker+source+code+youtube&rlz=1C1CHBD_en-GBAE1039AE1039&ei=gDFLZIGzN_jm7_UP0pqV8A8&ved=0ahUKEwiB8_Tgxcv-AhV487sIHVJNBf4Q4dUDCA8&uact=5&oq=gold+price+tracker+source+code+youtube&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQogQyBQgAEKIEOggIIRCgARDDBDoKCCEQoAEQwwQQCkoECEEYAFAAWNkXYNEZaABwAXgAgAG6AYgB1QiSAQMwLjaYAQCgAQHAAQE&sclient=gws-wiz-serp]
# [https://keisan.casio.com/exec/system/1227605622]
