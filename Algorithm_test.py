# #PROBLEM 1
#     # Compute the sum of digits in all numbers from 1 to n.
#     # When a function gets a number n, find the sum of digits in
#     # all numbers from 1 to n.
#     # Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
#
def sum_of_digits(n):
 for n in range(1, n+1):
    total = sum(range(1, n+1))
 return(total)
n = 5
print(sum_of_digits(n))
#
#
# #PROBLEM 2
#    #Find max number from 3 values.
#    # Example: 124, 21, 32. Result = 124.
# #
def max_number(list):
    max = list[0]
    for number in list:
        if number > max:
            max = number
    return (max)
list = [124, 21, 32]
print(max_number(list))
#
# #PROBLEM 3
#     #Count odd and even numbers.
#     # Count odd and even digits of the whole number.
#     # Example: number is 34560, then 3 digits will be
#     #   even (4, 6, and 0) and 2 odd digits (3 and 5).
#
#
def count_digits(num):
  if type(num) == int:
    arr = str(num)

    result = {
      'odd': 0,
      'even': 0

    }

    for digit in arr:
      if int(digit) % 2 == 0:
        result['even'] += 1
      else:
        result['odd'] += 1

    return result
  else:
    return False

print (count_digits(123))




