def prime(num):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        return "Prime"
    else:
        return "Not Prime"
int = int(input("Enter number: "))
print(prime(int))
