#type conversion => converting one data type to another data type
# in python two types of type conversion
# 1. implicit type conversion => done by the compiler
# 2. explicit type conversion => done by the user


#implicit type conversion
num1 = 5
num2 = 10.6
result = num1 + num2
print(result)
print(type(result))

#explicit type conversion
num1 = 5
num2 = 10.9
result = num1 + int(num2)
print(result)
print(type(result))

# int() => converts to integer
# float() => converts to float
# str() => converts to string
# bool() => converts to boolean
# complex() => converts to complex
