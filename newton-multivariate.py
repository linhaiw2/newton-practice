import numpy as np



def newton_method_multivariate(f, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        grad = gradient(f, x)
        hess = hessian(f, x)
        try:
            dx = np.linalg.solve(hess, grad)
        except np.linalg.LinAlgError:
            print("Hessian is singular.")
            break
        x_new = x - dx
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    return x