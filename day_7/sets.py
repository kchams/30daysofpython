#Exercises: Day 7
#Level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1. Find the length of the set it_companies
length_it_companies = len(it_companies)
print(length_it_companies)

#2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['INTEL', 'HP0', 'Lenovo'])
print(it_companies)

#4. Remove one of the companies from the set it_companies
it_companies.remove('Apple')
print(it_companies)

#5. What is the difference between remove and discard
"""With remove(), if the item is not found, method will raise errors
However, discard() method doesn't raise any errors
"""

#Level 2

#1. Join A and B
A_B = A.union(B)
print(A_B)

#2. Find A intersection B
A_intrs_B = A.intersection(B)
print(A_intrs_B)

#3. Is A subset of B
print(A.issubset(B))

#4. Are A and B disjoint sets
print(A.isdisjoint(B))

#5. Join A with B and B with A
A_join_B = A.union(B)
B_join_A = B.union(A)
print(A_join_B)
print(B_join_A)

#6. What is the symmetric difference between A and B
sym_A_B = A.symmetric_difference(B)
print(sym_A_B)

#7. Delete the sets completely
del A
del B

#Level 3
#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(age_set)
length_age_set = len(age_set)
length_age_lst = len(age)
print(length_age_set > length_age_lst)
print(length_age_lst > length_age_set)      # True : length of the list is bigger than length of the set
print(length_age_set == length_age_lst)

#2. Explain the difference between the following data types: string, list, tuple and set
"""
- string : is the text data type
- list : is a collection of data, which is ordered, changeable and allows duplicate members. 
- tuple : is a collection which is ordered unchangeable, and allows duplicate members.
- set : is a collection which is unordered, un-indexed and unmodifiable, but we  
can add new items to the set. Duplicate members are not allowed. 
"""

#3. I am a teacher and I love to inspire and teach people. How many unique
# words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
sentence_lst = sentence.split()
print(sentence_lst)
sentence_set = set(sentence_lst)
print(sentence_set)
nb_unique_word = len(sentence_set)
print(nb_unique_word)