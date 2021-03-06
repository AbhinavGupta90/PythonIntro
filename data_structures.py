list_of_veg = ["Carrot", "Cabbage", "Turnip", "Parsnip", "Brussel sprout", "Beetroot"]
list_of_numbers = [12, 345, 223, 13, 111]

print(max(list_of_numbers)) #345
print(max(list_of_veg)) #Turnip
print(min(list_of_numbers)) #12
print(min(list_of_veg)) #Beetroot
print(len(list_of_veg)) #6
list_of_numbers.append(34)
print(len(list_of_numbers))
list_of_veg.append("Celery")
print(len(list_of_veg))
list_of_numbers.insert(1, 1223) #[12, 1223, 345, 223, 13, 111, 34]
print(list_of_numbers)
list_of_numbers.insert(10, 992) # [12, 1223, 345, 223, 13, 111, 34, 992]
print(list_of_numbers)
print(list_of_numbers.index(223))
print(list_of_veg.index("Turnip"))

#PUZZLES

list_of_strings = ["Dog", "Elephant", "Cat", "Fish", "Monkey", "Horse"]
list_of_strings.remove("Cat")
list_of_strings[1] = "Zebra"
del list_of_strings[len(list_of_strings)-1]
#list_of_strings.extend("Blazej")
list_of_strings.append("Blazej")
list_of_strings.extend(["Giraffe", "Mouse"])
list_of_strings = list_of_strings + ["Hamster", "Kangaroo", "Gorilla"]

print(list_of_strings)
print(list_of_strings[:6])
print(list_of_strings[3:(len(list_of_strings)-1)])
print(list_of_strings[5:])
print(list_of_strings[0:7:2])
print(list_of_strings[1::2])
del list_of_strings[::3]
print(list_of_strings)
list_of_strings[1:4] = ["animals"]
print(list_of_strings)
list_of_strings[1] = ["Moomin", "Groak", "Snuffkin", "Troll"]
print(list_of_strings)

#SORTING

verbal_numerals = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
verbal_numerals.reverse()
print(verbal_numerals)

reversed(verbal_numerals)
counter = 0
for number in reversed(verbal_numerals):
    print(number + " ====> %s" % {counter})
    counter += 1

verbal_numerals.sort()
print(verbal_numerals)

for number in sorted(verbal_numerals, key=len):
    print(number)

for number in sorted(verbal_numerals, key=len, reverse=True):
    print(number)

## SETS

numbers = [1,2,3,3,4,2,1,3]
numbers_set = set(numbers)
numbers_set.add(4)
numbers_set.add(76)
numbers_set.remove(1)
print(numbers_set)
print(1 in numbers_set)

numbers_1_to_5 = set(range(1,6))
print(numbers_1_to_5)
numbers_6_to_12 = set(range(5, 13))
print(numbers_6_to_12)
set_of_all_numbers = numbers_1_to_5 | numbers_6_to_12 ## pipe joins two sets
print(set_of_all_numbers)
common_element_for_two_sets = numbers_1_to_5 & numbers_6_to_12 #should be 5
print(common_element_for_two_sets)

## DICTIONARY

occurances = dict(a=5, b=6, c=7, d=64)
occurances['a'] = 25
keys_of_occurances = occurances.keys()
values_of_occuerences = occurances.values()
print(values_of_occuerences)
print(keys_of_occurances)
print(occurances)
print(occurances.items())

for(key, value) in occurances.items():
    print("%s => %s" % ({"1" + key}, {30 + value}))

del occurances['a']
print(occurances)

squares_of_first_ten_numbers = [num*num for num in range(1, 11)]
print(type(squares_of_first_ten_numbers))
squares_of_nums_between_ten_and_twenty_set = {num*num for num in range(10, 21)}
print(squares_of_nums_between_ten_and_twenty_set)
squares_of_nums_between_twenty_and_thirty_dict = {num: num*num for num in range(20, 31)}
print(squares_of_nums_between_twenty_and_thirty_dict)
print(type(squares_of_nums_between_twenty_and_thirty_dict))
print(type([])) ##list
print(type({})) ##dist
print(type(())) ##tuple

##TUPLES
def create_a_person():
    return "Person name", "Person surname", 1998, 20

print(create_a_person())
print(type(create_a_person())) ##tuple

elise = create_a_person()
name, surname, yob, age = elise
print(elise)
print(name) #Person name
print(yob) #1998

