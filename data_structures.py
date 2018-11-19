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

