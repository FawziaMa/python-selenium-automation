# # #PROBLEM 1
# #     # Compute the sum of digits in all numbers from 1 to n.
# #     # When a function gets a number n, find the sum of digits in
# #     # all numbers from 1 to n.
# #     # Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
# #
# def sum_of_digits(n):
#  for n in range(1, n+1):
#     total = sum(range(1, n+1))
#  return(total)
# n = 5
# print(sum_of_digits(n))
# #
# #
# # #PROBLEM 2
# #    #Find max number from 3 values.
# #    # Example: 124, 21, 32. Result = 124.
# # #
# def max_number(list):
#     max = list[0]
#     for number in list:
#         if number > max:
#             max = number
#     return (max)
# list = [124, 21, 32]
# print(max_number(list))
# #
# # #PROBLEM 3
# #     #Count odd and even numbers.
# #     # Count odd and even digits of the whole number.
# #     # Example: number is 34560, then 3 digits will be
# #     #   even (4, 6, and 0) and 2 odd digits (3 and 5).
# #
# #
# def count_digits(num):
#   if type(num) == int:
#     arr = str(num)
#
#     result = {
#       'odd': 0,
#       'even': 0
#
#     }
#
#     for digit in arr:
#       if int(digit) % 2 == 0:
#         result['even'] += 1
#       else:
#         result['odd'] += 1
#
#     return result
#   else:
#     return False
#
# print (count_digits(123))


# PROBLEM 4
# Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

def split_string(test_string):
    length = len(test_string)
    add = 0
    if length % 2:
        add = 1
    for i in test_string:
        string1 = test_string[len(test_string)//2:]
        string2 = test_string[:len(test_string)//2]
    return(string1, string2)


test_string = 'bbbbbcaaaaa'

print(split_string(test_string))


# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.
# Hint: https://www.w3schools.com/python/python_sets.asp
#
def digital_root(n):
    d = {}
    for i in n:
        if i in d:
            d[i] += 1
            return True
        else:
            return False

# return len(set(n)) == len(n)


n = 'abccde'
print(digital_root(n))
