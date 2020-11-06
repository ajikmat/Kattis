n = int(input())

for i in range(n):
    r, e, c = map(int, input().split())
    
    if (e-c) > r :
        print("Advertise")
    elif (e-c) < r :
        print("Do not advertise")
    else :
        print("Does not matter")
