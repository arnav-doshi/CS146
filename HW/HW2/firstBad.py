def firstBadVersion(n):
    left = 1
    right = n

    while right > left:
        midd = left + (right - left) // 2
        if isBadVersion(midd):
            right = midd
        else:
            left = midd+1
    return left

