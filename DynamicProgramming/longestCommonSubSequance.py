#Recursive Solution O(2^n+m) time | O(n+m) space
def lcs_recurssive(X,Y,n,m):
    if(n == 0 or m == 0):
        return 0
    if(X[n-1] == Y[m-1]):
        return 1 + lcs_recurssive(X,Y,n-1,m-1)
    else:
        return max(lcs_recurssive(X,Y,n-1,m),lcs_recurssive(X,Y,n,m-1))
    
#Example: Longest Common Subsequence (LCS) with Recursion + Memoization O(n*m) time | O(n*m) space
def lcs_memoization(X,Y,n,m,memo={}):
    if(n == 0 or m == 0):
        return 0
    if((n,m) in memo):
        return memo[(n,m)]
    if(X[n-1] == Y[m-1]):
        memo[(n,m)] = 1 + lcs_memoization(X,Y,n-1,m-1,memo)
        return memo[(n,m)]
    else:
        memo[(n,m)] = max(lcs_memoization(X,Y,n-1,m,memo),lcs_memoization(X,Y,n,m-1,memo))
    return memo[(n,m)]

# Bottom up dynamic programming approach O(n*m) time | O(n*m) space
def lcs_bottom_up(X,Y,n,m):
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(X[i-1] == Y[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[n][m]

#Recovering the LCS string from the DP table
def lcs_string(X,Y,n,m):
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(X[i-1] == Y[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    
    index = dp[n][m]
    lcs_str = [''] * index
    i,j = n,m
    while(i > 0 and j > 0):
        if(X[i-1] == Y[j-1]):
            lcs_str[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif(dp[i-1][j] > dp[i][j-1]):
            i -= 1
        else:
            j -= 1
    return ''.join(lcs_str)

#minimum deletions and insertions to convert string X to Y
def min_deletions_insertions(X,Y):
    n = len(X)
    m = len(Y)
    lcs_length = lcs_bottom_up(X,Y,n,m)
    deletions = n - lcs_length
    insertions = m - lcs_length
    return deletions, insertions

#shortest common supersequence length
#- A supersequence of two strings s1 and s2 is a string that contains both s1 and s2 as subsequences.
#- The Shortest Common Supersequence (SCS) is the shortest possible string that has both s1 and s2 as subsequences.
#Its length can be derived using the Longest Common Subsequence (LCS).

def scs_length(X,Y):
    n = len(X)
    m = len(Y)
    lcs_length = lcs_bottom_up(X,Y,n,m)
    return n + m - lcs_length   

# longest palindromic subsequence
def longest_palindromic_subsequence(X):
    Y = X[::-1]
    n = len(X)
    m = len(Y)
    return lcs_bottom_up(X,Y,n,m)   

#Example usage
if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    n = len(X)
    m = len(Y)
    print(f"Length of LCS is {lcs_bottom_up(X,Y,n,m)}")
    print(f"LCS string is {lcs_string(X,Y,n,m)}")
    deletions, insertions = min_deletions_insertions(X,Y)
    print(f"Minimum deletions: {deletions}, Minimum insertions: {insertions}")
    print(f"Length of Shortest Common Supersequence is {scs_length(X,Y)}")  
    palin_str = "AGBCBA"
    print(f"Length of Longest Palindromic Subsequence is {longest_palindromic_subsequence(palin_str)}")