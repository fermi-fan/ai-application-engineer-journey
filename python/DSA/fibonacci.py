# 分别使用loof与recursion两种方式实现斐波那契数列
# loop方式
import time
def fibonacci_loop(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_value = fib_sequence[i-1] + fib_sequence[i-2]
            fib_sequence.append(next_value)
        return fib_sequence
time_start = time.time()
print(fibonacci_loop(10))  
time_end = time.time()
print("Execution time:", time_end - time_start, "seconds")
 
# recursion方式
def fibonacci_recursion(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursion(n-1)
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
        return fib_sequence
    
time_start = time.time()
print(fibonacci_recursion(19))  
time_end = time.time()
print("Execution time:", time_end - time_start, "seconds")    