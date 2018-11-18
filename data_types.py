integer_value = 234456
float_value = 3.456

bool_value = True
bool_value_false = False

string_value = 'string'
a_single_character = 'a'

print(type(integer_value))
print(type(float_value))
print(type(bool_value))
print(type(bool_value_false))
print(type(string_value))
print(type(a_single_character))

#division in python
print("Division in Python")
int1 = 20
int2 = 10
print(type(int2/int1))
print(type(int1/int2))

print("Slash-slash")
print(type(int2//int1))
print(type(int1//int2))

print(int2**int1)
print(pow(int2, int1))
print(round(2.33442, 3))
print(round(2.33452, 3))
print(round(2.33442, 4))
print(max(23, 11, 1, 23.1))
print(min(2, 344, 0.1))

##Strings

message = "Hello! Welcome to Python!"
lowercase_string = "i am lowercase"
print(message.upper())
print(message.lower())
print(lowercase_string.capitalize())
print(lowercase_string.find("am")) ##2
print(lowercase_string.casefold())
print("Es ist suß".casefold()) ## ß should be converted to ss
print("Ich wohne in Friedrichstraße".casefold()) ## ß should be converted#  to ss
print(message.isnumeric()) #false
print(message.istitle()) #false
print("Hello! Welcome To Python".istitle()) #true
print("1234abs".isnumeric()) #false
print("1234abs".isalpha()) #false
print("122333445".isnumeric()) #true
print("MEINNAMENISTBLAZEJ".isalpha()) #true

#Type conversion puzzles

