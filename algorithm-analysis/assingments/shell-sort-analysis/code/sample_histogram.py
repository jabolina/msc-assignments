from matplotlib import pyplot as plt
from collections import Counter
import sys


def plot(data):
    counter = Counter(data)
    plt.plot([k for k in counter.keys()], [x for x in counter.values()], '.')
    plt.show()


if __name__ == '__main__':
    type = sys.argv[1]
    sample = sys.argv[2]

    file = open('samples/' + type + '/sample-' + sample, 'r')
    data = [int(x) for x in file]
    file.close()

    plot(data)


