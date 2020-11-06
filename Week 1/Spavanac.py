nums = list(map(int, input().split()))
hour = nums[0]
minute = nums[1]

if minute < 45:
    minute += 15
    if hour == 0:
        hour = 23
    else:
        hour = hour - 1
else:
    minute = minute - 45

print(str(hour) + " " + str(minute))
