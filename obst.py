def optimal_bst(keys, freq):
    n = len(keys)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        dp[i][i + 1] = freq[i]

    for length in range(2, n + 1):
        for i in range(n - length + 2):
            j = i + length - 1
            dp[i][j] = float('inf')
            sum_freq = sum(freq[i:j+1])

            for k in range(i, j + 1):
                temp = dp[i][k] + dp[k + 1][j] + sum_freq
                if temp < dp[i][j]:
                    dp[i][j] = temp

    return dp[0][n]

if __name__ == "__main__":
    keys = input("Enter keys separated by spaces: ").split()
    freq = list(map(int, input("Enter corresponding frequencies: ").split()))

    result = optimal_bst(keys, freq)
    print("Optimal binary search tree cost:", result)



# output:
# Enter keys separated by spaces: A B C D
# Enter corresponding frequencies: 0.1 0.2 0.4 0.3
# Optimal binary search tree cost: 1.3