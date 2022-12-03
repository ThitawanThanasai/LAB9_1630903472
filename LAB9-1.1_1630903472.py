def lin_search(nums, item):
    for i in range(len(nums)):
        if nums[i] == item:
            return i
    return None

nums = [7,10,12,14,16,20,29,37]
item = 14
index = lin_search(nums, item)
if index != None:
    print("Item found at index", index)
else:
    print("Item not found")
item = 29
index = lin_search(nums, item)
if index != None:
    print("Item found at index", index)
else:
    print("Item not found")