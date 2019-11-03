from matplotlib import pyplot as plt
from collections import Counter

file = open('samples/repeated/sample-10', 'r')
data = [int(x) for x in file]
file.close()

counter = Counter(data)
plt.plot([k for k in counter.keys()], [x for x in counter.values()], '.')
plt.show()
