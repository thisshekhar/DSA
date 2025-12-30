# Top down dynamic programming approach to calculate Fibonacci numbers with memoization
def fibonacci(n,memo = {}):
    if(n in memo):
        return memo[n]
    if(n <= 1):
        return n
    memo[n] = fibonacci(n-1,memo) + fibonacci(n-2,memo)
    return memo[n]

# Bottom up dynamic programming approach to calculate Fibonacci numbers
def fibonacci_bottom_up(n):
    if(n<=1):
        return n
    fib = [0] * (n+1)
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]   

# Bottom up dynamic programming approach to calculate Fibonacci numbers
def fibonacci_bottom_up_space(n):
    if(n<=1):
        return n
    prev,curr = 0,1
   
    for i in range(2,n+1):
        next_fib = prev + curr
        prev,curr = curr,next_fib
    return curr 

# Example usage
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci of {n} is {fibonacci_bottom_up_space(n)}")    