nums = list(map(int, input().split()))
a = nums[0]
b = nums[1]
n = nums[2]

for num in range(1, n + 1):
    if num % a == 0 and num % b == 0:
        print("FizzBuzz")
    elif num % a == 0:
        print("Fizz")
    elif num % b == 0:
        print("Buzz")
    else:
        print(num)
