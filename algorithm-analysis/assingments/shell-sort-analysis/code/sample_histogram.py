from matplotlib import pyplot as plt
from collections import Counter
import sys


def gen_x_y(counter):
    values = [x for x in counter.keys()]
    greater = max(values)
    return ([counter[k] for k in range(greater)], [v for v in range(greater)])


def plot(data):
    (y, x) = gen_x_y(Counter(data))
    plt.plot(x, y, '-')
    plt.show()


if __name__ == '__main__':
    type = sys.argv[1]
    sample = sys.argv[2]

    file = open('samples/' + type + '/sample-' + sample, 'r')
    data = [int(x) for x in file]
    file.close()

    plot(data)


