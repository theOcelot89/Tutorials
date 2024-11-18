def fibonacci(steps):

    F1 = 1
    F2 = 1
    
    for step in range(steps-1):

        # fib = F1 + F2 
        # F1 = F2
        # F2 = fib
        F2, F1 = F1, F2 + F1
       
    return F2

print(fibonacci(12))