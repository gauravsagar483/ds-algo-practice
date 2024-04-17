"""

Given an array of n integers. The problem is to find maximum length of the 
subsequence with difference between adjacent elements as either 0 or 1.

Input : arr[] = {2, 5, 6, 3, 7, 6, 5, 8}
Output : 5
The subsequence is {5, 6, 7, 6, 5}.

Input : arr[] = {-2, -1, 5, -1, 4, 0, 3}
Output : 4
The subsequence is {-2, -1, -1, 0}.
"""


def find_max(arr):
    hash = dict()

    for i in arr:
        i = int(i)
        hash[i] = 1

        if hash.get(i - 1, None) is not None or hash.get(i + 1, None) is not None:
            hash[i] = max(hash.get(i - 1, 0), hash.get(i + 1, 0)) + 1

    return max(hash.values())


arr = [-2, -1, 5, -1, 4, 0, 3]
print(find_max(arr))

# Wohooo
