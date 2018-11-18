from fstring import fstring

def print_multiplication_table(table, start=1, end=10):
    print("NEW EXECUTION")
    for i in range(start, end+1):
        print (fstring("{table} X {i} = {table*i}"))

# print_multiplication_table(2, 1, 11)
# print_multiplication_table(12, 1, 13)
# print_multiplication_table(10)

def multiply_up_to_three_values(val1=1, val2=1, val3=1):
    result = val1*val2*val3
    return result

print(multiply_up_to_three_values(2,3)) #should equal 6
print(multiply_up_to_three_values(1,4,9)) #should equal 36

