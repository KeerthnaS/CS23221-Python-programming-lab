Converting Input Strings

Write a program to convert strings to an integer and float and display its type.
Sample Output:
10,<class 'int'>
10.9,<class 'float'>

For example:
Input
10
10.9
Result
10,<class 'int'>
10.9,<class 'float'>


Program:

a=input()
b=input()
c=int(a)
d=float(b)
print(c,type(c),sep=",")
print("{:0.1f}".format(d),type(d),sep=",")
