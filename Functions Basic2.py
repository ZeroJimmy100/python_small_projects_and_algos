#1
def countdown(num):
    for x in range (num, -1, -1):
        print(x)
num=5
countdown(num)

#2 
def printandreturn(a, b):
    print(a)
    return b
num1 = 1
num2 = 2
printandreturn(num1, num2)

#3 
def first_plus_length(arr):
    print(arr[0] + len(arr))
arr = [1, 2, 3, 4, 5]
first_plus_length(arr)

#4 
arr = [5,2,3,2,1,4]
def values_greater_than_second(arr):
    newarr = []
    count = 0
    for x in range(0, len(arr), 1):
        if arr[x] >= arr[2]:
            count+=1
            newarr.append(arr[x]) 
    print(newarr)
    print (count)
values_greater_than_second(arr)

#5 
newarr = []
def thislength_value(size, value):
    for x in range(0, size, 1):
        newarr.append(value)
    print(newarr)
thislength_value(4, 5)
