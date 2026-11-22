# day 16 level 1

from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = data                      # the list of numbers

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return max(self.data) - min(self.data)

    def mean(self):
        return round(sum(self.data) / len(self.data))

    def median(self):
        s = sorted(self.data)
        n = len(s)
        if n % 2 == 0:
            return (s[n // 2 - 1] + s[n // 2]) / 2
        return s[n // 2]

    def mode(self):
        value, count = Counter(self.data).most_common(1)[0]
        return {'mode': value, 'count': count}

    def var(self):
        m = sum(self.data) / len(self.data)
        return round(sum((x - m) ** 2 for x in self.data) / len(self.data), 1)

    def std(self):
        m = sum(self.data) / len(self.data)
        variance = sum((x - m) ** 2 for x in self.data) / len(self.data)
        return round(variance ** 0.5, 1)

    def freq_dist(self):
        n = len(self.data)
        counts = Counter(self.data)
        return sorted([(round(c / n * 100, 1), v) for v, c in counts.items()], reverse=True)

    def describe(self):
        m = self.mode()
        return (f"Count: {self.count()}\nSum: {self.sum()}\nMin: {self.min()}\n"
                f"Max: {self.max()}\nRange: {self.range()}\nMean: {self.mean()}\n"
                f"Median: {self.median()}\nMode: ({m['mode']}, {m['count']})\n"
                f"Variance: {self.var()}\nStandard Deviation: {self.std()}\n"
                f"Frequency Distribution: {self.freq_dist()}")

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print(data.describe())

#level two my personal accoount

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}          # description  : amount
        self.expenses = {}

    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return (f"{self.firstname} {self.lastname}\n"
                f"Total income: {self.total_income()}\n"
                f"Total expense: {self.total_expense()}\n"
                f"Balance: {self.account_balance()}")

person = PersonAccount('Hassana', 'Abdullahi')
person.add_income('Salary', 50000)
person.add_income('Gift', 5000)
person.add_expense('Food', 12000)
person.add_expense('Transport', 6000)
print(person.account_info())       