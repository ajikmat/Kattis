import math

case = int(input())
g = 9.81

for i in range(case):
    v, angle, x1, h1, h2 = map(float, input().split())
    
    t = x1 / (v * (math.cos(math.radians(angle))))
    y = v * t * (math.sin(math.radians(angle))) - (0.5 * g) * (t ** 2)

    if (h1+1) < y < (h2-1):
        print("Safe")
    else:
        print("Not Safe")
