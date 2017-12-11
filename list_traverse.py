import sys

def list_traverse(L):
    L1 = []
    for i in range(len(L)):
        length = 0
        for j in range(i+1,len(L)):
            if abs(L[j] - L[i]) <= 1:
                length += 1
        L1.append(length + 1);
        
        
    return max(L1)

L = [1,3,2,2,5,2,3,7]
print(list_traverse(L))

