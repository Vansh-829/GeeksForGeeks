# Input
# 3

# Expected output 
# 3 3 3 2 2 2 1 1 1 $3 3 2 2 1 1 $3 2 1 $

def printPat(n):
    #Code here
    for i in range(n,0,-1):
        for j in range(n,0,-1):
            for k in range(i,0,-1):
                print(j,end=" ")
        print('',end="$")


# { 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n= int(input())
        printPat(n)
# } Driver Code Ends