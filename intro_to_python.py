
import numpy as np


size =2
#arr=np.ones(9).reshape(3,3)
arr=np.identity(3)

print("Print a specific 3x3 matrix where a cell is 1 if i == j, else 0 ")
arrZeros= np.zeros(9).reshape(3,3)
for row in range(size):
    for col in range(1,size):
        if (row ==col):
            print("\nif i==j")
            print(arr,end='')
        else:
            print("\nElse")
            print(arrZeros,end=' ')

print("\nPrint the 3x3 matrix from #1 and then add 3 to every cell where i ≠j")  
for row in range(size):
    for col in range(1,size):
        if (row ==col):
            print()
        else:
            print("\nElse")
            arrZeros= arrZeros +3
            print(arrZeros,end=' ')
          
print("\nPrint the 3x3 matrix from #2 as a 3x2 by deleting the last column from the matrix created ") 
for row in range(size):
    for col in range(1,size):
        if (row ==col):
            print()
        else:
            print("\nElse")
            print(np.delete(arrZeros,0,1))
