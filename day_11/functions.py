#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum
print(add_two_numbers(7, 5))

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle (r):
    pi = 3.14
    area = pi * r ** 2
    return area
print(area_of_circle(4))

#3. Write a function called add_all_nums which takes arbitrary number of
# arguments and sums all the arguments. Check if all the list items are number
# types. If not do give a reasonable feedback

def add_all_nums (*args):
    args_sum = 0
    for arg in args:
        args_sum += arg  
    return args_sum          

print(add_all_nums(3, 6, 9))

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) 
# +32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit

def convert_celsius_to_fahrenheit(c):
    F = (c * 9/5) + 32
    return F
print(convert_celsius_to_fahrenheit(3))

#5. Write a function called check-season, it takes a month parameter and returns
# the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    autumn_months = ['September', 'October', 'November']
    winter_months = ['December', 'January', 'February']
    spring_months = ['March', 'April', 'May']
    summer_months = ['June', 'July', 'August']

    if month in autumn_months :
        return "The season is Autumn"
    elif month in winter_months :
        return "The season is Winter"
    elif month in spring_months :
        return "The season is Spring"
    elif month in summer_months :
        return "The season is Summer"
    else :
        return "The month is not correct"
    
print(check_season('February'))
print(check_season('August'))

#6. Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, x2, y1, y2):
    slope = (y2-y1) / (x2-x1)
    return slope

print(calculate_slope(3, 2, 5, 7))

#7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function
# which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn(a, b, c, x):
    eqn = (a * x**2) + (b * x) + c
    return eqn

print(solve_quadratic_eqn(3, 5, 7, 1))

#8. Declare a function named print_list. It takes a list as a parameter and it prints
# out each element of the list.
def print_list(the_list):
    for elem in the_list:
        print(elem)
    
print(print_list([1, 3, 'Book', 6]))

#9. Declare a function named reverse_list. It takes an array as a parameter and it
# returns the reverse of the array (use loops).

def reverse_list(args):
    args_reverse = []
    index = -1
    for arg in args:
        args_reverse.append(args[index])
        index = index - 1
    return args_reverse

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

#10. Declare a function named capitalize_list_items. It takes a list as a parameter
# and it returns a capitalized list of items

def capitalize_list_items(args):
    capitalized_list = []
    for arg in args:
        capitalized_list.append(arg.capitalize())
    return capitalized_list

print(capitalize_list_items(['mangodb', 'microsoft', 'html', 'css']))

#11. Declare a function named add_item. It takes a list and an item parameters. It
# returns a list with the item added at the end.

def add_item(args, item):
    args.append(item)
    return args

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat')) 
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

#12. Declare a function named remove_item. It takes a list and an item
# parameters. It returns a list with the item removed from it.

def remove_item(args, item):
    index_item = args.index(item)
    args.pop(index_item)
    return args

print(remove_item(['Me', 'You', 'We'], 'You'))
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

#13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(number):
    sum = 0
    for num in range(number + 1):
        sum += num
    return sum

print(sum_of_numbers(5)) 
print(sum_of_numbers(10)) 
print(sum_of_numbers(100)) 

#14. Declare a function named sum_of_odds. It takes a number parameter and it
# adds all the odd numbers in that range

def sum_of_odds(number):
    sum_odds = 0
    for num in range(number + 1):
        if num % 2 != 0:
            sum_odds += num
    return sum_odds

print(sum_of_odds(5)) 
print(sum_of_odds(10)) 
print(sum_of_odds(100)) 

#15. Declare a function named sum_of_even. It takes a number parameter and it
# adds all the even numbers in that - range.

def sum_of_even(number):
    sum_even = 0
    for num in range(number + 1):
        if num % 2 == 0:
            sum_even += num
    return sum_even

print(sum_of_even(5)) 
print(sum_of_even(10)) 
print(sum_of_even(100)) 

#Exercises Level 2

#1. Declare a function named evens_and_odds . It takes a positive integer as
# parameter and it counts number of evens and odds in the number

def evens_and_odds(number):
    count_evens = 0
    count_odds = 0
    for num in range(number + 1):
        if num % 2 == 0:
            count_evens += 1
        else:
            count_odds += 1
    return (f'The number of odds are {count_odds} \nThe number of evens are {count_evens}')

print(evens_and_odds(100))

#2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    factorial = 1
    for num in range (1, number + 1):
        factorial *= num
    return factorial

print(factorial(5))
print(factorial(10))

#2. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    return param == ''

print(is_empty('Hello'))
print(is_empty(''))
