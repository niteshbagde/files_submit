def my_Sqrtrt(x):
    if x == 0:
        return 0

    left, right = 1, x
    while left <= right:
        mid = (left + right) // 2 # getting round for remainder as single value
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return right

print(my_Sqrtrt(8))  
# Output: 2
