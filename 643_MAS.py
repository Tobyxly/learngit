import sys

def max_average_subarray(L,k):
    temp_list = []
    for i in range(len(L)-k):
        sum1 = 0
        average = 0
        for j in range(i,k+i):
            sum1 += L[j]
        average = sum1/k
        temp_list.append(average)

    return max(temp_list)

L = [1,12,-5,-6,50,3]
k = 4

print(max_average_subarray(L,k))
        
            
    
