# Python3 program to illustrate 
# recursive approach to ternary search 

import numpy as np  

# Function to perform Ternary Search 

def ternarySearch(l, r, key, ar,c): 
    
    if (r >= l): 
  
        # Find the mid1 and mid2 
        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3
        c=c+1
  
        # Check if key is present at any mid 
        if (ar[mid1] == key): 
            
            print("found:",ar[mid1],"\tcomparisons:",c,end="\t")
            return c 
          
        if (ar[mid2] == key):
            
            print("found:",ar[mid2],"\tcomparisons:",c,end="\t")
            return c 
          
        # Since key is not present at mid, 
        # check in which region it is present 
        # then repeat the Search operation 
        # in that region 
        if (key < ar[mid1]):  
            
            # The key lies in between l and mid1 
            return ternarySearch(l, mid1 - 1, key, ar,c) 
          
        elif (key > ar[mid2]):  
            
            # The key lies in between mid2 and r 
            return ternarySearch(mid2 + 1, r, key, ar,c) 
          
        else:  
           
            # The key lies in between mid1 and mid2 
            return ternarySearch(mid1 + 1, mid2 - 1, key, ar,c) 
          
    # Key not found 
    print("didn't find:",key,end="")
    return c
#############################BINARY SEARCH##################################
# Python Program for recursive binary search. 
  
# Returns index of x in arr if present, else -1 
def binarySearch (l, r, key, ar,c): 
  
    # Check base case 
    if r >= l: 
        
        mid = l + (r - l)//2
        c=c+1
  
        # If element is present at the middle itself 
        if (ar[mid] == key): 
            print("found:",ar[mid],"\tcomparisons:",c,end="\t")
            return c 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif (ar[mid] > key): 
            
            return binarySearch(l, mid-1, key,ar,c) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            
            return binarySearch(mid + 1,r, key,ar,c) 
  
    else: 
        # Element is not present in the array 
        print("didn't find:",key,end="")
        return c
  
###########################################################################
  #DRIVER CODE
###########################################################################
 
#KEY GENERATION 
keys = np.zeros(10,dtype=int)   #initialize array to hold 10 keys

#this function fills the key array with values, depending on the size of the array
def keyGen(length,arr): 
    length=len(arr)
    for i in range (10):  #fill array with values
        keys[i]=np.random.randint(0, int(8*np.sqrt(length)), dtype=int)
        
arrSizes = [500, 1000, 2000, 4000, 8000]  
for i in range(len(arrSizes)):
    arrCurr = np.zeros(arrSizes[i],dtype=int) #initialize to zeros
    for j in range (arrSizes[i]):
        arrCurr[j] = int(8*np.sqrt(j))
    print("-------------------------------------------------------\n")
    print("Array size:",arrSizes[i],"\n")
    
    
    keyGen(arrSizes[i],arrCurr)
    print("Keys:",keys)
    
    #RUN TERNARY SEARCH
    print("TERNARY SEARCH")
    avg = 0
    for k in range (10):
        avg = avg +ternarySearch(0, arrSizes[i], keys[k], arrCurr,0) #ternary function call
        print()
    print("Average number of comparisons:",avg/10)
            
    exponent = np.log(arrSizes) / np.log(3)
    print("\n# of comparisons <= log(",arrSizes[i],")) base 3\n")
    
    #RUN BINARY SEARCH
    print("BINARY SEARCH")
    avg = 0
    for k in range (10):
        avg = avg +binarySearch(0, arrSizes[i], keys[k], arrCurr,0)    #binary function call
        print()
    print("Average number of comparisons:",avg/10)
    
    
    print("\n# of comparisons <=",int(np.log2(arrSizes[i])),"(C = log(",arrSizes[i],")) base 2\n")
          
          
          
  
