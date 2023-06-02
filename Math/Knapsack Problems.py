
class Knapsack:
    def __init__(self):
        self.__items = []
        self.__capacity = 0

    def __add_item(self, value, weight):
        self.__items.append((value, weight))

    def __set_capacity(self, capacity):
        self.__capacity = capacity

    def __fractional_knapsack(self):
        items = sorted(self.__items, key=lambda x: x[0]/x[1], reverse=True)
        value = 0
        for item in items:
            if self.__capacity >= item[1]:
                value += item[0]
                self.__capacity -= item[1]
            else:
                value += (self.__capacity/item[1]) * item[0]
                break
        return value

    def __zero_one_knapsack(self):
        n = len(self.__items)
        dp = [[0 for _ in range(self.__capacity + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for w in range(1, self.__capacity + 1):
                if self.__items[i-1][1] <= w:
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w-self.__items[i-1][1]] + self.__items[i-1][0])
                else:
                    dp[i][w] = dp[i-1][w]
        return dp[n][self.__capacity]

    def __run(self):
        try:
            n = int(input("Number of items: "))
            for i in range(n):
                value = int(input(f"Value of item {i+1}: "))
                weight = int(input(f"Weight of item {i+1}: "))
                self.add_item(value, weight)
            capacity = int(input("Capacity of the knapsack: "))
            self.set_capacity(capacity)
            print("Fractional Knapsack: ", self.__fractional_knapsack())
            print("0/1 Knapsack: ", self.__zero_one_knapsack())
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def add_item(self, value, weight):
        return self.__add_item(value, weight)

    def set_capacity(self, capacity):
        return self.__set_capacity(capacity)

    def run(self):
        return self.__run()


if __name__ == "__main__":
    knapsack = Knapsack()
    knapsack.run()

# knapsack.add_item(60, 10)
# knapsack.add_item(100, 20)
# knapsack.add_item(120, 30)
# knapsack.set_capacity(50)



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
""" The Knapsack class is used to solve the knapsack problem, which is an optimization problem where you have a set of items, each with a weight
and a value, and you need to determine which items to include in a collection so that the total weight is less than or equal to a given limit
and the total value is as large as possible.

The knapsack problem is a combinatorial optimization problem where you have a set of items, each with a weight and a value, and you need to determine
which items to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
The problem is named after the scenario of someone trying to pack the most valuable items into a knapsack without exceeding its weight limit.

There are different variations of the knapsack problem, including the 0/1 knapsack problem and the fractional knapsack problem. In the 0/1 knapsack problem,
items must be included in the collection in their entirety or not at all. In other words, you cannot include a fraction of an item in the collection.
This problem is typically solved using dynamic programming.

In the fractional knapsack problem, on the other hand, you are allowed to include fractions of items in the collection. This means that you can break items
into smaller pieces to maximize the total value of the collection. This problem can be solved using a greedy algorithm where you sort the items by their
value-to-weight ratio and include as much of each item as possible, starting with the item with the highest value-to-weight ratio. """