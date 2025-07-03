def create_list():
    l=[]
    while True:
        try:
            l.append(int(input("Enter a number: ")))
        except Exception as e:
            return l

def Bubble_sort_asc(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def Bubble_sort_desc(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=create_list()
print("Array before sorting: ",arr)
print("Array after sorting in ascending: ",Bubble_sort_asc(arr))
print("Array after sorting in descending: ",Bubble_sort_desc(arr))
