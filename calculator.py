# calculator.py

import numpy as np
import matplotlib.pyplot as plt

def add(a, b):
    """Adds two numbers."""
    return np.add(a, b)

def subtract(a, b):
    """Subtracts two numbers."""
    return np.subtract(a, b)

def multiply(a, b):
    """Multiplies two numbers."""
    return np.multiply(a, b)

def divide(a, b):
    """Divides two numbers, raises an error if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return np.divide(a, b)

def plot_function(x, y):
    """Plots x vs y using matplotlib."""
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Simple Plot')
    plt.show()
