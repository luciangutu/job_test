# https://www.youtube.com/watch?v=nxuXNU8n904

# nums = [2, 7, 11, 17]
nums = [2, 17, 11, 7]
target = 9

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)
            exit()



hash_table = {}
for i in range(len(nums)):
    difference = target - nums[i]
    if difference in hash_table:
        print([hash_table[difference], i])
        exit()
    hash_table[nums[i]] = i


