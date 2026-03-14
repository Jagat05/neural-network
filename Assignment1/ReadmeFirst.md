# Understanding a Neuron and Threshold Activation Function

## Basics of a Neuron
A **neuron** is the fundamental unit of a neural network. It receives multiple inputs, applies weights to them, adds a bias, and produces an output using an **activation function**.  

Key components of a neuron:

1. **Inputs (x₁, x₂, …, xₙ)**  
   Signals received from the environment or previous layer.  

2. **Weights (w₁, w₂, …, wₙ)**  
   Each input has a weight that determines its influence on the output.  

3. **Bias (b)**  
   A constant that allows the neuron to shift the activation threshold.  

4. **Weighted Sum (z)**  
   The neuron calculates the total input using:  
   ### z = x1w1 + x2w2 + ... + xn*wn + b

   
5. **Activation Function**  
Determines the output based on the weighted sum. Examples include sigmoid, ReLU, and threshold functions.  

---

## About This Program
This Python program simulates **a single neuron** using a **threshold activation function**. The program:

1. Asks the user for the number of inputs (`n`).  
2. Takes the input values and their corresponding weights.  
3. Accepts a bias value.  
4. Computes the **weighted sum** of inputs plus bias.  
5. Applies the **threshold activation function**:  
- Output = 1 if weighted sum ≥ 0  
- Output = 0 if weighted sum < 0  
6. Prints the **weighted sum** and the **neuron output**.

---

Enter number of inputs: 3
Enter input x1: 1
Enter input x2: 0
Enter input x3: 1
Enter weight w1: 0.5
Enter weight w2: -0.6
Enter weight w3: 0.8
Enter bias: -0.1

## Example Usage
Weighted Sum = 1.2
Neuron Output = 1


---


## Author
Jagat Joshi

## License
This project is open-source and free to use.