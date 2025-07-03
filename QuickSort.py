def Quick_sort(arr,low,high):
    if low>=high:
        return

    start,end=low,high
    mid=(start + end)//2
    pivot=arr[mid]

    while start<=end:
        while arr[start]<pivot:
            start+=1
        while arr[end]>pivot:
            end-=1

        if start <=end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1

    #LHS
    Quick_sort(arr,low,end)

    #RHS
    Quick_sort(arr,start,high)

def create_list():
    l=[]
    while True:
        try:
            l.append(int(input("Enter a number: ")))
        except Exception as e:
            return l

arr=create_list()
print("Array before sorting: ",arr)
Quick_sort(arr,0,len(arr)-1)
print("Array after sorting: ",arr)
