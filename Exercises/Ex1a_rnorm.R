# Script to print out 10 random numbers from a normal distribution given an mean and standard deviation

args <- commandArgs(trailingOnly = TRUE)

mean <- as.numeric(args[1])
stdev <- as.numeric(args[2])

samples <- rnorm(10, mean, stdev)

print(samples)
