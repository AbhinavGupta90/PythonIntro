import string
#LOOPS
from enum import Enum

letters = reversed(list(map(chr, range(ord('g'), ord('s')-1))))
numbers = []

for num in range(2, 20):
    numbers.append(num)


for index, number in enumerate(numbers):
    print("%s -> INDEX %s" % (number, index))

print(numbers)
print(list(letters))

#ENUM

class Currency(Enum):
    USD = 1
    EUR = 2
    PLN = 3
    NOK = 4

for currency in Currency:
    print(currency, currency.value)

print(Currency(2))

#METHODS AND ARGS

def example_method(mandatory, default="Default", *args, **kwargs):
    print("\n\n MANDATORY => %s\n DEFAULT => %s\n ARGS => %s\n KWARGS => %s" % (mandatory, default, args, kwargs))

example_method(15)
example_method(14,28)