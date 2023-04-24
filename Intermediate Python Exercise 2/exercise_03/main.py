import numpy as np

# Creating an array of 10 random floats
arr = np.random.rand(10)
mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)

# Use the print method to print the mean, median, and std
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)