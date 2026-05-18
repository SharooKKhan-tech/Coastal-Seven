def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)
int = int(input("Enter a number: "))
print(total(int))