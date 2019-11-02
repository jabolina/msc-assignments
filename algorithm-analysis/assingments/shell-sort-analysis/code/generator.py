import numpy as np
import sys
from time import time


def random_sample(size):
    np.random.seed(int(time()))
    return np.random.uniform(low=0, high=100 * size, size=size)

def repeated_sample(size):
    np.random.seed(int(time()))
    return np.random.normal(loc=(size // 2), size=size)

def almost_ordered(size, percent):
    order_to = int(size * percent)
    ordered = [int(x) for x in range(order_to)]

    np.random.seed(int(time()))
    unordered = [int(x) for x in np.random.uniform(low=order_to, high=100 * size, size=(size - order_to))]

    return ordered + unordered

def ordered_75(size): return almost_ordered(size, .75)

def output_sample(sample, name):
    file = open(name, 'w')
    [file.write(str(int(value)) + '\n') for value in sample]
    file.close()


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

