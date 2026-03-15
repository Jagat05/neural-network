# Perceptron program for gender classification

# Training dataset: [Height, Weight]
X = [
    [5.9, 75],
    [5.8, 86],
    [5.2, 50],
    [5.4, 55],
    [6.1, 85],
    [5.5, 62]
]

# Target class (Male = 1, Female = -1)
y = [1, 1, -1, -1, 1, -1]

# Initialize weights and bias
w1 = 0
w2 = 0
bias = 0
learning_rate = 0.01

# Training perceptron
for epoch in range(100):
    for i in range(len(X)):
        x1, x2 = X[i]
        target = y[i]

        output = w1*x1 + w2*x2 + bias

        if target * output <= 0:
            w1 = w1 + learning_rate * target * x1
            w2 = w2 + learning_rate * target * x2
            bias = bias + learning_rate * target

# Prediction function
def predict(height, weight):
    result = w1*height + w2*weight + bias
    if result >= 0:
        return "Male"
    else:
        return "Female"

# Test inputs
print("Prediction for (6,82):", predict(6, 82))
print("Prediction for (5.3,52):", predict(5.3, 52))