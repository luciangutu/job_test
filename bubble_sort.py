def bubble_sort(arr: list) -> list:
    for _ in enumerate(arr):
        for index in range(len(arr)-1):
            next_value = arr[index+1]
            if arr[index] > arr[index+1]:
                arr[index + 1] = arr[index]
                arr[index] = next_value
    return arr


print(bubble_sort([4, 6, 8, 3, 1]))
print(bubble_sort([4, 6, 5, 4, 9]))
print(bubble_sort([]))


def bubble_sort_better(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubble_sort_better([4, 6, 8, 3, 1]))
print(bubble_sort_better([4, 6, 5, 4, 9]))
print(bubble_sort_better([]))
