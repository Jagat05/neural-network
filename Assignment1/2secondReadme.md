# Training AND Gate Using Perceptron Learning Algorithm

## Introduction

A **Perceptron** is the simplest type of artificial neural network. It works like a single artificial neuron that receives multiple inputs, processes them using weights and bias, and produces an output using an activation function.

The perceptron learns by adjusting its **weights** and **bias** based on errors. This learning process is called the **Perceptron Learning Algorithm (PLA)**.

In this program, we train a perceptron to learn the behavior of an **AND logic gate**.

---

# Basics of a Perceptron

A perceptron has the following components:

### 1. Inputs
Values given to the neuron.

Example:

x1, x2


### 2. Weights
Each input has a weight that determines its importance.


w1, w2


### 3. Bias
A constant value added to the weighted sum to shift the decision boundary.


b


### 4. Weighted Sum

The perceptron calculates:


z = x1w1 + x2w2 + b


### 5. Activation Function (Threshold)

The activation function decides the final output.


if z >= 0 → output = 1
else → output = 0


---

# AND Gate Logic

The AND gate produces output **1 only when both inputs are 1**.

| x1 | x2 | Output |
|----|----|-------|
| 0  | 0  | 0 |
| 0  | 1  | 0 |
| 1  | 0  | 0 |
| 1  | 1  | 1 |

Our goal is to train the perceptron so that it correctly predicts this output.

---

# Perceptron Learning Algorithm (PLA)

The perceptron learns using the following steps:

1. Initialize weights and bias to 0.
2. For each training example:
   - Calculate weighted sum.
   - Apply activation function.
   - Compare predicted output with expected output.
3. If prediction is wrong, update weights and bias.

Weight update rule:


w_new = w_old + learning_rate * (expected - predicted) * input


Bias update rule:


b_new = b_old + learning_rate * (expected - predicted)


The process repeats until all predictions are correct.

---

# Python Implementation

The program performs the following tasks:

1. Define training data for the AND gate.
2. Initialize weights and bias.
3. Apply the perceptron learning algorithm.
4. Update weights when errors occur.
5. Stop training when the perceptron correctly predicts all outputs.

---

# Example Output


Training complete!

Testing AND Gate Perceptron:

- Input: [0,0] → Output: 0
- Input: [0,1] → Output: 0
- Input: [1,0] → Output: 0
- Input: [1,1] → Output: 1


This shows that the perceptron has successfully learned the AND gate.

---

# Conclusion

The perceptron learning algorithm adjusts weights and bias until the model produces the correct outputs. In this program, the perceptron successfully learns the AND gate logic through iterative training.

---

# Author
Jagat Joshi