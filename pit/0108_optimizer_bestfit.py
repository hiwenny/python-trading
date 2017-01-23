"""
Used to find min value for function
Will also work for polys, awesome!
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

# error computation function
# either abs(sum(err)) or sum(err^2)
# here the second approach is taken.
def error(line, data):
    err = np.sum( (data[:, 1] - (line[0] * data[:, 0] + line[1]) ) ** 2)
    return err

def fit_line(data, error_func):
    # Generate initial guess for line model
    l = np.float32([0, np.mean(data[:, 1])]) # slope=0, intercept=mean(y values)

    # Plot initial guess
    x_ends = np.float32([-5, 5])
    plt.plot(x_ends, l[0] * x_ends + l[1], 'm--', linewidth=2.0, label="Initial guess")

    # Call optimizer to minimize error function
    # args=(data,) is not typo, it is so that we can pass args to it - see docs.
    result = spo.minimize(error_func, l, args=(data,), method='SLSQP', options={'disp': True})
    return result.x

def run_this_for_linear():
    # Define original line starting point
    lamb_orig = np.float32([4, 2])
    print("Original line: C0 = {}, C1 = {}".format(lamb_orig[0], lamb_orig[1]))
    X_orig = np.linspace(0, 10, 21)
    Y_orig = lamb_orig[0] * X_orig + lamb_orig[1]
    plt.plot(X_orig, Y_orig, 'b--', linewidth=2.0, label="Original line")

    # Generate noisy datapoints
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Y_orig.shape)
    data = np.asarray([X_orig, Y_orig + noise]).T
    plt.plot(data[:, 0], data[:, 1], 'go', label="Data points")

    # Line fitting
    line = fit_line(data, error)
    print ("Fitted line: C0 = {}, C1 = {}".format(line[0], line[1]))
    plt.plot(data[:, 0], line[0] * data[:, 0] + line[1], 'r--', linewidth=2.0, label="LOBF")
    plt.show()

# def error_poly(C, data):
#     err = np.sum((data[:, 1] - np.polyval(C, data[:, 0])) ** 2)
#     return err
#
# def fit_poly(data, error_func, degree=3):
#     # Initial guess
#     Cguess = np.poly1d(np.ones(degree+1, dtype=np.float32))
#
#     # Plot initial guess
#     x = np.linspace(-5, 5, 21)
#     plt.plot(x, np.polyval(Cguess, x), 'm--', linewidth=2.0, label="Initial guess")
#
#     # Call optimizer to min err func
#     res = spo.minimize(error_func, Cguess, args=(data,), method='SLSQP', options={'disp': True})
#     return np.poly1d(res.x)

if __name__ == "__main__":
    run_this_for_linear()
