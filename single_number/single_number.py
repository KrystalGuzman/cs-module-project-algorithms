'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# def single_number(arr):
#     for elem in arr:
#         if arr.count(elem) == 1:
#             return elem

# def single_number(arr):
#     #multiplies all different values by 2, then subtracts from sum
#     return 2 * sum(set(arr)) - sum(arr)

def single_number(arr):
    counts= {}
    for num in arr:

        if num in counts:
            # remove item
            del counts[num]
        else:
            #add item
            counts[num] = 1
    for k, v in counts.items():
        if v==1:
            return k




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")