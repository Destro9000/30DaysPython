'''Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation).
In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. 
You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

# you output should look like this
print(data.describe())
Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)
Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

Exercises: Level 2
Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods.
Incomes is a set of incomes and its description. The same goes for expenses.'''


# Exercise 1 




# Exercise 2 
class PersonAccount:
    def __init__(self, firstname, lastname, incomes=None, expenses=None):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes if incomes is not None else set()
        self.expenses = expenses if expenses is not None else set()

    def total_income(self):
        return sum(self.incomes)

    def total_expense(self):
        return sum(self.expenses)

    def account_info(self):
        print(f"First Name: {self.firstname}")
        print(f"Last Name: {self.lastname}")
        print(f"Incomes: {self.incomes}")
        print(f"Expenses: {self.expenses}")

    def add_income(self):
        income = input("Please enter the income (blank to skip): ").strip()
        if not income:
            print("No income added.")
            return
        try:
            income = int(income)
        except ValueError:
            print("Please enter a valid number.")
            return
        if income < 0:
            print("Please enter a valid income!!")
        else:
            self.incomes.add(income)
            print("Income added!!")

    def add_expense(self):
        expense = input("Please enter the expense (blank to skip): ").strip()
        if not expense:
            print("No expense added.")
            return
        try:
            expense = int(expense)
        except ValueError:
            print("Please enter a valid number.")
            return
        if expense < 0:
            print("Please enter a valid expense!!")
        else:
            self.expenses.add(expense)
            print("Expense added!!")

    def account_balance(self):
        return self.total_income() - self.total_expense()


def handle_op(person):
    print("""
        Operations you can make:
        1 - Get your total income
        2 - Get your total expenses
        3 - Add a new income 
        4 - Add a new expenses
        5 - Get your total balance (incomes minus expenses)
        6 - Exit the application
    """)

    while True:
        op_number = input("Enter the number of operation you want to do: ").strip()
        if not op_number.isdigit():
            print("Please enter a valid number.")
            continue

        op_number = int(op_number)

        if op_number > 6 or op_number < 1:
            print("Enter a correct number of operation")
            continue

        if op_number == 1:
            print(f"Total income: {person.total_income()}")
        elif op_number == 2:
            print(f"Total expenses: {person.total_expense()}")
        elif op_number == 3:
            person.add_income()
        elif op_number == 4:
            person.add_expense()
        elif op_number == 5:
            print(f"Account balance: {person.account_balance()}")
        else:
            print("Exiting application.")
            return

        print()  # blank line for readability


# Main flow
firstnamee = input("Enter your first name (blank for 'John'): ").strip() or "Banana"
lastnamee = input("Enter your last name (blank for 'Doe'): ").strip() or "Spllt"

person = PersonAccount(firstnamee, lastnamee)

handle_op(person)
    
    
    
    
  
  