cube = lambda x: x**3 

def fibonacci(n):
    fib = []
    for i in range(n):
        if i == 0:
            num = 0
        elif i == 1:
            num = 1
        else:
            num = fib[i-1] + fib[i-2]
        fib.append(num)
    return fib
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))