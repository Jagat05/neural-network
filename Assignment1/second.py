# Write a python program to train AND Gate Using Perceptron Learning Algorithm.
# Perceptron Learning Algorithm to Train AND Gate

# Training data for AND gate
training_inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Expected outputs for AND gate
expected_outputs = [0, 0, 0, 1]

# Initialize weights and bias
weights = [0, 0]  # one weight for each input
bias = 0
learning_rate = 1  # step size for updates

# Activation function (threshold)
def activation(z):
    return 1 if z >= 0 else 0

# Training loop
epoch = 0
while True:
    epoch += 1
    print(f"\nEpoch {epoch}")
    error_count = 0  # count how many predictions are wrong in this epoch
    
    for inputs, expected in zip(training_inputs, expected_outputs):
        # Compute weighted sum
        z = sum(w*x for w, x in zip(weights, inputs)) + bias
        
        # Compute predicted output
        output = activation(z)
        
        # Compute error
        error = expected - output
        
        # Update weights and bias if prediction is wrong
        if error != 0:
            weights = [w + learning_rate * error * x for w, x in zip(weights, inputs)]
            bias += learning_rate * error
            error_count += 1
        
        print(f"Inputs: {inputs}, Weighted sum: {z}, Output: {output}, Weights: {weights}, Bias: {bias}")
    
    # Stop training if all outputs are correct
    if error_count == 0:
        print("\nTraining complete!")
        break

# Testing the trained perceptron
print("\nTesting AND Gate Perceptron:")
for inputs in training_inputs:
    z = sum(w*x for w, x in zip(weights, inputs)) + bias
    output = activation(z)
    print(f"Input: {inputs}, Output: {output}")