def selection_sort_greedy(arr):
    n = len(arr)
    print("\nList before Sorting: ", arr,"\n")
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:#smaller than the current minimum element
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print("List After Pass ",i+1,": ",arr)
    return arr
n=int(input("Length of List: "))
arr=[]
for i in range(n):
    element=int(input("Enter List Element: "))
    arr.append(element)
print("\nSorted List is:", selection_sort_greedy(arr))

'''
Length of List: 5
Enter List Element: 11
Enter List Element: 45
Enter List Element: 8
Enter List Element: 12
Enter List Element: 16

List before Sorting:  [11, 45, 8, 12, 16] 

List After Pass  1 :  [8, 45, 11, 12, 16]
List After Pass  2 :  [8, 11, 45, 12, 16]
List After Pass  3 :  [8, 11, 12, 45, 16]
List After Pass  4 :  [8, 11, 12, 16, 45]
List After Pass  5 :  [8, 11, 12, 16, 45]

Sorted List is: [8, 11, 12, 16, 45]
'''
'''
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
'''
