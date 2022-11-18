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
#
# def split_string(test_string):
#     length = len(test_string)
#     add = 0
#     if length % 2:
#         add = 1
#     for i in test_string:
#         string1 = test_string[len(test_string)//2:]
#         string2 = test_string[:len(test_string)//2]
#     return(string1, string2)
#
#
# test_string = 'bbbbbcaaaaa'
#
# print(split_string(test_string))
#
#
# # Unique Characters in String
# # Given a string, determine if it consists of all unique characters.
# # For example, the string 'abcde' has all unique characters and should return True.
# # The string 'aabcde' contains duplicate characters and should return False.
# # Hint: https://www.w3schools.com/python/python_sets.asp
# #
# def digital_root(n):
#     d = {}
#     for i in n:
#         if i in d:
#             d[i] += 1
#             return True
#         else:
#             return False
#
# # return len(set(n)) == len(n)
#
#
# n = 'abcde'
# print(digital_root(n))


#PROBLEM 6
# Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The
# arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25),
# Return [1, 3, 4, 2, 3]

# def arthmetical_mean(list):
#     list = [1, 3, 5, 6, 4, 10, 2, 3]
#     list_mean = (sum(list)/len(list))
#     print(list_mean)
#     list2 = []
#     for num in list:
#         if num < list_mean:
#             list2.append(num)
#     return list2
# print(arthmetical_mean(list))
#
#
# #PROBLEM 7
# # Two Lowest Elements
# # When given a list of elements, find the two lowest elements. They can be equal to each other or different.
# # Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
#
# def lowest_elements(list):
#     list = [198, 3, 4, 9, 10, 9, 2]
#     list.sort()
#     return list[0:2]
#
# print(lowest_elements(list))


# PROBLEM 8
# Even First
# Your input is a list of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]


# def even_first(array):
#     index = 0
#     for i in range(0, len(array)):
#         if array[index] % 2 != 0:
#             array.append(array[index])
#             array.remove(array[index])
#         else:
#             index += 1
#     return array
#
# array = [7, 3, 5, 6, 4, 10, 3, 2]
# print(even_first(array))
# # def even_odd(A):
# #     even = 0
# #     odd = len(A) - 1
# #     while even < odd:
# #         if A[even] % 2 == 0:
# #             even += 1
# #         else:
# #             A[even], A[odd] = A[odd], A[even]
# #             odd -= 1
# #     return A
# # A = [7, 3, 5, 6, 4, 10, 3, 2]
# # print(even_odd(A))
#
# # PROBLEM 9
# # Increment a Number
# # Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and
# # updates the list to represent the integer D + 1.
# # For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].
#
# # def increment(S):
# #     if S[i] >= 9:
# #         S[i] = 0
# #         S[i - 1] += 1
# #     elif S[i - 1] < 9:
# #         S[i - 1] += 1
# #     else S[i - 2] :
# #         S[i -2] += 1
#
# #     return S
# #
# # S = [9,9,9]
# # print(increment(S))
#
#
# def plus_one(arr):
#     arr[-1] += 1
#     for i in reversed(range(1, len(arr))):
#         if arr[i] != 10:
#             break
#         arr[i] = 0
#         arr[i - 1] += 1
#
#     if arr[0] == 10:
#         arr[0] = 1
#         arr.append(0)
#
#     return arr
#
# test1 = [1,2,5]
# test2 = [1,2,9]
# test3 = [9,9,9]
#
# print(plus_one(test1))
# print(plus_one(test2))
# print(plus_one(test3))


#Selection Sort
# Implement the selection sort algorithm that is sorting in descending order.
def descendingSelectionSort(MyList):
    for i in range(len(MyList) - 1):
        minimum = i
        for j in range(len(MyList)-1, i, -1):
            if(MyList[j] > MyList[minimum]):
                minimum = j
        if(minimum != i):
            MyList[i], MyList[minimum] = MyList[minimum], MyList[i]
    return MyList


MyList = [1, 3, 19, 2]
print(descendingSelectionSort(MyList))

# Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.

def bubble_Sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


number = [ 4, 10, 7, 9 ];
bubble_Sort(number)
print(number)


# Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key > array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key


list = [9, 3, 7, 8, 0]
insertionSort(list)
print(list)

# Merge Sort
# Implement the merge sort algorithm that is sorting in descending order.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def merge_arrays(left_arr, right_arr):
    merged_arr = []
    i = j = 0
    while i < len(left_arr) or j <len(right_arr):
        if i == len(left_arr):
            merged_arr.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merged_arr.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] >= right_arr[j]:
            merged_arr.append(left_arr[i])
            i += 1
        else:
            merged_arr.append(right_arr[j])
            j += 1
    return merged_arr



test_list = [3, 7, 9, 11]
print(merge_sort(test_list))
