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
    print("\n\n MANDATORY => %s type{%s}\n DEFAULT => %s type{%s}\n ARGS => %s type{%s}\n KWARGS => %s type{%s}"
          % (mandatory, type(mandatory), default, type(default), args, type(args), kwargs, type(kwargs)))

example_method(15)
## MANDATORY => 15 DEFAULT => Default ARGS => () KWARGS => {}

example_method(14,28, "el1", "el2", "el4", "el3")
## MANDATORY => 14 DEFAULT => 28 ARGS => ('el1', 'el2', 'el4', 'el3') KWARGS => {}

example_method(120, "string1", "string2", "string3", "string4", name="Blazej", surname="Wielk", eng_equiv_name="Blaise")
## MANDATORY => 120 type{<class 'int'>}
## DEFAULT => string1 type{<class 'str'>}
## ARGS => ('string2', 'string3', 'string4') type{<class 'tuple'>}
## KWARGS => {'name': 'Blazej', 'eng_equiv_name': 'Blaise', 'surname': 'Wielk'} type{<class 'dict'>}

example_method(name="John", surname="McT", initials="AJM", mandatory=29, default="Twenty")
## MANDATORY => 29 type{<class 'int'>}
## DEFAULT => Twenty type{<class 'str'>}
## ARGS => () type{<class 'tuple'>}
## KWARGS => {'name': 'John', 'surname': 'McT', 'initials': 'AJM'} type{<class 'dict'>}

example_method(1992, *("seal", "fish", "dolphin", "sealion", "walrus"))
## MANDATORY = > 1992 type{ <class 'int'>}
## DEFAULT = > seal type{< class 'str' >}
## ARGS = > ('fish', 'dolphin', 'sealion', 'walrus') type{< class 'tuple' >}
## KWARGS = > {} type{< class 'dict' >}

example_method(1992,("seal", "fish", "dolphin", "sealion", "walrus"))
## MANDATORY => 1992 type{<class 'int'>}
## DEFAULT => seal type{<class 'str'>}
## ARGS => ('fish', 'dolphin', 'sealion', 'walrus') type{<class 'tuple'>}
## KWARGS => {} type{<class 'dict'>}