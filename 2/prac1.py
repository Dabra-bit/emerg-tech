nums = input("Introduce los numeros: ")
nums = nums.split()
nums = list(map(lambda x: int(x), nums))

def cubes(l):
    return list(map(lambda x: x**3, l))

# First point
half = len(nums)//2
print(f"1: {nums[:half]} {nums[half:]}")

# Second point
print(f"2: {nums[0]} {nums[-1]}")

# Third point
first = nums[0]
second = nums[-1]
nums.append(first)
nums.append(second)
print(f"3: {nums}")

# Fourth point
nums.sort()
print(f"4: {nums}")

# Fifth point
nums = nums[::-1]
print(f"5: {nums}")

# Sixth point
cubedNums = cubes(l=nums)
print(f"6: {cubedNums}")