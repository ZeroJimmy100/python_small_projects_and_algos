
def Insertion(list):
    for i in range(1, len(list)):
        value = list[i]
        while list[i-1] > value and i > 0:
            list[i], list[i-1] = list[i-1], list[i]
       
        
    return list

list = [3,6,8,2,0,9,5,4,1]
Insertion(list)
print(Insertion(list))