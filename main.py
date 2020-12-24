import random

randomlist = random.sample(range(1, 9999999), 1000000)    # generate 10 random numbers between 1 and 99

print(randomlist)



'''
def insertion_sort(mylist):
    for i in range (1, len(mylist)):
        key = mylist[i]

        j = i - 1
        while j >= 0 and mylist[j] > key:
            mylist[j + 1] = mylist[j]
            j = j - 1
        mylist[j + 1] = key

insertion_sort(randomlist)
print(randomlist)
'''
'''
def mergesort(mylist):
    if len(mylist) > 1:                         # check array size is greater than 1
        mid = len(mylist) // 2
        left = mylist[:mid]                     # from start to mid
        right = mylist[mid:]                    # from mid to end

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                mylist[k] = left[i]
                i += 1
            else:
                mylist[k] = right[j]
                j += 1

            k += 1
        while i < len(left):
            mylist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            mylist[k] = right[j]
            j += 1
            k += 1


mergesort(randomlist)
print(randomlist)
'''
'''
def heapify(mylist, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if (left < n and mylist[i] < mylist[left]):                         # check if there is a left child and greater than
        largest = left                                                  # rooted index

    if (right < n and mylist[largest] < mylist[right]):                 # check if there is a right child and greater than
        largest = right                                                 # rooted index

    if (largest != i):
        mylist[i], mylist[largest] = mylist[largest], mylist[i]         # exchange mylist[i] and mylist[largest]

        heapify(mylist, n, largest)

def heapSort(mylist):
    n = len(mylist)

    for i in range(n, -1, -1):
        heapify(mylist, n, i)

    for i in range(n - 1, 0, -1):
        mylist[i], mylist[0] = mylist[0], mylist[i]                     # exchange mylist[i] with mylist[0]
        heapify(mylist, i, 0)

heapSort(randomlist)
print(randomlist)
'''
'''
def partition (mylist, lower, upper):
    pivotindex = mylist[upper]                                                   # pivot variable is = to end of list
    i = (lower - 1)

    for x in range(lower, upper):
        if mylist[x] < pivotindex:
            i += 1

            mylist[i], mylist[x] = mylist[x], mylist[i]

    mylist[i + 1], mylist[upper] = mylist[upper], mylist[i + 1]
    return i+1

def quicksort (mylist, lower, upper):
    if (lower < upper):
        q = partition(mylist, lower, upper)
        quicksort (mylist, lower, q - 1)                                    # lower bound is sorted
        quicksort (mylist, q + 1, upper)                                    # upper bound is sorted


quicksort (randomlist, 0, len(randomlist) - 1)
print(randomlist)
'''
'''
def random_quicksort (mylist, lower, upper):
    if (lower < upper):
        q_index = random_partition(mylist, lower, upper)
        random_quicksort(mylist, lower, q_index - 1)
        random_quicksort(mylist, q_index + 1, upper)

def random_partition(mylist, lower, upper):
    random_pivot = random.randrange(lower, upper)
    mylist[lower], mylist[random_pivot] = mylist[random_pivot], mylist[lower]
    return somepartition(mylist, lower, upper)

def somepartition(mylist, lower, upper):
    pivot = lower
    i = lower + 1

    for j in range (lower + 1, upper + 1):
        if mylist[j] <= mylist[pivot]:

            mylist[i], mylist[j] = mylist[j], mylist[i]
            i += 1
    mylist[pivot], mylist[i - 1] = mylist[i - 1], mylist[pivot]
    pivot = i - 1
    return pivot

random_quicksort(randomlist, 0, len(randomlist) - 1)
print(randomlist)
'''

def countingSort(mylist, place):
    size = len(mylist)

    output = [0] * size                                 # where the sorted array will be placed

    count = [0] * 10                                    # start array count at 0

    for i in range(0, size):                            # goes through array and counts elements
        index = mylist[i] // place
        count[index % 10] += 1

    for i in range(1, 10):                              # counts the position of the digit
        count[i] += count[i - 1]


    i = size - 1
    while i >= 0:
        index = (mylist[i] // place)
        output[count[index % 10] - 1] = mylist[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):                            # makes a copy of the elements
        mylist[i] = output[i]


def radixsort(mylist):

    maxelements = max(mylist)

    # countingSort
    place = 1
    while maxelements // place > 0:
        countingSort(mylist, place)
        place *= 10


radixsort(randomlist)
print(randomlist)
