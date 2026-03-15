# 3.	Write a python program to implement Min-Max Scalar.
# Python program to implement Min-Max Scaling

# Sample dataset
data = [10, 15, 20, 25, 30]
  
# Step 1: find min and max
min_val = min(data)
max_val = max(data)

# Step 2: apply Min-Max formula
scaled_data = [(x - min_val) / (max_val - min_val) for x in data]

# Step 3: print results
print("Original Data:", data)
print("Scaled Data:", scaled_data)