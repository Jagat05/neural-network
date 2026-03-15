# Standard Scaler Implementation in Python

## Introduction

In data preprocessing, **feature scaling** is an important step used to normalize numerical data before applying machine learning algorithms. One commonly used method is **Standard Scaling (Standard Scaler)**.

Standard Scaling transforms data so that it has a **mean of 0** and a **standard deviation of 1**. This process is also known as **standardization**. It helps machine learning models perform better by ensuring that all features are on a similar scale.

---

## Standard Scaling Formula

```
z = (x - μ) / σ
```

Where:

* **x** = Original value
* **μ (mu)** = Mean of the dataset
* **σ (sigma)** = Standard deviation of the dataset
* **z** = Standardized value

---

## Program Logic

The program follows these steps:

1. Define a sample dataset.
2. Calculate the **mean** of the dataset.
3. Compute the **variance** of the dataset.
4. Calculate the **standard deviation** using the square root of variance.
5. Apply the **standard scaling formula** to each value.
6. Store the standardized values in a new list.
7. Display the original and scaled data.

---

## Python Implementation

```python
# Python program to implement Standard Scaler

import math

# Sample dataset
data = [10, 15, 20, 25, 30]

# Step 1: calculate mean
mean = sum(data) / len(data)

# Step 2: calculate variance
variance = sum((x - mean) ** 2 for x in data) / len(data)

# Step 3: calculate standard deviation
std_dev = math.sqrt(variance)

# Step 4: apply Standard Scaling formula
scaled_data = [(x - mean) / std_dev for x in data]

# Step 5: print results
print("Original Data:", data)
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Standard Scaled Data:", scaled_data)
```

---

## Example Output

```
Original Data: [10, 15, 20, 25, 30]
Mean: 20.0
Standard Deviation: 7.0710678118654755
Standard Scaled Data: [-1.414, -0.707, 0.0, 0.707, 1.414]
```

---

## Conclusion

Standard Scaling is an essential technique in data preprocessing. By transforming data to have a mean of 0 and standard deviation of 1, it ensures that all features contribute equally to machine learning models. This Python implementation demonstrates a simple way to standardize numerical data using basic mathematical operations.
