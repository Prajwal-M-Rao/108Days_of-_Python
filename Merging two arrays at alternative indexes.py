#WAP to merge the given two arrays at alternate indexes
def create_list():
    l=[]
    while True:
        try:
            l.append(int(input("Enter a number: ")))
        except Exception as e:
            return l

def merge_array(arr1,arr2):
    i,j,k=0,0,0
    n=len(arr1)+len(arr2)
    res=[]
    while k<n:
        if i<len(arr1) and k%2==0:
            res.append(arr1[i])
            i+=1
            k+=1
        elif j<len(arr2) and k%2!=0:
            res.append(arr2[j])
            j+=1
            k+=1
        else:
            if len(arr1)<len(arr2):
                res.append(arr2[j])
                j+=1
                k+=1
            else:
                res.append(arr1[i])
                i+=1
                k+=1
    return res
print("Enter values of first array")
arr1=create_list()
print("Enter values of second array")
arr2=create_list()
print(merge_array(arr1,arr2))
