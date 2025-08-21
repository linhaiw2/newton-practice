def first_derivative(f, x, eps=1e-5):
    return (f(x + eps) - f(x - eps)) / (2 * eps) # good!

def second_derivative(f, x, eps=1e-5):
    return (f(x + eps) - 2 * f(x) + f(x - eps)) / (eps ** 2) # good!

def newton_method(f, x0, eps=1e-5, max_iter = 100, tol = 1e-6):
    """
    Parameters:
    ___________
    f: function to minimize
    x0: starting value to estimate
    max_iter: maximum number to iterate
    tol: maximum difference between x_new and x

    Returns:
    ________
    x: estimated local min/max

    """
    x = x0
    for i in range(max_iter):
        f_prime = first_derivative(f, x, eps)
        f_double_prime = second_derivative(f, x, eps)

        if f_double_prime == 0:
            print("Stop Iteration")

            break
        x_new = x - f_prime / f_double_prime

        if abs(x_new - x) < tol:
            return x_new  # Converged

        x = x_new

    return x
    """
    Newton strategy:
    functions:
    1st derivative
    2nd derivative
    parameters:
    x0: starting value
    ...
    """

        