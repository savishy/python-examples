# Problem: Given an array of size N, sort it in increasing order using selection sort.
# Solution (Algorithm)
# 
# 1. Select the minimum element of the array
# 2. Swap it with first element of array

# Pseudo Code:
# for an array of size N:
# go from 0 to N-1. find index of minimum element.
# swap min element with 0th element.
# go from 1 to N-1. find index of minimum element.
# swap min element with 1st element.
# ...
# go from N-2 to N-1. (etc. etc.)



def selectionSort(arr):
    N = len(arr)
    sorted = [0]*N


    # outer loop from 0 to N-2
    for i in range(0,N-2):

        min = 100000
        minIndex = 100000

        # inner loop
        for j in range(i,N):
            if arr[j] < min:
                min = arr[j]
                minIndex = j
        # swap minimum and first element.
        arr[minIndex] = arr[i]
        # set first element to minimum.
        arr[i] = min

        print(arr)

selectionSort([99, 11, 5, 55, 6])