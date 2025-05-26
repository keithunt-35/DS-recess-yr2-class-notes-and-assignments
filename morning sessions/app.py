print("hello world this is keithunt")
diameter = 5
radius = diameter / 2
pi = 3.14
area = pi * (radius ** 2)
print("The area of the circle is:", area)
print("The diameter of the circle is:", diameter)


'''
 Python also has us covered for the rest of the basic buttons on your calculator:

Operator	Name	Description
a + b	Addition	Sum of a and b
a - b	Subtraction	Difference of a and b
a * b	Multiplication	Product of a and b
a / b	True division	Quotient of a and b
a // b	Floor division	Quotient of a and b, removing fractional parts
a % b	Modulus	Integer remainder after division of a by b
a ** b	Exponentiation	a raised to the power of b
-a	Negation	The negative of a

a == b	Equality	True if a is equal to b

'''

#abs funtion returns the absolute value of a number
print(abs(-5)) # 5
#round function rounds a number to the nearest integer
print(round(5.6)) # 6
#min function returns the smallest of the input values


help(print) # prints the help documentation for the print function
 
 #docstring is a way to document your code and provide information about the functions, classes, and modules you create.
def add(a, b):
    """
    This function adds two numbers and returns the result.
    
    Parameters:
    a (int): The first number
    b (int): The second number
    
    Returns:
    int: The sum of a and b
    """
    return a + b

help(add) 
