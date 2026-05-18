def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num = num // 10

    return count
int = int(input("Enter a number: "))
print(count_digits(int))