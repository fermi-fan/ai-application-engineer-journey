# A simple hash table implementation using a list
my_hash_set = [None,'Jones',None,'Lisa',None,'Bob',None,'Siri','Pete',None]
def hash_function(value):
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char)
    return sum_of_char % 10

def contains(value):
    index = hash_function(value)
    return my_hash_set[index] == value

print(contains('Bob'))  # Output: True
print(contains('Alice'))  # Output: False    


my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]

def hash_function(value):
    return sum(ord(char) for char in value) % 10

def add(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    if value not in bucket:
        bucket.append(value)

def contains(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    return value in bucket

add('Stuart')        

print(my_hash_set)
print("contains 'Bob':", contains('Bob')) 