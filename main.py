# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def PartA(k):
    return [int('1'+'0'*i) for i in range (0,k)]
    return list
for i in PartA(10):
    print (i)
def PartB(k):
    list=[sum(2*i for i in range (0,j)) for j in range (1,k+1)]
    return list
for i in PartB(10):
    print (i)
def PartC(k):
    return [chr(97+i) for i in range (0,k)]
for i in PartC(26):
    print(i,end=' ')