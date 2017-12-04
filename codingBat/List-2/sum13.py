'''

Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6

'''

def sum13(nums):
  n = 0
  x = 0
  index = 0
  
  if len(nums) < 1:
    return 0
    
  for i in nums:
    if i == 13:
      index = nums.index(i)
      if index < len(nums)-1:
        nums[index] = 0
        nums[index+1] = 0
    else:
      n += i
  return (n - x)


