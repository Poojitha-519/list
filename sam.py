'''
Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
'''

lst = list(map(int, input("Enter the elements of the list separated by space: ").split()))
lst.sort()
print(" ".join(map(str, lst)))
