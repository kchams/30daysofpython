#Exercises: Day 6
#Level 1
#1. Create an empty tuple
ept_tuple = tuple()

#2. Create a tuple containing names of your sisters and your brothers (imaginary
# siblings are fine)

sisters = ('Koffi', 'Ali', 'Bastou', 'Abalo')
brothers = ('Rebeca', 'Fatima', 'Florence', 'Prisca')

#3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

#4. How many siblings do you have?
nb_siblings = len(siblings)
print(nb_siblings)

#5. Modify the siblings tuple and add the name of your father and mother and
# assign it to family_members
siblings = list(siblings)
siblings.append('Blandine')
siblings.append('Octave')
family_members = tuple(siblings)
print(family_members)

#Level 2
#1. Unpack siblings and parents from family_members
nb_family = len(family_members)
siblings = family_members[:nb_family - 2]
parents = family_members[-2:]
print(siblings)
print(parents)

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and
# assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal  = ('Chicken', 'Goat', 'Beef', 'Turkey')
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

#3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = food_stuff_tp [6:-6]
print(middle_item)

#5. Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print(first_three_items)
print(last_three_items)

#6. Delete the food_staff_tp tuple completely
del food_stuff_tp

#7. Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
is_Estonia_exists = 'Estonia' in nordic_countries
print(is_Estonia_exists)

#Check if 'Iceland' is a nordic country
is_Iceland_exists = 'Iceland' in nordic_countries
print(is_Iceland_exists)