#Exercises: Day 21
#Level 1

"""
1. Python has the module called statistics and we can use this module to do all
the statistical calculations. However, to learn how to make function and reuse
function let us try to develop a program, which calculates the measure of
central tendency of a sample (mean, median, mode) and measure of
variability (range, variance, standard deviation). In addition to those
measures, find the min, max, count, percentile, and frequency distribution of
the sample. You can create a class called Statistics and create all the
functions that do statistical calculations as methods for the Statistics class.
Check the output below
"""
import statistics
from collections import Counter

class Statistics:

    def __init__(self, data):
        self.data = data

    def mean(self):
       return statistics.mean(self.data)

    def median(self):
        return statistics.median(self.data)
    
    def mode(self):
        return statistics.mode(self.data)

    def range(self):
        return self.max() - self.min()
    
    def var(self):
        return statistics.pvariance(self.data)
    
    def std(self):
        return statistics.stdev(self.data)

    def min(self):
        return min(self.data)
    
    def max(self):
        return max(self.data)
    
    def count(self):
        return len(self.data)
    
    def percentile(self):
        return statistics.percentile(self.data)
    
    def sum(self):
        return sum(self.data)
    
    def freq_dist(self):
        return Counter(self.data)

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
#print(stat.mean())

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
print('Frequency Distribution: ', data.freq_dist())

#Exercises: Level 2

"""
1. Create a class called PersonAccount. It has firstname, lastname, incomes,
expenses properties and it has total_income, total_expense, account_info,
add_income, add_expense and account_balance methods. Incomes is a set
of incomes and its description. The same goes for expenses.
"""
class PersonAccount:

    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        return sum(self.incomes.values())
    
    def total_expense(self):
        return sum(self.expenses.values())
    
    def account_info(self):
        return f'{self.firstname} {self.lastname} has {self.incomes} and has spend {self.expenses}'
    
    def add_income(self, income):
        return self.incomes.append(income)
    
    def add_expense(self, expense):
        return self.incomes.append(expense)
    
    def account_balance(self):
        return
    
person1 = PersonAccount('John', 'Doe', {'a':3, 'b':8}, {'a':4, 'b':2})

print(person1.account_info())
print(person1.total_income())
print(person1.total_expense())
#print(person1.add_income({'c':5}))