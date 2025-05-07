def create_list():
    l=[]
    while True:
        try:
            l.append(int(input("Enter a number: ")))
        except Exception as e:
            return l

def selection_sort(arr):
    n=len(arr)
    for i in range (0,n-1):
        actual_ind=n-1-i
        curr_max=-2147283648
        curr_max_ind=-1
        for j in range(0,n-i):
            if curr_max<arr[j]:
                curr_max=arr[j]
                curr_max_ind=j
        arr[actual_ind],arr[curr_max_ind]=(arr[curr_max_ind],arr[actual_ind])
arr=create_list()
selection_sort(arr)
print(arr)