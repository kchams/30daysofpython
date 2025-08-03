#Exercises: Day 12
#Level 1

#1. Writ a function which generates a six digit/character random_user_id.

from random import random, randint
#def random_user_id():

#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgb_color_gen():
    number_list = []
    for i in range(3):
       number = randint(0, 255)
       number_list.append(number)
    number_tuple = tuple(number_list)
    return f'rgb{number_tuple}'  

print(rgb_color_gen())

#Exercises: Level 2

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def list_of_rgb_colors():
    return [randint(0, 255)]

print(list_of_rgb_colors())

#Level 3
#1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(args):
    shuffled_list = []
    index = -1
    for i in args:
        shuffled_list.append(args[index])
        index -= 1
    return shuffled_list

print(shuffle_list([6, 9, 'ABALO', 5, 'KOFFI']))

#2. Write a function which returns an array of seven random numbers in a range
# of 0-9. All the numbers must be unique

def seven_random_numbers():
    number_list = []
    for i in range(7):
       number = randint(0, 9)
       number_list.append(number)
    return number_list

print(seven_random_numbers()) 