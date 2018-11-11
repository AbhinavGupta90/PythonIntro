from fstring import fstring

def print_multiplication_table(table, start, end):
    for i in range(start, end+1):
        print (fstring("{table} X {i} = {table*i}"))

print_multiplication_table(2, 1, 11)