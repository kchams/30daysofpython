#Exercises: Day 5
#Level 1
#1. Declare an empty list
empt_list = list()

#2. Declare a list with more than 5 items
prog_languages = ['Python', 'Java', 'Php', 'Dart', 'Kotlin', 'C++']

#3. Find the length of your list
print(len(prog_languages))

#4. Get the first item, the middle item and the last item of the list
first_item = prog_languages[0]
middle_index = len(prog_languages) // 2
middle_item = prog_languages[middle_index]
last_item = prog_languages[-1]
print(first_item)
print(middle_item)
print(last_item)

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['KOFFI', 'Ali', 24, 60.20, 'Célibataire', 'Lome']

#6. Declare a list variable named it_companies and assign initial values 
# Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7. Print the list using print()
print(it_companies)

#8. Print the number of companies in the list
print(len(it_companies))

#9. Print the first, middle and last company
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

#10. Print the list after modifying one of the companies
it_companies[2] = 'HP'
print(it_companies)

#11. Add an IT company to it_companies
it_companies.append('INTEL')
print(it_companies)

#12. Insert an IT company in the middle of the companies list
middle_it_list = len(it_companies) // 2
it_companies.insert(middle_it_list, 'Lenovo')
print(it_companies)

#3. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[6] = 'ORACLE'
print(it_companies)

#14. Join the it_companies with a string '#; '
it_companies_join = it_companies.extend(['#; '])
print(it_companies)

#15. Check if a certain company exists in the it_companies list.
is_apple_exist = 'Apple' in it_companies
print(is_apple_exist)

#16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#18. Slice out the first 3 companies from the list
it_companies_3f = it_companies[:3]
print(it_companies_3f)

#19. Slice out the last 3 companies from the list
it_companies_3lst = it_companies[-3:]
print(it_companies_3lst)

#20. Slice out the middle IT company or companies from the list
middle_it = it_companies[len(it_companies) // 2]
print(middle_it)

#21. Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

#22. Remove the middle IT company or companies from the list
middle_it = len(it_companies) // 2
it_companies.pop(middle_it)
print(it_companies)

#23. Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

#24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#25. Destroy the IT companies list
del it_companies
#print(it_companies)

#26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_back = front_end + back_end
print(front_back)

#27. After joining the lists in question 26. Copy the joined list and assign it to a 
# variable full_stack, then insert Python and SQL after Redux.
full_stack = front_back.copy()
redux_index = full_stack.index('Redux')
full_stack.insert((redux_index + 1), 'Python')
python_index = full_stack.index('Python')
full_stack.insert((python_index + 1), 'SQL')
print(full_stack)

#Level 2
#1- The following is a list of 10 students ages:
#Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(min_age)
print(max_age)

#Add the min age and the max age again to the list
ages.append(19)
ages.append(26)

#Find the median age (one middle item or two middle items divided by two)
median_age = ages[len(ages) // 2]
print(median_age)

#Find the average age (sum of all items divided by their number )
len_ages = len(ages)  # 12
sum_ages = ages[0] + ages[1] + ages[2] + ages[3] + ages[4] + ages[5] + ages[6] + ages[7] + ages[8] + ages[9] + ages[10] + ages[11]
print(sum_ages)
average_age = sum_ages / len_ages
print(average_age)

#Compare the value of (min - average) and (max - average), use abs() method
min_m_average = ages[0] - average_age
max_m_average = ages[-1] - average_age
is_equal = min_m_average == max_m_average
min_small_max = min_m_average < max_m_average
max_small_min = max_m_average < min_m_average
print(is_equal)
print(min_small_max)
print(max_small_min)

#Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
middle_count = countries[len(countries)//2] 