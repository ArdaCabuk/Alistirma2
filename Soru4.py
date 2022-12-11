def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for n in range(0,30):
    print(fibonacci(n),end=" ")
        
    
