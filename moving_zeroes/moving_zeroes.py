'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # finds position in list
    index = 0
    for i in range(len(arr)):
        # moves up in list
        if arr[i] != 0:
            arr[index]=arr[i]
            index+=1
    #replaces ending with 0's
    for i in range(index,len(arr)):
        arr[i]=0
    return arr

# def moving_zeroes(arr):
#     for i in range(len(arr)):
#         x = arr[i]
#         if x != 0:
#             arr = [x] + arr[:i] + arr[i+1:]

# def moving_zeroes(arr):
#     # return just the nonzero values in the array
#     nonzero_integers = [number for number in arr if number != 0]

#     # add with zeroes on the right
#     return nonzero_integers + [0] * (len(arr) - len(nonzero_integers))

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")