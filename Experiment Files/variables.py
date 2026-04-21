#variables => containers for storing data values
#variables are used to store data values
# Variable is a name given to data to identify it

# In python varibles refer to memory location where data is stored
# In python, variables are created when you assign a value to it - 
# In python, you do not need to declare the variable type - Dynamic Typing


#variable naming rules =>
# Varibales name are case-sensitive. - 'name' and 'Name' are different variables
name = "Madanmohan"
Name = "Python"
print(name, Name)

# Variable should be meaningful - use names that convey the purpose of the variable (e.g., 'age' instead of 'a')
age = 25 
print(age)

#variable names cannot be a keyword - reserved words in python like 'if', 'else', 'while', 'for', 'def', etc.
# if = 10  # invalid
valid_variable = 10  # valid
print(valid_variable)

#variable names cannot start with a number, it should start with a letter or underscore. - '1name' is invalid, '_name' or 'name1' is valid
_name = "Madanmohan"
name1 = "Python"
print(_name, name1)

#variable names can only contain alpha-numeric characters & One special character underscore. - 'name@' is invalid, 'name_' or 'name1' is valid (0-9, a-z, A-Z, and _ )
name_ = "Madanmohan"
name1 = "Python"
print(name_, name1)
#variable names cannot contain spaces. use underscore(_) instead of space
first_name = "Madanmohan"
print(first_name)

# add two numbers using variables
num1 = 5
num2 = 10
print(num1 + num2)

# In python, variables can be assigned multiple values in a single line
#multiple assignments in a single line
a, b, c = 2, 4, 6
print(a, b, c)

# assigning same value to multiple variables in a single line
a = b = c = 10
print(a, b, c)
# to check the memory address of the variables use id() function
print(id(a), id(b), id(c))


#Dynamic typing => where the type of the variable is determined at runtime by the value assigned to it is called dynamic typing
#Static typing => where the type of the variable is determined at compile time means you need to specify the type of the variable when you declare it

#Dynamic Binding => data type can be changed anytime in the program
#Static Binding => data type cannot be changed once declared in the program

# In python, variables can be reassigned to different data types
var = 10        # integer
print(var, type(var))
var = "Python"  # string
print(var, type(var))
var = 10.5      # float
print(var, type(var))
var = True      # boolean
print(var, type(var))




