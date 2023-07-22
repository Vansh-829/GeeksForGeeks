'''
For Input: 
5
10 20 30 40 50
Your Output: 
10.00 15.00 20.00 25.00 30.00
Expected Output: 
10.00 15.00 20.00 25.00 30.00
'''

class Solution:
    def streamAvg(self, arr, n):
        ans = []
        for i in range(len(arr)):
            sum = 0
            for j in range(i+1):
                sum = sum + arr[j]
            avg = sum / (i+1)
            ans.append(avg)
        return ans


# {
 # Driver Code Starts
# Initial template for Python
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.streamAvg(arr, n)
        for x in ans:
            print('%.2f' % x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
