#reverse array
def create_list():
    l=[]
    while True:
        try:
            l.append(int(input("Enter a number: ")))
        except Exception as e:
            return l

def reverse_array(arr,i,j):
    while i<=j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

arr=create_list()
arr1=arr.copy()
k=int(input("Enter the number of rotations to be made: "))
n=len(arr)
k%=n
print("Array before rotation: ",arr)

#right rotation
reverse_array(arr,0,n-1)
reverse_array(arr,0,k-1)
reverse_array(arr,k,n-1)
print("Array After right rotation: ",arr)

#left rotation
reverse_array(arr1,0,k-1)
reverse_array(arr1,k,n-1)
reverse_array(arr1,0,n-1)

print("Array After left rotation: ",arr1)