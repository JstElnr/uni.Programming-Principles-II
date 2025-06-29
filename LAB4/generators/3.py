def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input("Enter a number: "))
numbers = divisible(n)
numbers_str = ', '.join(str(num) for num in numbers)
print("Numbers divisible by 3 and 4 between 0 and", n, ":", numbers_str)
