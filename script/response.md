Here’s a simple Python function to generate the Fibonacci sequence using recursion:  

```python
def fibonacci_recursive(n):
    if n <= 0:
        return "Input must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
print(fibonacci_recursive(10))  # Output: 34
```

Alternatively, if you need a more efficient approach using iteration:  

```python
def fibonacci_iterative(n):
    if n <= 0:
        return "Input must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

# Example usage:
print(fibonacci_iterative(10))  # Output: 34
```

For generating a sequence instead of a single number:  

```python
def fibonacci_sequence(n):
    if n <= 0:
        return "Input must be a positive integer."
    
    sequence = [0, 1]
    for _ in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence[:n]

# Example usage:
print(fibonacci_sequence(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

Let me know if you need a different implementation! 🚀