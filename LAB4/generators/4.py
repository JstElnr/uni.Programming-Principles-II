def squares_gen(a, b):
    for i in range(a, b+1):
        yield i**2
for square in squares_gen(1, 5):
    print(square)