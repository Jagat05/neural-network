# Training data (inputs + expected output)
training_data = [
([0,0],0),
([0,1],0),
([1,0],0),
([1,1],1)
]

# Initialize weights and bias
weights = [0,0]
bias = 0
learning_rate = 1

# Activation function
def activation(z):
    if z >= 0:
        return 1
    else:
        return 0


epoch = 0

# Training loop
while True:

    epoch += 1
    print("\nEpoch",epoch)

    error_count = 0

    for inputs, expected in training_data:

        # Calculate weighted sum
        z = weights[0]*inputs[0] + weights[1]*inputs[1] + bias

        # Predicted output
        output = activation(z)

        # Error calculation
        error = expected - output

        # Update weights if wrong
        if error != 0:

            weights[0] = weights[0] + learning_rate*error*inputs[0]
            weights[1] = weights[1] + learning_rate*error*inputs[1]

            bias = bias + learning_rate*error

            error_count += 1

        print("Inputs:",inputs,
              "Z:",z,
              "Output:",output,
              "Weights:",weights,
              "Bias:",bias)

    if error_count == 0:
        print("\nTraining Complete")
        break


# Testing the trained perceptron
print("\nTesting AND Gate")

for inputs, expected in training_data:

    z = weights[0]*inputs[0] + weights[1]*inputs[1] + bias
    output = activation(z)

    print("Input:",inputs,"Output:",output)