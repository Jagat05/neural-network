# Perceptron Training for Gender Classification (Python)

## Introduction

A **Perceptron** is one of the simplest types of artificial neural networks used for **binary classification problems**. It learns by adjusting weights based on errors during training.

In this program, a perceptron model is trained using a dataset containing **Height and Weight** to classify a person as **Male or Female**.

---

## Objective

The objective of this program is to:

* Train a **Perceptron model** using the given training dataset.
* Classify gender based on **Height and Weight**.
* Predict the class for the inputs **(6, 82)** and **(5.3, 52)**.

---

## Training Dataset

| Height (x1) | Weight (x2) | Class  |
| ----------- | ----------- | ------ |
| 5.9         | 75          | Male   |
| 5.8         | 86          | Male   |
| 5.2         | 50          | Female |
| 5.4         | 55          | Female |
| 6.1         | 85          | Male   |
| 5.5         | 62          | Female |

For training the perceptron:

* **Male = 1**
* **Female = -1**

---

## Perceptron Formula

```text
Output = w1*x1 + w2*x2 + bias
```

Where:

* **x1** = Height
* **x2** = Weight
* **w1, w2** = Weights
* **bias** = Bias value

Weights are updated using the learning rule:

```text
w = w + learning_rate * target * input
```

---

## Program Logic

The program works in the following steps:

1. Store the **training dataset** containing height and weight.
2. Convert gender classes into numeric values (Male = 1, Female = -1).
3. Initialize weights and bias to **0**.
4. Train the perceptron for several **epochs** (iterations).
5. Update weights when the prediction is incorrect.
6. After training, use the learned weights to **predict new inputs**.

---

## Python Implementation

```python
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
```

---

## Example Output

```text
Prediction for (6,82): Male
Prediction for (5.3,52): Female
```
---

## Conclusion

This program demonstrates how a **Perceptron algorithm** can be trained using height and weight data to classify gender. After training, the model successfully predicts the class of new input samples using the learned weights.
