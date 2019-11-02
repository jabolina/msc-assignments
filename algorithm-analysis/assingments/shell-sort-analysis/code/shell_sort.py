from timeit import default_timer as timer

def shell_sort(nums):
    h = 1
    n = len(nums)

    while h > 0:
        for i in range(h, n):
            c = nums[i]
            j = i

            while j >= h and c < nums[j - h]:
                nums[j] = nums[j - h]
                j = j - h
                nums[j] = c
            h = h // 2.2
    return nums

def __name__ == '__main__':
    numbers_file = open(sys.argv[1], 'r')
    arr = [int(x) for x in numbers_file]
    numbers_file.close()

   start = timer()
   shell_sort(arr)
   end = timer()

   print('{}\t{}'.format(len(arr), (end - start))
