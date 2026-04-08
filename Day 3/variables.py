# Declare Variables
user_name = "Aghin"
user_age = 19
user_height = 5.7

# Experiment with Types
integer_value = 10
float_value = 3.14
string_value = "Hello"
boolean_value = True

# Check Types
print(type(user_name))
print(type(user_age))
print(type(user_height))
print(type(integer_value))
print(type(float_value))
print(type(string_value))
print(type(boolean_value))

# Practice Casting
string_number = "25"
converted_int = int(string_number)
print(converted_int, type(converted_int))

number = 100
converted_str = str(number)
print(converted_str, type(converted_str))

# String Formatting
print(f"My name is {user_name}, I am {user_age} years old and my height is {user_height}.")

# Input Task
birth_year = input("Enter your birth year: ")
birth_year = int(birth_year)

current_year = 2026
age = current_year - birth_year

print(f"You are {age} years old.")