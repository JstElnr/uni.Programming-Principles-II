def even_num_gen(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a value for n: "))
even_numbers = even_num_gen(n)
print(','.join(map(str, even_numbers)))