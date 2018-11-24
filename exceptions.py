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
    finally:
        print("Process finished")

run_division(10,0)
run_division(10,1)


# print(2 + "2") #error TypeError

list_of_values = [1, "1", 11, 23, "23"]
# print(sum(list_of_values)) #error TypeError

# print(list_of_values.non_existing) #error AttributeError





