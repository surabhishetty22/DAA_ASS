def optimal_bst(keys, freq):
    n = len(keys)
    dp = [[float('inf')] * n for _ in range(n)]  # Initialize dp with large values
    
    for i in range(n):
        dp[i][i] = freq[i]  # Single key has the cost equal to its frequency
        
    for L in range(2, n+1):
        for i in range(n - L + 1):
            j = i + L - 1
            sum_freq = sum(freq[i:j+1])
            
            for k in range(i, j + 1):
                left = dp[i][k - 1] if k > i else 0
                right = dp[k + 1][j] if k < j else 0
                temp = left + right + sum_freq
                dp[i][j] = min(dp[i][j], temp)
    
    return dp[0][n - 1]
keys = input("Enter keys separated by spaces: ").split()
freq = list(map(float, input("Enter corresponding frequencies: ").split()))
result = optimal_bst(keys, freq)
print("Optimal binary search tree cost:", result)
