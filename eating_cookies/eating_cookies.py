'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n, cache=None):
#     # negative cookies left: not possible. Return 0 as a solution.
#     if n < 0:
#         return 0

#     # exactly 0 cookies left: 1 solution found
#     # exactly 1 cookie left: 1 way to eat
#     elif n == 0 or n == 1:
#         return 1

#     # exactly 2 cookies left: 2 ways to eat
#     elif n == 2:
#         return 2

#     # define recursive terms
#     # start current term at 3 cookies to eat so all recursive terms are known
#     n_minus_3_cookies = 1
#     n_minus_2_cookies = 1
#     n_minus_1_cookie = 2

#     # define a variable to hold result
#     n_cookies = None

#     # calculate current term based on previous two terms
#     for i in range(3, n + 1):

#         n_cookies = n_minus_3_cookies + n_minus_2_cookies + n_minus_1_cookie

#         # update variables by shifting values over
#         n_minus_1_cookie, n_minus_2_cookies, n_minus_3_cookies = n_cookies, n_minus_1_cookie, n_minus_2_cookies

#     return n_cookies
    
def eating_cookies(n, cache=None):
    # Your code here
    if cache is None:
        cache = {}
    # base cases
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif cache and cache[n]:
        return cache[n]
    else:
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    num_cookies = 50

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
