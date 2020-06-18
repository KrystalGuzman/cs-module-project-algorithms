'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# def sliding_window_max(nums, k):
#     # Your code here
#     # For loop up to k times for the window
#     # loop over everything
#     maximums = []
#     for i in range(len(nums)-k+1):
#         max = nums[i]
#         for j in range(i, i + k):
#             if(j < len(nums) and max < nums[j]):
#                 max = nums[j]
#         maximums.append(max)

#     return maximums


# def sliding_window_max(nums, k):
#     # hold maxes for each window.
#     total_maxes = len(nums) - k + 1
#     maxes = [None] * total_maxes

#     # calculate max for each window
#     for i in range(total_maxes):

#         lower_bound = i
#         upper_bound = i + (k - 1)

#         maxes[i] = max(nums[lower_bound:upper_bound + 1])

#     return maxes

def sliding_window_max(nums, k):
    # n = len(nums)
    # if n * k == 0:
    #     return []

    # # O(nk) in the worst case of sorted descending array
    # # O(n) in the best case of sorted ascending array
    # output = []
    # max_idx = -1
    # for i in range(n - k + 1):
    #     # max_idx is out of sliding window
    #     if max_idx < i:
    #         max_idx = i
    #         for j in range(i, i + k):
    #             if nums[j] > nums[max_idx]: 
    #                 max_idx = j
    #     # max element is smaller than the last 
    #     # element in the window
    #     elif nums[max_idx] < nums[i + k - 1]: 
    #         max_idx = i + k - 1
    #     output.append(nums[max_idx])
    # return output

    # if not nums:
    #     return []
    # arr, out = nums[:k], []
    # curr = max(arr)
    # for i in range(len(nums) - k):
    #     out.append(curr)
    #     arr[i%k] = nums[i+k]
    #     curr = max(curr, nums[i+k]) if (curr != nums[i]) else max(arr)
    # out.append(curr)
    # return out

    # if not nums:
    #     return []
    # # Find max number (maxN) in first k elements
    # maxN = max(nums[:k])
    # # Store maxN index as maxPos
    # maxPos = nums[:k].index(maxN)
    # ans = [maxN]
    # i = k
    # step = k - 1
    # for i in range(k, len(nums)):
    #     # If new number > maxNum, store new maxN and maxPos
    #     if nums[i] > maxN:
    #         maxN, maxPos = nums[i], i
    #     # If window doesn't contain maxN anymore: i - step >= maxPos
    #     elif i - step >= maxPos:
    #         # Find new maxN and maxPos from what we currently have in the window
    #         arr = nums[i - step:i + 1]
    #         maxN = max(arr)
    #         maxPos = i - step + arr.index(maxN)
    #     # On each iteration add maxN to the answers
    #     ans.append(maxN)
    # return ans


    if k<2:
        return nums
            
    # Find max of first window
    mx = max(nums[:k])
    m = [mx]
    for i in range(len(nums)-k):
        # If number before window is max, compute new max
        if nums[i]==mx:
            mx=max(nums[i+1:i+k])
        # If rightmost number > max, set max to 
        if nums[i+k]>mx:
            mx=nums[i+k]
        m.append(mx)
    return m


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
