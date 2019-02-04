"""
    Looking at Dictionary creation, comparison, copying, and adding and removing elements to and from dictionaries
"""

temp = {}
temp1 = {'key': 'value'}

print(temp == temp1)


temp2 = {'one': 1, 'two': 2, 'three': 3}
temp3 = {'three': 3, 'two': 2, 'one': 1}

print('temp2 == temp3', temp2 == temp3)

temp4 = temp3.copy()

print(temp4)

temp4['one'] = 7

print("temp4:", temp4)
print("temp3:", temp3)

temp4.pop('three')

print(temp4)

temp4['Jeff'] = 21

print(temp4)

numbers = {'one': 1, 'two': 2, 'three': 3}
numbers.setdefault('four', 4)

print(numbers)
numbers.setdefault('four', 'Four')
print(numbers)
numbers['four'] = 'Four'
print(numbers)