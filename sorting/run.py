#!/usr/bin/env python3
"""Sorting algorithms demo — MITx 6.00.1x."""

import sys
sys.path.insert(0, ".")
from mergeSort import mergeSort
from bubbleSort import bubble_sort

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 33, 17]
    print("MITx 6.00.1x — Sorting demo")
    print("Input: ", data)
    m = mergeSort(list(data))
    b = list(data)
    bubble_sort(b)
    print("mergeSort:", m)
    print("bubbleSort:", b)
