# Two Pointer pattern
mylist = [1, 5, 3, 7, 9, 4, 6]
print(f'Original list: {mylist}')

start = 0
end = len(mylist) - 1

while start < end:
    # Move the smaller elements to the start
    for i in range(start, end):
        if mylist[i] > mylist[i + 1]:
            mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]
    # After the first loop, the largest element is at the end
    end -= 1

    # Move the larger elements to the end
    for i in range(end, start, -1):
        if mylist[i] < mylist[i - 1]:
            mylist[i], mylist[i - 1] = mylist[i - 1], mylist[i]
    # After the second loop, the smallest element is at the start
    start += 1

print("Sorted list:", mylist)
