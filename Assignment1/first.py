# 1.	Write a python program to create a neuron and 
# # predict its output using the threshold activation function.

# -->Neuron with Threshold Activation Function for n inputs

n = int(input("Enter number of inputs: "))

inputs = []
weights = []

# Taking inputs
for i in range(n):
    val = float(input(f"Enter input x{i+1}: "))
    inputs.append(val)

# Taking weights
for i in range(n):
    val = float(input(f"Enter weight w{i+1}: "))
    weights.append(val)

# Bias
b = float(input("Enter bias: "))

# Weighted sum
z = 0
for i in range(n):
    z += inputs[i] * weights[i]

z += b

# Threshold activation
if z >= 0:
    output = 1
else:
    output = 0

print("Weighted Sum =", z)
print("Neuron Output =", output)