# Script to calculate the sum and product of numbers passed as arguments

import sys # Provides access to system level functionality

# arguments passed to the script are stored in the argv attribute of sys as a list
# slicing the list returns just those arguments 
args = sys.argv[1:]

if len(args) == 0:
    prod_res = 0
    sum_res = 0 
else:
    prod_res = 1
    sum_res = 0 
    for arg in args:
        prod_res = prod_res * float(arg)
        sum_res = sum_res + float(arg)

print('Product: ', prod_res)
print('Sum: ', sum_res)

