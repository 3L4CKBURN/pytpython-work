def array_union(arr1, arr2):
   
    union_set = set(arr1).union(set(arr2))
  
    union_list = sorted(list(union_set))
    return union_list
    


size1=int(input("enter size array 1"))
size2=int(input("enter size array 2"))

arr1=[int(input()) for i in range(size1)]
arr2=[int(input()) for i in range(size2)]


# arr1 = [1, 2, 3, 4, 5]
# arr2 = [4, 5, 6, 7, 8]
print(array_union(arr1, arr2)) 
