def square_gen(N):
    for i in range(1, N+1):
        yield i**2
for x in square_gen(5):
    print(x)