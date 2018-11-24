print(2/1)
i = 0
# print(1/i) #error ZeroDivisionError

def run_division(to_divide, divider):
    try:
        print(to_divide//divider)
    except (ZeroDivisionError, ValueError):
        print(0)
    except ValueError:
        print(1)
    else: #executed when the whole code executes successfully
        print("else")
    finally:
        print("Process finished")

run_division(10,0)
run_division(10,1)

# print(2 + "2") #error TypeError

list_of_values = [1, "1", 11, 23, "23"]
# print(sum(list_of_values)) #error TypeError

# print(list_of_values.non_existing) #error AttributeError


##CUSTOM EXCEPTIONS

class Amount:

    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return repr((self.currency, self.amount))

    def add(self, that):
        if self.currency == that.currency:
           self.amount += that.amount
        else:
            raise CurrencyDoesNotMatchException(("%s, %s" % (self.currency,that.currency)))

class CurrencyDoesNotMatchException(Exception):

    def __init__(self, message):
        super().__init__(message)


money1 = Amount("EUR", 23)
money2 = Amount("EUR", 34)
money3 = Amount("USD", 10)
money4 = Amount("USD", 12)

money1.add(money2)
print(money1.amount)
money2.add(money3)
print(money2.amount)