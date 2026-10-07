1class Solution {
2public:
3    int maxProfit(vector<int>& A) {
4        int mini = A[0];
5        int maxprofit = 0;
6        int n = A.size();
7        for(int i = 1; i<n; i++){
8            int cost = A[i] - mini;
9            maxprofit = max(maxprofit,cost);
10            mini = min(mini , A[i]);
11        }
12        return maxprofit;
13        
14        
15    }
16};