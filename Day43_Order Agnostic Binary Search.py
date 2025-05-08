def binary_search(num,arr):
    start=0
    end=len(arr)-1

    #to check array is ascending or descending
    if arr[start]<arr[end]:
        flag=True
    else:
        flag=False

    while start<=end:
        mid=(start+end) //2
        if arr[mid]==num:
            return mid

        if flag:
            if num<arr[mid]:
                end=mid-1
            else:
                start=mid+1
        else:
            if num < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1

def create_list():
    l=[]
    while True:
        try:
            l.append(int(input("Enter a number: ")))
        except Exception as e:
            return l

arr=create_list()
num=int(input("Enter the element to be searched: "))
flag=binary_search(num,arr)
if flag==-1:
    print("element not found")
else:
    print("The element",num,"found, in the index",flag)
