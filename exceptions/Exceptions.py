n = int(input())

for i in range(n):
    a, b = input().split()
    try:
        print(int(int(a) / int(b)))
    except ValueError as e:
        print(f"Error Code: {e}")
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")