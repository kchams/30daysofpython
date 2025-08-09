#Exercises: Day 18
#Level 1

#1. What is the most frequent word in the following paragraph?
paragraph = '''I love teaching. If you do not love teaching
what else can you love. I love Python if you do not love
something which can give you all the capabilities to develop
an application what else can you love.'''

#The word is : love

#2. 
'''The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in
the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract
these numbers from this whole text and find the distance between the two
furthest particles.'''

import re
import keyword

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points = [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12)

negative_points = sorted_points[0:5]
positive_points = sorted_points[5:10]
print(negative_points)
print(positive_points)

#Level 2
#1. Write a pattern which identifies if a string is a valid python variable
regex_pattern = r'^[A-Za-z_]\w*$'

def is_valid_variable(name):
    return re.match(regex_pattern, name) and not keyword.iskeyword(name)


print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

#Level 3
#1. Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve
%tea@ching%;. There $is nothing; &as& mo@re rewarding as
educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching
m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s
mo@tivate yo@u to be a tea@cher!?'''

def clean_text(txt):
    regex_pattern = r"[^A-Za-z0-9\s\.,;!?]"
    cleaned = re.sub(regex_pattern, "", sentence)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned

print(clean_text(sentence))

#Count three most frequent words in the string
from collections import Counter

def most_frequent_words(sentence):
    clean_sentence = clean_text(sentence)
    words = re.findall(r"\b\w+\b", clean_sentence.lower())
    word_counts = Counter(words)
    return word_counts.most_common(3)

print(most_frequent_words(sentence))