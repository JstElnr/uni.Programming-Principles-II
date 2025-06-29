def solve(numheads, numlegs):
    for x in range(numheads + 1):
        y = numheads - x
        if 2 * x + 4 * y == numlegs:
            return x, y
    return None, None


head = int(input())
legs = int(input())

chicken, rabbit = solve(head,legs)
if chicken is not None and rabbit is not None:
    print(f"there are {chicken} chickens and {rabbit} rabbits")
else:
    print("no solution")