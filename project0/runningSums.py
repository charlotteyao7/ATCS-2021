def runningSum(nums):
    newNums = []
    temp = 0
    for val in nums:
        temp += val
        newNums.append(temp)
    return newNums

arr = [1, 2, 3, 4]
print(runningSum(arr))
