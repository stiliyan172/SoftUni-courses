flag_1 = False

while not flag_1:
    number = float(input())
    if 1 <= number <= 100:
        print(f'The number {number} is between 1 and 100')
        break
