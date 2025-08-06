#SyntaxError
"""
PS C:\Users\admin\CODING\PYTHON2\30daysofpython\day_15> python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'Hello world' 
  File "<stdin>", line 1
    print 'Hello world'
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print('Hello world')
Hello world
"""

#NameError
"""
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
"""

"""
>>> age = 20   
>>> print(age)
20
"""

#IndexError
"""
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
"""

#ModuleNotFoundError

"""
>>> mport maths
  File "<stdin>", line 1
    mport maths
          ^^^^^
SyntaxError: invalid syntax

>>> import math 
"""

#AttributeError

"""
>>> import math 
>>> 
>>> 
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
>>>

>>> math.pi
3.141592653589793
"""

#KeyError

"""
>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['name']
'Asab'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
"""

#TypeError

"""
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

>>> 4 + int('9') 
13
>>> 4 + float('9') 
13.0
"""

#ImportError

"""
PS C:\Users\admin\CODING\PYTHON2\30daysofpython\day_15> python     
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> rom math import power
  File "<stdin>", line 1
    rom math import power
        ^^^^
SyntaxError: invalid syntax
>>> from math import pow
>>> pow(2,3)
8.0
"""

#ValueError

"""
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
"""

#ZeroDivisionError

"""
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
"""