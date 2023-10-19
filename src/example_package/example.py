import random

def hello_world():
    print('hello, world!')


def monte_carlo_integration(func, a, b, num_samples):
    """
    Compute the integral of a function using the Monte Carlo method.
    
    Parameters:
    - func: The function to be integrated.
    - a: The lower limit of the integration interval.
    - b: The upper limit of the integration interval.
    - num_samples: The number of random samples to use.

    Returns:
    - An estimate of the integral of the function.
    """
    total = 0
    for _ in range(num_samples):
        x = random.uniform(a, b)
        total += func(x)
    
    average = total / num_samples
    integral = (b - a) * average
    return integral
