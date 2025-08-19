#Exercises: Day 27
# Import the flask

from flask import Flask, render_template
import os
import pymongo
from bson import ObjectId

MONGODB_URI = 'mongodb+srv://chamsiyak:AJuwu4NxJ2xum95F@cluster0.peaih06.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

# Creating database
db = client.thirty_days_of_python
# Creating students collection and inserting a document
db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
print(client.list_database_names())

#Insert many students
students = [
{'name':'David','country':'UK','city':'London','age':34},
{'name':'John','country':'Sweden','city':'Stockholm','age':28},
{'name':'Sami','country':'Finland','city':'Helsinki','age':25},]

for student in students:
    db.students.insert_one(student)

student = db.students.find_one()
print(student)

student = db.students.find_one({'_id': ObjectId('5df68a23f106fe2d315bbc8c')})
print(student)

#Find all students
students = db.students.find()
for student in students:
    print(student)

students = db.students.find({}, {"_id":0, "name": 1, "country":1}) # 0 means not include and 1 means include
for student in students:
    print(student)

#Query experiment 
query = { "country":"Finland"}
students = db.students.find(query)

for student in students:
 print(student)

#Another Query 
query = { "country":"Finland", "city":"Helsinki"}
students = db.students.find(query)
for student in students:
 print(student)

 #
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
 print(student)

#Limiting documents
db.students.find().limit(3)

#Find with sort
students = db.students.find().sort('name')
for student in students:
    print(student)

students = db.students.find().sort('name',-1)
for student in students:
 print(student)

students = db.students.find().sort('age')
for student in students:
    print(student)

students = db.students.find().sort('age',-1)
for student in students:
 print(student)

app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

