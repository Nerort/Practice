max_range = input('Enter any even number')
max_range += 1
total = 0
for number in range(2, max_range, 2):
    total += number
print(total)
