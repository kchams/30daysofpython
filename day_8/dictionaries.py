#Exercises: Day 
#1. Create an empty dictionary called dog
dog = dict()

#2. Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'Mydoc', 'color':'gray', 'breed':'Labrador', 'legs':4, 'age':2}

#3. Create a student dictionary and add first_name, last_name, gender, age,
# marital status, skills, country, city and address as keys for the dictionary
student_dict = {
    'first_name' : 'Rebeca',
    'last_name' : 'ABALO',
    'gender' : 'Female',
    'age' : 34,
    'marital_status' : 'Single',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country' : 'Togo',
    'city' : 'Lome',
    'address' : 'My address'
}

#4. Get the length of the student dictionary
len_student_dict = len(student_dict)
print(len_student_dict)

#5. Get the value of skills and check the data type, it should be a list
skills_value = student_dict.get('skills')
print(skills_value)

#6. Modify the skills values by adding one or two skills
skills_value.append('Html')
skills_value.append('CSS')
print(student_dict)

#7. Get the dictionary keys as a list
student_keys = student_dict.keys()
print(student_keys)

#8. Get the dictionary values as a list
student_values = student_dict.values()

#9. Change the dictionary to a list of tuples using items() method
student_list = student_dict.items()
print(student_list)

#10. Delete one of the items in the dictionary
student_dict.pop('age')
print(student_dict)

#11. Delete one of the dictionaries
del student_dict
