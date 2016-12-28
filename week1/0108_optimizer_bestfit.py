"""
Used to find min value for function
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

# error computation function
# either abs(sum(err)) or sum(err^2)
# here the second approach was taken.
def error(line, data):
    err = np.sum( (data[:, 1] - (line[0] * data[:, 0] + line[1]) ) ** 2)
    return err

def run_this():
    # Define original line
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
    # line = fit_line(data, error)
    # print "Fitted lin"
    # plt.show()

if __name__ == "__main__":
    run_this()