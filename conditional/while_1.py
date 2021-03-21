score, ttl, count = 0, 0, 0

while (score != -1):
    score = float(input('Input the score or -1 to exit: '))
    if score != -1:
        ttl += score
        count += 1

print(f'The average is {ttl / count}')
