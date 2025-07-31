#Exercises: Day 9
#Level 1

#1. Get user input using input(“Enter your age: ”). If user is 18 or older, give
# feedback: You are old enough to drive. If below 18 give feedback to wait for
# the missing amount of years. Output:

age = input("Enter your age: ")
int_age = int(age)
if int_age == 18 or int_age > 18 :
    print('You are old enough to drive')
else : 
    missing = 18 - int_age
    print(f'You need {missing} more years to learn to drive.')

#2. Compare the values of my_age and your_age using if … else. Who is older
# (me or you)? Use input(“Enter your age: ”) to get the age as input. You can
# use a nested condition to print 'year' for 1 year difference in age, 'years' for
# bigger differences, and a custom text if my_age = your_age. Output:

my_age = 20
your_age = int(input("Enter your age: "))
if my_age > your_age :
    diff_age = my_age - your_age
    if diff_age == 1 :
        print(f'You are {diff_age} year younger than me.')
    else :
        print(f'You are {diff_age} years younger than me.')

elif my_age < your_age :
    diff_age_2 = your_age - my_age
    if diff_age_2 == 1 :
        print(f'You are {diff_age_2} year older than me.')
    else :
        print(f'You are {diff_age_2} years older than me.')
else :
    print('we are the same age')

#3. Get two numbers from the user using input prompt. If a is greater than b
# return a is greater than b, if a is less b return a is smaller than b, else a is
# equal to b. Output:
a_value = int(input("Enter number one: "))
b_value = int(input("Enter number two: "))

if a_value > b_value :
    print(f'{a_value} is greater than {b_value}')
elif a_value < b_value :
    print(f'{a_value} is smaller than {b_value}')
else :
    print(f'{a_value} is equal to {b_value}')


#Level 2
#1. Write a code which gives grade to students according to theirs scores:

score = int(input("Enter your score: "))
if score == 0 or score == 49 :
    print('0-49, F')
elif score == 50 or score == 59 :
    print('50-59, D')
elif score == 60 or score == 69 :
    print('60-69, C')
elif score == 70 or score == 89 :
    print('70-89, B')
elif score == 80 or score == 100 :
    print('80-100, A')
else :
    print('No grade for this score')


#2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
# September, October or November, the season is Autumn. December, January
# or February, the season is Winter. March, April or May, the season is Spring
# June, July or August, the season is Summer

user_input = input("Enter month: ")
if user_input in ['September', 'October', 'November'] :
    print("The season is Autumn")
elif user_input in ['December', 'January', 'February'] :
    print("The season is Winter")
elif user_input in ['March', 'April', 'May'] :
    print("The season is Spring")
elif user_input in ['June', 'July', 'August'] :
    print("The season is Summer")
else :
    print("Write the month correctly")


#3. The following list contains some fruits:

