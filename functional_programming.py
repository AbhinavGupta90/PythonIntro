def multiply_by_two(number):
    return number*2

print(multiply_by_two)

def do_this_and_add_number(func, number):
    print(func(number) + number)

do_this_and_add_number(multiply_by_two,5)

function_for_methods = multiply_by_two
print(function_for_methods(10))

do_this_and_add_number(function_for_methods, 10)

def multiply_by_three(number):
    return number*3

#LAMBDAS

do_this_and_add_number(lambda number: number*3, 12)
do_this_and_add_number(lambda number: number*5, 100)
do_this_and_add_number(lambda number: number*number, 100)

list_of_numbers = []
for number in range(1,21):
    list_of_numbers.append(number)

filtered_list = list(filter(lambda num: num%2==0, list_of_numbers))
print(filtered_list)

filter(lambda num: print(num%2), list_of_numbers)

words = ["Apple", "Bat", "Juice", "fainT", "Ape", "Bolt", "Brother", "Taste", "parT", "crawL"]
words_ending_with_t = list(filter(lambda word: word.lower().endswith("t"), words))
print(words_ending_with_t)



