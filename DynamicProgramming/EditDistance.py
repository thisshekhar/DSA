# edit  distance between two strings naive recursive approach
def edit_distance_recursive(X,Y):
    if len(X) == 0:
        return len(Y)
    if len(Y) == 0:
        return len(X)
    if X[-1] == Y[-1]:
        return edit_distance_recursive(X[:-1],Y[:-1])
    else:
        # delete, insert, replace
        return 1 + min(edit_distance_recursive(X,Y[:-1]),edit_distance_recursive(X[:-1],Y), edit_distance_recursive(X[:-1],Y[:-1]))
    
# edit distance using dynamic programming bottom up approach O(n*m) time | O(n*m) space
def edit_distance_bottom_up(X,Y):    
    n = len(X)
    m = len(Y)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):    
        for j in range(m+1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],    # Delete
                                   dp[i][j - 1],    # Insert
                                   dp[i - 1][j - 1]) # Replace
                
    return dp[n][m]

# Example usage
if __name__ == "__main__":   
    X = "sunday"
    Y = "saturday"
    print(f"Edit Distance between {X} and {Y} is {edit_distance_recursive(X,Y)}")   
