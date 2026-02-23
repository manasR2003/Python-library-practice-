import numpy as np
# Create an empty and full NumPy array
arr1=np.array([])
print(arr1)
# Create a Numpy array filled with all zeros
arr2=np.array([0,0,0,0,0,0])
print(arr2)
# Create a Numpy array filled with all ones
arr3=np.array([1,1,1,1,1,1,1,1])
print(arr3)
# Check whether a Numpy array contains a specified row
arr4=np.array([[1,2,3],
               [4,5,6]])
row=[4,5,6]
row2=[7,8,9]
print(row in arr4.tolist())
print(row2 in arr4.tolist())
# Remove rows in Numpy array that contains non-numeric values
a = np.array([[10.5, 22.5, 3.8],
              [41, np.nan, np.nan]])
a=a[np.isfinite(a).all(axis=1)]
print(a)
# Remove single-dimensional entries from shape of an array
arr5=np.array([[[[1,2,3,4],[5,6,7,8]]]])
print(arr5.shape)
print(arr5)
arr6=arr5.squeeze()
print(arr6)
print(arr6.shape)
# Find number of occurrences of a sequence
arr7 = np.array([[2, 8, 9, 4],
                [9, 4, 9, 4],
                [4, 5, 9, 7],
                [2, 9, 4, 3]])

out=repr(arr7).count('9, 4')
print(out)
# Find most frequent value
arr8 = np.array([[2, 8, 9, 4],
                [9, 4, 9, 4],
                [4, 5, 9, 7],
                [2, 9, 4, 3]])

out=repr(arr8).count('9, 4')
print(out)
# Combining a one and a two-dimensional
arr9=np.array([1,2,3])
arr10=np.array([[10,20,30],[40,50,60]])

for a,b in np.nditer([arr9,arr10]):
    print(a,':',b)
# Build an array of all combinations of two NumPy arrays
arr11=np.array([1,2,3])
arr12=np.array([4,5,6])

l1=arr11.tolist()
l2=arr12.tolist()
arr13=np.empty((0,2),int)
for i in l1:
    for j in l2:
        arr13=np.append(arr13,[[i,j]],axis=0)
print(arr13)
        

# Add a border around a NumPy array
arr14 = np.array([[10],
                [20],
                [30],
                [40]])

out=np.pad(arr14,pad_width=1,mode='constant',constant_values=-1)
print(out)
# Compare two NumPy arrays
arr15 = np.array([[1, 2], [3, 4]])
arr16 = np.array([[1, 2], [3, 4]])

if np.array_equal(arr15, arr16):
    print("Equal")
else:
    print("Not Equal")
# Check whether specified values are present in NumPy array
arr17=np.array([[1,2,3],[4,5,6]])
val=6
print(val in arr17)
# Get 2D diagonals of a 3D array
arr = np.array([[[1, 2],
                 [3, 4]],
                [[5, 6],
                 [7, 8]]])
out=np.diagonal(arr,axis1=1,axis2=2)
print(out)
# Flatten a Matrix
matrix = np.array([[6, 9, 12],
                   [8, 5, 2],
                   [18, 21, 24]])
new_matrix=matrix.reshape(-1)
print(new_matrix)

# Interchange two axes of an array
arr = np.array([[1, 2, 3], [4, 5, 6]])

result = np.swapaxes(arr, axis1=0, axis2=1)

print("Original array:\n", arr)
print("Array after swapping axes:\n", result)
# Counts number of non-zero values
arr=np.array([0,1,0,3,0,5,3])
c=0
for i in arr:
    if int(i)!=0:
        c+=1
print(c)
print(np.count_nonzero(arr))
# Count number of elements along a given axis
matrix = np.array([[6, 9, 12],
                   [8, 5, 2],
                   [18, 21, 24]])
print(np.size(matrix,0))
# Trim leading and/or trailing zeros from a 1-D array
a = np.array([0, 0, 1, 2, 3, 0])
out=np.trim_zeros(a)
out1=np.trim_zeros(a,trim='f')
out2=np.trim_zeros(a,trim='b')
print(out)
print(out1)
print(out2)
# Change data type of given numpy array
arr = np.array([10, 20, 30, 40, 50])
print(arr.dtype)
# Reverse a numpy array
arr = np.array([10, 20, 30, 40, 50])
new_arr=arr[::-1]
print(new_arr)
# Make a NumPy array read-only
arr = np.array([10, 20, 30, 40, 50])
arr.setflags(write=False)
# arr[2]=99
print(arr)

#Sum of All Elements in a Numpy Array
arr = np.array([10, 20, 30, 40, 50])
sum_ele=np.sum(arr)
print(sum_ele)

#Maximum Element in a Numpy Array
arr = np.array([10, 20, 30, 40, 50])
print(np.max(arr))

#Mean of a Numpy Array
arr = np.array([10, 20, 30, 40, 50])
print(np.mean(arr))

#Reshape a Numpy Array
arr = np.array([10, 20, 30, 40, 50, 60])
new_arr=arr.reshape(2,3)
print(new_arr)

#Standard Deviation
arr = np.array([10, 20, 30, 40, 50, 60])
print(np.median(arr))

#Element-wise Exponentiation
arr = np.array([10, 20, 30, 40, 50, 60])
exp=2
arr=np.pow(arr,exp)
print(arr)

#Array Concatenation
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([100, 200, 300, 400, 500, 600])

arr3=np.hstack([arr1,arr2])
print(arr3)

#Reverse Rows of a 2D Array
matrix = np.array([[6, 9, 12],
                   [8, 5, 2],
                   [18, 21, 24]])
print(len(matrix))
for i in range(len(matrix)):
    matrix[0]=matrix[0][::-1]
print(matrix)

#Diagonal Elements in an Array
matrix = np.array([[6, 9, 12],
                   [8, 5, 2],
                   [18, 21, 24]])
print(np.array([matrix[i][i] for i in range(len(matrix))]))

#3D Array from a List of Lists
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
arr=np.array(data,ndmin=3)
print(arr)

#Accessing Element in a 3D Array
array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

index = (1, 0, 1)
print(array[index[0]][index[1]][index[2]])
print('----------------------------')

#Maximum Element along Each Axses in a 3D Array
matrix = np.array([[6, 9, 12],
                   [8, 5, 2],
                   [18, 21, 24]])
for i in matrix:
    print(np.max(i))

