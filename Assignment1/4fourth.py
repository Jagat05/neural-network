# 4.	Write a python program to implement Standard Scalar.
# Python program to implement Standard Scaler

import math

# Sample dataset
data = [10, 15, 20, 25, 30]

# Step 1: calculate mean
mean = sum(data) / len(data)

# Step 2: calculate standard deviation
variance = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = math.sqrt(variance)

# Step 3: apply Standard Scaling formula
scaled_data = [(x - mean) / std_dev for x in data]

# Step 4: print results
print("Original Data:", data)
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Standard Scaled Data:", scaled_data)