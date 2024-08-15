import matplotlib.pyplot as plt
import numpy as np


def bubble_sort_visualization(arr):
    n = len(arr)
    fig, ax = plt.subplots()

    for i in range(n):
        for j in range(0, n-i-1):
            ax.bar(range(n), arr, color=['lightblue' if x == j or x == j+1 else 'blue' for x in range(n)])

            plt.pause(0.1)
            plt.draw()

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

        ax.bar(range(n), arr, color='lightgreen')


arr = np.random.randint(0, 101, 10)
bubble_sort_visualization(arr)
