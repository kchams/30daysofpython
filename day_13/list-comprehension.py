#Exercises: Day 13
#1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
only_negative_zero =[i for i in numbers if i <=0]
print(only_negative_zero)

#2. Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_list = [number for first_list in list_of_lists for scd_list in first_list for number in scd_list ]
print(one_list)

#3. Using list comprehension create the following list of tuples:
numbers = [(num, num/num, num * 1,  num **2, num **3, num **4, num **5) for num in range(11) if num >0]

#4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_list = [[elem.upper()] for countries_list in countries for scd_list in countries_list for elem in scd_list]
print(new_list)

#5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_dict = [{'country': country[0][0].upper(), 'city': country[0][1].upper()} for country in countries]
print(list_dict)

#6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_concatenated = [name[0][0] + ' ' + name[0][1] for name in names]
print(names_concatenated)

#7. Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)
print(slope(6, 2, 7, 9))
