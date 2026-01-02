def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i):
            if nums[i]+nums[j]==target:
                print(j,i)
                break

nums=[3,3]
target=6
twoSum(nums,target)