### Q1 :- Print the given strings as per stated format.

#Given strings:
"Data" "Science" "Mentorship" "Program"
"By" "CampusX"
#Output:
#Data-Science-Mentorship-Program-started-By-CampusX
print("Data", "Science", "Mentorship", "Program", sep="-", end="-")
print("started", end="-")
print("By", "CampusX", sep="-")

### Q2:- Write a program that will convert celsius value to fahrenheit.
celsius = float(input("Enter the temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in fahrenheit is: ", fahrenheit,"°F", sep="")

#Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

num1 = num1 + num2
num2 = num1-num2
num1= num1- num2

print("After Swapping first number is ", num1, "and second number is ", num2)
