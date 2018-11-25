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

words_with_length_of_greater_than_3 = list(filter(lambda word: len(word) > 3, words))
print(words_with_length_of_greater_than_3)

def words_beginning_with_a_character(char):
    if len(char) > 1 or type(char) != str:
        error_message = "You need to enter a single character for the function. You have entered '%s'" % char
        raise ValueError(error_message)
    else:
        list_of_results = list(filter(lambda word: word.lower().startswith(char), words))
        if len(list_of_results) == 0:
            return "No results found"
        else:
            return list_of_results

print(words_beginning_with_a_character("a"))
print(words_beginning_with_a_character("z"))
print(words_beginning_with_a_character("aaz"))
print(words_beginning_with_a_character(4))



