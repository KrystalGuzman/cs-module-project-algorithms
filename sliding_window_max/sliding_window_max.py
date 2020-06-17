'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # hold maxes for each window.
    total_maxes = len(nums) - k + 1
    maxes = [None] * total_maxes

    # calculate max for each window
    for i in range(total_maxes):

        lower_bound = i
        upper_bound = i + (k - 1)

        maxes[i] = max(nums[lower_bound:upper_bound + 1])

    return maxes


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
