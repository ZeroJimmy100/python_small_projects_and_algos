
def selectionSort(list):

   for i in range(len(list)):

      # Find the minimum element in remaining
       Min = i

       for j in range(i+1, len(list)):
           if list[Min] > list[j]:
               Min = j
                
       # Swap the found minimum element with Min
       print(list)      
       temp = list[i]
       list[i] = list[Min]
       list[Min] = temp

   return list

print(selectionSort([1,5,3,2,0,6,8,7,9,4]))