Hamming Weight:

Write a python program that takes a integer between 0 and 15 as input and displays the number of '1' s in its binary form.(Hint:use python bitwise operator.
Sample Input
3
Sample Output:
2
Explanation:
The binary representation of 3 is 011, hence there are 2 ones in it. so the output is 2.

Program:

a=int(input())
n=bin(a)
n=n.replace("0b","")
s=str(n)
c=list(s)
d=0
for i in range(len(c)):
    if(int(c[i])==1):
        d+=1
print(d)
