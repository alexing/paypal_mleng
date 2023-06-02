"""
2. Subsegment Sort
An array of n integers, arr[n] can be partitioned into any number of contiguous subsegments.
Every element must present in exactly 1 partition.
After partitioning, and without changing the order of partitions, sort each partition in non-descending order.
Concatenate the sorted partitions and compare the resulting array to the original array, sorted non-descending.
If the two match, the set of partitions is valid.
Find the maximum number of contiguous subsegments in which the array arr can be partitioned such that the set of
partitions is valid.



Example
    n = 6
    arr = [2, 5, 1, 9, 7, 6]

The array can be divided into 2 contiguous subsegments:
Subsegments -> [2, 5, 1], [9, 7, 6]
Sorted subsegments -> [1, 2, 5], [6, 7, 9]
Final array -> [1, 2, 5, 6, 7, 9]
As the final arr is sorted, 2 is a possible answer.

The array can be divided into 3 contiguous subsegments:
Subsegments -> [2, 5, 1], [9, 7], [6]
Sorted Subsegments -> [1, 2, 5], [7, 9], [6]
Final array -> [1, 2, 5, 7, 9, 6]
As the combined arr is not sorted, 3 can't be possible.

Any higher number of subsegments will fail as well. The answer is 2.

Function Description
The function is named findMaxSubsegmentsCount
findMaxSubsegmentsCount has the following parameter(s):
    int arr[n]:  the array of integers to partition
Returns
    int: the maximum number of contiguous subsegments in a valid set of partitions
Constraints

    1 ≤ n ≤ 105
    1 ≤ arr[i] ≤ 105
"""

from typing import List


def findMaxSubsegmentsCount(array: List[int]) -> int:
    n = len(array)

    # create two arrays: prefix_max and suffix_min, where prefix_max[i] is the maximum value in arr[0..i] 
    # and suffix_min[i] is the minimum value in arr[i..n-1]. Initialize them in 0.
    prefix_max = [0] * n
    suffix_min = [0] * n
    prefix_max[0] = array[0]
    suffix_min[n - 1] = array[n - 1]

    # compute prefix_max
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i - 1], array[i])

    # compute suffix_min
    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(suffix_min[i + 1], array[i])

    # count the number of valid subsegments
    valid_subsegments = 1
    for i in range(n - 1):
        if prefix_max[i] <= suffix_min[i + 1]:
            valid_subsegments += 1

    return valid_subsegments


if __name__ == "__main__":
    assert findMaxSubsegmentsCount([2, 5, 1, 9, 7, 6]) == 2
