import numpy as np
import sys
from time import time


def random_sample(size):
    np.random.seed(int(time()))
    return np.random.uniform(low=0, high=100 * size, size=size)

def repeated_sample(size):
    np.random.seed(int(time()))
    return np.random.normal(loc=(size // 2), scale=int(size * 0.010), size=size)

def inverted_almost_ordered(size, percent):
    ordered = almost_ordered(size, percent)
    ordered.reverse()
    return ordered

def inverted_75_ordered(size):
    return inverted_almost_ordered(size, .75)

def almost_ordered(size, percent):
    order_to = int(size * percent)
    ordered = [int(x) for x in range(order_to)]

    np.random.seed(int(time()))
    unordered = [int(x) for x in np.random.uniform(low=order_to, high=100 * size, size=(size - order_to))]

    return ordered + unordered

def ordered_75(size): return almost_ordered(size, .75)

def output_sample(sample, name):
    try:
        file = open(name, 'w')
        [file.write(str(int(value)) + '\n') for value in sample]
        file.close()
    except Exception as ex:
        print("Error")
        print(ex)


if __name__ == '__main__':
    sample_type = sys.argv[1]
    size = sys.argv[2]
    filename = sys.argv[3]

    if sample_type == 'random':
        output_sample(random_sample(int(size)), filename)

    if sample_type == 'repeated':
        output_sample(repeated_sample(int(size)), filename)

    if sample_type == 'ordered':
        output_sample(ordered_75(int(size)), filename)

    if sample_type == 'inverted':
        output_sample(inverted_75_ordered(int(size)), filename)

