# %%
import timeit
import collections

# %%
# Description
# Mathematical approach to the problem. It uses the fact that if x = sum(n = 0, N)10^n*a_n where N is
# the highest order of the magnitude of the given number, then inverted x' = sum(n = 0, N)10^(N-n)*a_n
# and delta = x - x' = sum(n = 0, N)(10^n - 10^[N-n])a_n which yields x' = x - delta. The output is multiplied by
# x/abs(x) to ensure right sign.
#
# Parameters
# x - number to be inverted
#
# Return
# Returns inverted number if x is 32int and 0 otherwise.

def invNum(x):
    if x < 2**31 and x > -2**31-1:
        ax = abs(x)
        N = len(str(ax))
        coef = []
        for i in range(N):
            coef.insert(0,(ax % 10**(N-i)) // 10**(N-i-1))
        delta = 0
        for i in range(N):
            delta = delta + (10**i-10**(N-i-1))*coef[i]
        y = int(x/ax*(ax - delta))
        print(y)
    else:
        print(0)

# %%
# Description
# More conventional approach. It stores number of units, tens, hundreds etc. in the table in inverted order.
#
# Parameters
# x - number to be inverted
#
# Return
# Returns inverted number if x is 32int and 0 otherwise.

def altInvNum(x):
    if x < 2**31 and x > -2**31-1:
        ax = abs(x)
        N = len(str(ax))
        coef = collections.deque([])
        for i in range(N):
            coef.appendleft(str((ax % 10**(N-i)) // 10**(N-i-1)))
        coef[0]=str(int(x/ax)*int(coef[0]))
        print(''.join(coef))
    else:
        print(0)

# %%
print("The script uses two different methods to obtain output. Please check out the description.")
x = int(input("Enter a number: "))
invNum(x)
altInvNum(x)

# %%
# This parts checks the efficiency of both methods. Interestingly efficiency varies for different inputs.
#def wrapper(func, *args, **kwargs):
#    def wrapped():
#        return func(*args, **kwargs)
#    return wrapped

# %%
#wrapped=wrapper(invNum,x)
#timeit.timeit(wrapped, number=1)

# %%
#wrapped=wrapper(altInvNum,x)
#timeit.timeit(wrapped, number=1)
