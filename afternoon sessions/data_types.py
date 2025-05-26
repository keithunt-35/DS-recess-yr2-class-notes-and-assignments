

#complex numbers
# complex_number = 3 + 4j
# print(complex_number) # 3 + 4j
# print(complex_number.real) # 3.0
# print(complex_number.imag) # 4.0


print("**************LISTS****************")
#lists
# A list is a collection of items that can be of different types. Lists are mutable, meaning you can change their content.
# Lists are defined using square brackets [].
# Example:
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]
# Lists can contain different data types:
mixed_list = [1, "Hello", 3.14, True]
print(mixed_list)  # Output: [1, "Hello", 3.14, True]
# Lists can be nested:
nested_list = [1, [2, 3], [4, 5]]
print(nested_list)  # Output: [1, [2, 3], [4, 5]]

#negative indexing
# Negative indexing allows you to access elements from the end of the list.
# Example:
my_list = [1, 2, 3, 4, 5]
print(my_list[-1])  # Output: 5 (last element)
print(my_list[-2])  # Output: 4 (second last element)
# Slicing
# You can extract a portion of a list using slicing.
# Example:
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # Output: [2, 3, 4] (elements from index 1 to 3)











#changing a particular element in a list
my_list = [1, 2, 3, 4, 5]
my_list[2] = "nine"
print(my_list)  



name2= 'Gloria\'s car'
print(name2)

#list constructors
# The list() constructor creates a list from an iterable (like a string, tuple, or set).
# Example:
the_list = list("Hello")
print(the_list)  # Output: ['H', 'e', 'l', 'l', 'o']
# The list() constructor can also be used to create an empty list.
empty_list = list()
print(empty_list)  # Output: []


cars = list(('audi', 'bmw', 'mercedes', 'rover', 'toyota', 'honda', 'ford', 'fiat'))
print(cars)



print("**************TYPES****************")
#types
# The type() function returns the type of an object.
# Example:
my_list = [1, 2, 3]
print(type(my_list))  # Output: <class 'list'>
# The type() function can also be used to check the type of other data types.
my_string = "Hello"
print(type(my_string))  # Output: <class 'str'>
my_integer = 42
print(type(my_integer))  # Output: <class 'int'>
my_float = 3.14
print(type(my_float))  # Output: <class 'float'>
my_boolean = True
print(type(my_boolean))  # Output: <class 'bool'>
my_complex = 3 + 4j
print(type(my_complex))  # Output: <class 'complex'>
my_tuple = (1, 2, 3)
print(type(my_tuple))  # Output: <class 'tuple'>
my_set = {1, 2, 3}
print(type(my_set))  # Output: <class 'set'>
my_dict = {"key": "value"}
print(type(my_dict))  # Output: <class 'dict'>
# The type() function can also be used to check the type of a function.
def my_function():
    pass
print(type(my_function))  # Output: <class 'function'>
# The type() function can also be used to check the type of a module.


#removning an element from a list
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5]


print("**************DICTIONARIES****************")
#dictionaries
# A dictionary is a collection of key-value pairs. Dictionaries are mutable and unordered.
# Dictionaries are defined using curly braces {}.
# Example:
my_dict = {"name": "Alice", "age": 30, "city": "New York", "is_student": False, "grades": [90, 85, 88], "address": {"street": "123 Main St", "zip": "10001"}}
print(my_dict)  
# Accessing values in a dictionary
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])  # Output: 30
print(my_dict["city"])  # Output: New York


#what is the difference between a dictionary and a set
# A dictionary is a collection of key-value pairs, while a set is an unordered collection of unique elements.
# A dictionary allows you to store and retrieve values using keys, while a set is used to store unique values without any specific order.
# Example of a set:
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
# Example of a dictionary:
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}