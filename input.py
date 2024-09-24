'''
Write a Python Program to find the smallest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
1
'''

n = int(input("Enter the size of the list: "))
lst = []
for i in range(n):
    num = int(input())
    lst.append(num)
smallest = lst[0]
for num in lst:
    if num < smallest:
        smallest = num
print(smallest)
