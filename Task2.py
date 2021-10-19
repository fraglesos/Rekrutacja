# %%
import itertools

# %%
# Description 
# dials is ordered list of letters assigned to every number on the phone dial, notice that for 0 its '', because '+'
# is not a letter. The script takes a number num from a user, which can have any number of digits because it varies 
# from country to country and removes all the 1s and 0s. Then it converts numbers to letters sets stored in a 
# table letters. In the and it uses itertools method product() with variable size argument *letters to 
#produce all the combinations.
#
# Variables
# dials - ordered list of letters assigned to every number on the phone dial
# num - number provided by the user as a string
# nums - number provided by the user as a table
# letters - table of numbers converted to according letters set

dials = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
num = input("Please, provide a number: ")
if num == ''or num.isdigit() == False:
    print([])
else:
    nums = [int(i) for i in num]
    while (0 in nums):
        nums.remove(0)
    while (1 in nums):
        nums.remove(1)
    letters = [dials[i] for i in nums]
    for i in itertools.product(*letters):
        print(''.join(i))

# %%
