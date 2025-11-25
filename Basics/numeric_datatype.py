# Numeric Dtatypes in Python - Integer, Float, Complex, Boolean

# 1. Integer - whole numbers positive or negative - immutable(cannot change once created) - supports all arithmetic operations
age = 25  # positive integer
temperature = -5  # negative integer
count = 0  # zero integer
print("Integer examples:", age, temperature, count)     
print(type(age), type(temperature), type(count))

########################################################################################################################

# 2. Float - numbers with decimal points - immutable - supports all arithmetic operations
height = 5.9  # positive float
weight = -70.5  # negative float
pi = 3.14159  # float representation of pi
print("Float examples:", height, weight, pi)
print(type(height), type(weight), type(pi))

# Floating point precision
a = 0.1 + 0.2
print("0.1 + 0.2 =", a)  # may not be exactly 0.3 due to precision issues
exp = 2e3 # 2 * 10^3 = 2000.0
small = 5e-4 # 5 * 10^-4 = 0.0005
print("Exponential notation examples:", exp, small)

#############################################################################################################################

# 3. Complex - numbers with real and imaginary parts - immutable - supports arithmetic operations
# Syntax: a + bj where a is the real part and b is the imaginary part
z1 = 3 + 4j  # complex number with real part 3 and imaginary part 4
z2 = 1 - 2j  # complex number with real part 1 and imaginary part -2
print("Complex number examples:", z1, z2)
print("Real part of z1:", z1.real)
print("Imaginary part of z1:", z1.imag)
print(type(z1), type(z2))
comp = complex(2, 3)  # using complex() function
print("Complex number using complex() function:", comp)

########################################################################################################################

# 4. Boolean - represents truth values - only two values - immutable - can be used in arithmetic operations (True as 1, False as 0)
is_active = True
is_admin = False
print("Boolean examples:", is_active, is_admin)
print(type(is_active), type(is_admin))

# Used in conditional statements and logical operations
x = 10
print(x > 5)  # True
print(x < 5)  # False
print(bool("Hii")) # True

# False values in Python
print(bool(0))        # False
print(bool(0.0))      # False
print(bool(""))       # False
print(bool(None))     # False
print(bool([]))       # False
print(bool(()))       # False   
print(bool({}))       # False
print(bool(set()))    # False
print(False)          # False
# Everything else is considered True

