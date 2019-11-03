import sys
from timeit import default_timer as timer

def shell_sort(nums):
    h = 1
    n = len(nums)

    while h < n:
        h = 3 * h + 1

    while h > 0:
        for i in range(h, n):
            c = nums[i]
            j = i

            while j >= h and c < nums[j - h]:
                nums[j] = nums[j - h]
                j = j - h
                nums[j] = c
        h = int(h / 3)
        print(h)
    return nums

if __name__ == '__main__':
    all_times = []

    for _ in range(10):
        numbers_file = open(sys.argv[1], 'r')
        arr = [int(x) for x in numbers_file]
        numbers_file.close()

        start = timer()
        arr = shell_sort(arr)
        end = timer()

        all_times.append(end - start)

    print('{}\t{}'.format(len(arr), sum(all_times) / len(all_times)))
