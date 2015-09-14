# Script to print out 10 random numbers from a normal distribution given an mean and standard deviation

x = commandArgs(trailingOnly = TRUE)

arg_mean = as.numeric(x[1])
arg_std = as.numeric(x[2])

values = rnorm(10, arg_mean, arg_std)

print(values)