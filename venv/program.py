name = "Blazej"
surname = "Wielk"
print("Test print")
print(name + " " + surname)

def print_personal_details(name, surname, yob):
    print("NAME: " + name
          + "\nSURNAME: " + surname
          + "\nYEAR OF BIRTH: " + yob)

print_personal_details(name, surname, "1992")

def print_personal_details_multiple_times(number_of_times, name, surname, yob):
    for i in range(1, number_of_times+1):
        print("TIMES " + str(i))
        print_personal_details(name, surname, yob)

print_personal_details_multiple_times(5, name, surname, "1992")

def conduct_squaring(i):
    print(str(i) + " X " + str(i) + " = " + str(i * i))

def print_squares_of_numbers_up_to(num):
    print("ALL NUMBERS SQUARED UP TO " + str(num))
    for i in range(1, num+1):
       conduct_squaring(i)

def print_squares_of_even_numbers_up_to(num):
    print("SQUARED EVEN NUMBERS UP TO " + str(num))
    for i in range (0, num+1, 2):
        conduct_squaring(i)

def print_squares_of_numbers_up_to_backwards(num):
    print("BACKWARDS")
    for i in range(num, 1, -1):
        conduct_squaring(i)

print_squares_of_numbers_up_to(12)
print_squares_of_even_numbers_up_to(10)
print_squares_of_numbers_up_to_backwards(10)