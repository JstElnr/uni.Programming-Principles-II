import math, time
def dsqrt(num, ms):
    time.sleep(ms/1000)
    return math.sqrt(num)
print(f"Sqrt of 25100 after 2123ms is {dsqrt(25100,2123)}")