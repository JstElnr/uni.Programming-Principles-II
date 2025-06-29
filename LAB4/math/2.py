def trap(a, b, h):
    A = ((a + b) * h) / 2
    return A
x = int(input("Input 1st base: "))
y = int(input("Input 2nd base: "))
z = int(input("Input height: "))
print(trap(x, y, z))