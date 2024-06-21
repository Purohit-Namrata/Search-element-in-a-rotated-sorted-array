import array as a

def searchelement(array,l,e):
    i=0
    j=l-1
    while(i<=j):
        mid=(i+j)//2

        if array[i]==e:
            return i
        
        if array[j]==e:
            return j      

        if array[mid]==e:
            return mid
        
        if array[i]<=array[mid]:
            if array[i]<=e and e<=array[mid]:
                j=mid-1
            else:
                i=mid+1
        else:
            if array[mid]<=e and e<=array[j]:
                i=mid+1
            else:
                j=mid-1

    return -1
    
'''
arr=[]
l=int(input("Enter length of array:\n"))
print("Enter elements of array")

for i in range(0,l):
    input(arr.append(i))
'''

#arr=a.array('i',[4,5,1,2,3])

arr=[4,5,7,1,2,3]
element=int(input("Enter element to search"))

search_value=searchelement(arr,6,element)

if search_value==-1:
    print("ELement not found")
else:
    print("ELement found at index: ", search_value)




        
