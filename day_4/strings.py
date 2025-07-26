#Exercises - Day 4
#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python
space = ' '
print('Thirty' +space+ 'Days' +space+ 'Of'+space+ 'Python')

#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('Coding' +space+ 'For' +space+ 'All')

#3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#4. Print the variable company using print().
print(company)

#5. Print the length of the company string using len() method and print()
print(len(company))

#6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

#. Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9. Cut(slice) out the first word of Coding For All string
print(company[0:7])

#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
sub_campany = 'Coding'
print(company.index(sub_campany))

#11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding','Python'))

#12. Change Python for Everyone to Python for All using the replace method or other methods
language = 'Python for Everyone'
print(language.replace('Everyone', 'All'))

#13. Split the string 'Coding For All' using space as the separator (split()) 
print(company.split(' '))

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

#15. What is the character at index 0 in the string Coding For All.
print('Coding For All'[0])                      # C

#16. What is the last index of the string Coding For All
print('Coding For All'.rfind('l'))              #13

#17. What character is at index 10 in "Coding For All" string.
print('Coding For All'[10])                     # Space

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
print('Python For Everyone'[0:11:7]) # PFA


#19. Create an acronym or an abbreviation for the name 'Coding For All'
print('Coding For All'[0:11:7]) #CFA

#20. Use index to determine the position of the first occurrence of C in Coding For All.
print('Coding For All'.index('C'))              #0

#21. Use index to determine the position of the first occurrence of F in Coding For All
print('Coding For All'.index('F'))              # 7

#22. Use rfind to determine the position of the last occurrence of l in Coding For All People
print('Coding For All'.rfind('l'))              #13

#23. Use index or find to find the position of the first occurrence of the word
# 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))    #31

#24. Use rindex to find the position of the last occurrence of the word because in 
# the following sentence: 'You cannot end a sentence with because because because is a conjunction
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))  #47

#25. Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction
string = 'You cannot end a sentence with because because because is a conjunction'
print(string[0:31] + string[54:]) 

#26. Find the position of the first occurrence of the word 'because' in the following
# sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))

#27. Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string[0:31] + string[54:]) 

#28. Does ''Coding For All' start with a substring Coding?
print('Coding For All'.startswith('Coding'))        # True

#29. Does 'Coding For All' end with a substring coding?
print('Coding For All'.endswith('coding'))          # False

#30. Coding For All ' , remove the left and right trailing spaces in the given string
str_cod = ' Coding For All '
last_l = str_cod.rfind('l')
print(str_cod[1:last_l + 1])

#31. Which one of the following variables return True when we use the method isidentifier()

# This 'thirty_days_of_python' is True
print('thirty_days_of_python'.isidentifier())  #True

#32. The following list contains the names of some of python libraries: ['Django',
# 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join_result = '# '.join(python_libraries)

#33. Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge. \nI just wonder what is next')

#34. Use a tab escape sequence to write the following lines.
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

#35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
formate_string = 'The area of a circle with radius {} is {:.2f} meters square.'.format(radius, area)
print(formate_string)

#36. Make the following using string formatting methods
print(f'8 + 6 = {8 + 6}')
print(f'8 - 6 = {8 - 6}')
print(f'8 * 6 = {8 * 6}')
print(f'8 / 6 = {8 / 6:.2f}')
print(f'8 % 6 = {8 % 6}')
print( f'8 // 6 = {8 // 6}')
print(f'8 ** 6 = {8 ** 6}')