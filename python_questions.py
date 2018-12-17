import pdb;

'''
A is a sorted list of n different elements in ascending order.
Consider A = [10,23,36,37,47,59,64,71] for example.
Using python language specific syntax, determine if a given element
is contained in the list, A.

'''

def find_element_py(sorted_list,element):
    if element in sorted_list:
    	print('Element found.')
    else:
    	print('Element not found')

find = int(input('Enter the element you are looking for: '))
find_element_py([10,23,36,47,59,64,71],find)

'''
A is a sorted list of n different elements in ascending order.
Consider A = [10,23,36,37,47,59,64,71] for example.
Using python language specific syntax, determine if a given element
is contained in the list, A.

'''

def find_element_nopy(sorted_list, element):
    found = False
    for x in sorted_list:
        if x == element:
            found = True
            
    if found == True:
        print('Element found.')
    else:
        print('Element not found')

find = int(input('Enter the element you are looking for: '))
list = [10, 23, 36, 47, 59, 64, 71]
list.sort()
find_element_nopy(list,find)



#find_element_py([10,23,36,37,47,59,64,71], 36) >>True



'''
A  shift  of  a  sorted  array  by k,
means  removing  the  last k elements and placing them at the beginning.

For example, if A=[1,2,3,4,5,6,7] and k= 3 then new A = [5,6,7,1,2,3,4].
Given a sorted list A that  has  been  shifted  by  an  unknown k,
give  an O(n) algorithm to find k

'''

from collections import deque

def shifting_array(sorted_list):
    #used https://docs.python.org/3/library/collections.html#deque-objects for reference
    A = deque(sorted_list)
    k = int(input('By how many elements would you like to shift the array?\n'))
    #shifting the elements
    A.rotate(k)
    #print result
    print('Shifted array: ')
    for x in A:
        print(x)

shifting_array([1,2,3,4,5,6,7])


def shifted_array(alist):
    minimum = min(alist)
    k = alist.index(minimum)
    print('The list was shifted by ',k,'elements.')


shifted_array([5,6,7,1,2,3,4])


'''
try to implement this with O(log(n)) algorithm
'''
def shifted_array_fast(sorted_list):
    pass

#shiftd_array([5,6,7,1,2,3,4]) >>3


'''
Find the Nth number in Fibonacci sequence.

A Fibonacci sequence is defined as follow:

The first two numbers are 0 and 1.
The i th number is the sum of i-1 th number and i-2 th number.
The first ten numbers in Fibonacci sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

Example
Given 1, return 0

Given 2, return 1

Given 10, return 34

Notice
The Nth fibonacci number won't exceed the max value of signed 32-bit integer in the test cases.

'''

def fibonacci(n):
    fib = [0,1]
    for x in range(2,(n+1)):
        fib.append(fib[x-1] + fib[x-2])
    return fib[n]

n = int(input('In what position is the number you are looking for?\n'))
print('Given', n, 'the fibonacci is' , fibonacci(n))

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

'''

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Clarification
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
'''

def reverseString(s):
    new_string = s.split(" ")
    new_string.reverse()
    print new_string

s = "this is my test sentence"
reverseString(s)


'''
Reverse a 3-digit integer.

Example
Reverse 123 you will get 321.

Reverse 900 you will get 9.

Notice
You may assume the given number is larger or equal to 100 but smaller than 1000.
'''

def reverseInteger(num):
    reverse = 0
    while num!=0:
        reverse = (reverse*10) + (num%10)
        num = int(num/10)
    return reverse

num = int(input('Enter the number you want to reverse: '))
reverse = reverseInteger(num)
print('The reversed number is:', reverse)













