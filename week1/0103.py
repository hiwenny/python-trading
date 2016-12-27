import numpy as np
import time

def print_array():
    print np.array([(2, 3, 4), (5, 6, 7)])
    print np.empty(5)
    print np.empty((5, 4))
    print np.ones((8, 2))
    print np.ones((2, 2), dtype=np.int)

def print_rand_array():
    print np.random.random((6, 2))
    print np.random.rand(3, 4)

def print_dist_array():
    print np.random.normal(size=(4, 2))
    print np.random.normal(0, 10, size=2)
    print np.random.normal(0, 10, 5)
    print np.random.normal(50, 10, (4, 3))# normal with mean 50, stddev 10
    print np.random.normal(50, 10, size=(1, 10))# normal with mean 50, stddev 10

def print_array_shape():
    a = np.random.random((2, 3))
    print a
    print a.shape
    print a.shape[1]
    print len(a.shape)
    print a.size

def make_array():
    np.random.seed(321) # with seed the random is same everytime
    a = np.random.randint(0, 10, size=(4, 2))
    print "Array:\n", a
    print "Sum of all elements:", a.sum()
    print "Sum of each row: ", a.sum(axis=1)
    print "Sum of each col: ", a.sum(axis=0)
    print "Min, mean, max etc can also be used per-row or col e.g. ", a.mean(axis=1)

def get_max_index(a):
    """Return the index of the maximum value in given 1D array."""
    return a.argmax()

def test_run():
    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32-bit integer array
    print "Array:", a
    # Find the maximum and its index in array
    print "Maximum value:", a.max()
    print "Index of max.:", get_max_index(a)

if __name__ == "__main__":
    t1 = time.time()
    # print_array()
    # print_dist_array()
    # print_array_shape()
    # make_array()
    test_run()
    t2 = time.time()
    print t2-t1