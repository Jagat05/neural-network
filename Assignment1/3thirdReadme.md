# Min-Max Scaling in Python

## Introduction

**Min-Max Scaling**, also called **Normalization**, is a technique in machine learning used to **rescale data into a fixed range**, usually `[0,1]`.  

Machine learning algorithms often perform better when input features are on the **same scale**, because large differences in magnitude can dominate learning.  

---

## Objective

The objective of this program is to implement **Min-Max Scaling** in Python to normalize a dataset using the Min-Max formula.

---

## Min-Max Scaling Formula

The formula used for Min-Max Scaling is:

```
x' = (x - xmin) / (xmax - xmin)
```

Where:

* **x** = Original value
* **xmin** = Minimum value in the dataset
* **xmax** = Maximum value in the dataset
* **x'** = Scaled value between 0 and 1

---

## Program Logic

The program follows these steps:

1. Define a sample dataset.
2. Find the **minimum** and **maximum** values in the dataset.
3. Apply the **Min-Max scaling formula** to each value.
4. Store the scaled values in a new list.
5. Print the original and scaled datasets.

---

## Python Implementation

```python
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
```

---

## Example Output

```
Original Data: [10, 15, 20, 25, 30]
Scaled Data: [0.0, 0.25, 0.5, 0.75, 1.0]
```

---

## Conclusion

Min-Max Scaling is a simple yet powerful technique for **normalizing data**.
This Python program demonstrates how raw numerical data can be transformed into a standardized range, making it more suitable for data analysis and machine learning applications.

# Author
Jagat Joshi