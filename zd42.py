input_data = open('input.txt', 'r')
n = int(input_data.read())

count = 1


if n == 4:
    ans = 4
else:
    while n > 3:
        count *= 3
        n -= 3
    else:
        count *= n

print(count)