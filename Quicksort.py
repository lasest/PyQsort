"""
This module presents multiple implementations of  standart quicksort algorithm.
The main method is quicksort(). It returns either a list arr which is the sorted initial list, or a tuple (arr, logs).
Both iterative and recursive versions are present. Logging of the sorting process is implemented for iterative
version. Specify "log = True" as an argument to receive results as a tuple with logs list as its second element.
The i-th element in logs list shows the position of element arr[i] in the initial sequence.
The module uses a simple Stack class.
"""

import Stack


# Swap utility function without logging
def swap(a, b, data):
    data[a], data[b] = data[b], data[a]


# Swap utility function with logging
def swap_logged(a, b, data, logs):
    data[a], data[b] = data[b], data[a]
    logs[a], logs[b] = logs[b], logs[a]


# Partition function without logging
def partition(start, end, data):
    pivot = data[end]
    index = start
    for i in range(start, end):
        if data[i] < pivot:
            swap(i, index, data)
            index += 1
    swap(end, index, data)
    return index


# Partition function with logging
def partition_logged(start, end, data, logs):
    pivot = data[end]
    index = start
    for i in range(start, end):
        if data[i] < pivot:
            swap_logged(i, index, data, logs)
            index += 1
    swap_logged(end, index, data, logs)
    return index


# Recursive sort function
def recursive_sort(start, end, data):
    if start >= end:
        return

    index = partition(start, end, data)
    recursive_sort(start, index, data)
    recursive_sort(index + 1, end + 1, data)


# Iterative sort function
# Uses custom Stack class, which can be found in the current repository
def iterative_sort(start, end, data, log):
    if log:
        logs = list(range(len(data)))

    stack = Stack.Stack()

    stack.push(start)
    stack.push(end)

    while not stack.is_empty():
        end = stack.pop()
        start = stack.pop()

        if log:
            index = partition_logged(start, end, data, logs)
        else:
            index = partition(start, end, data)
        if index - 1 > start:
            stack.push(start)
            stack.push(index - 1)
        if index + 1 < end:
            stack.push(index + 1)
            stack.push(end)

    if log:
        return logs


# Main function of the module. Calls appropriate sort function based on the arguments passed to it.
def quicksort(arr, start=0, end=-1, recursive=True, log=False):
    logs = []
    if end == -1:
        end = len(arr) - 1

    if recursive:
        recursive_sort(start, end, arr)

    if not recursive:
        logs = iterative_sort(start, end, arr, log)

    if logs:
        return (arr, logs)
    else:
        return arr
