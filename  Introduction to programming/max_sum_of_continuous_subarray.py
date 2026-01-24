"""Implement a function that returns the maximum sum of a continuous subarray whose length does not
exceed k. There is a list of integers a (can contain both positive and negative values) and an integer k.
Find the maximum possible sum of a subarray of length at most k, which consists of continuous elements.
Example:
Input: a = [1, -2, 3, 4, -1, 2], k = 3
Output: 7
Explanation: The subarray [3, 4] has a sum of 7, and length 2 ≤ 3.
Problem statement
The input is a list of integers (can be both positive and negative).
You need to find the maximum sum of a continuous subarray with a length from 1 to k inclusive.
If the list is empty or k < 1, return 0."""

def max_subarray_sum_limited(a, k):
    if not a:
        return 0
    if k <= 0:
        return 0
    max_sum = float('-inf')
    for i in range(len(a)):
        current_sum = 0
        for m in range(i, min(i + k, len(a))):
            current_sum += a[m]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum


print(max_subarray_sum_limited(a = [1, -2, 3, 4, -1, 2], k = 3)) #7
print(max_subarray_sum_limited(a = [4, -1, 2], k = 0)) #0
print(max_subarray_sum_limited(a = [], k = 3)) #0


