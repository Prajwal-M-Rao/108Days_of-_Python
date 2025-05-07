def create_list():
    l=[]
    while True:
        try:
            l.append(int(input("Enter a number: ")))
        except Exception as e:
            return l

def Insertion_sort_asc(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(i+1,0,-1):
            if arr[j-1]>arr[j]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
    return arr
def Insertion_sort_desc(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(i+1,0,-1):
            if arr[j-1]<arr[j]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
    return arr

arr=create_list()
print("Array before sorting: ",arr)
print("Array after sorting in ascending: ",Insertion_sort_asc(arr))
print("Array after sorting in descending: ",Insertion_sort_desc(arr))
