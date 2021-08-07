#1 
arr = [-1, 3, 5, -5]
def Biggie(arr):
    for x in range(0, len(arr), 1):
        if arr[x] > 0:
            arr[x] = "Big"
    print(arr)        

Biggie(arr)

#2 
arr = [-1, 3, 5, -5]

def CountPos(arr):
    count = 0
    for x in range(0, len(arr), 1):
        if arr[x] > 0:
            count+=1
    arr[x] = count
    print(arr)
CountPos(arr)    

#3
arr = [1,5,6,8,10]
def SumCount(arr):
    sum = 0
    for x in range(0, len(arr), 1):
        sum+=arr[x]
    print(sum)
SumCount(arr)        

#4
arr = [1,2,4,6,10]
def avgVal(arr):
    sum=0
    for x in range(0, len(arr), 1):
        sum+=arr[x]
    avg=sum/len(arr)
    print(avg)
avgVal(arr)    

#5
arr = [1,2,4,5,6]
def LenGth(arr):
    return len(arr)
print(LenGth(arr))   

#6 
arr = [1,5,10,2,8]
def Min(arr):
    min = arr[0]
    if len(arr) == 0:
        return False
    for x in range(0, len(arr), 1):
        if arr[x] < min:
            min = arr[x]
    return min    
print(Min(arr))  

#7
arr = [1,5,10,2,8]
def Max(arr):
    max = arr[0]
    if len(arr) == 0:
        return False
    for x in range(0, len(arr), 1):
        if arr[x] > max:
            max = arr[x]
    return max    
print(Max(arr))  

#8 
arr = [37,2,1,-9]
def Analy(arr):
    max = arr[0]
    min = arr[0]
    sum = 0
    for x in range(0, len(arr), 1):
        if arr[x] < min:
            min = arr[x]
        if arr[x] > max:
            max = arr[x]
        sum+=arr[x]
    avg = sum/len(arr)
    return {'sumTotal': sum, 'average' : avg, 'maximum': max, 'length': len(arr)}
print(Analy(arr))

#9 
arr = [37,2,1,-9]
def rev(arr):
    return arr[::-1]
print(rev(arr))
   
