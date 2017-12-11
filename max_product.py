import sys

def max_product(L):
    max = 0
    for i in range(len(L)-2):
        product = L[i]
        for j in range(i+1,i+3):
            product *= L[j]
        if product > max:
            max = product
    return max
            
            

L = [1,3,2,2,5,2,3,7]
print(max_product(L))
