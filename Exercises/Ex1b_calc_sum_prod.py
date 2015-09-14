# Script to calculate the sum and product of numbers passed as arguments

import sys # Provides access to system level functionality
import numpy as np

args = sys.argv

num_args = [float(i) for i in args[1:]]

sum_args = np.sum(num_args)
prod_args = np.prod(num_args)

print('Sum: ', sum_args)
print('Product:', prod_args)
