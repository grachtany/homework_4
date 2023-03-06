n = int(input())

bushes = [int(i) for i in input().split]
bush_max = 0

for i in range(n):
    bush_sum = bushes[i-1] + bushes[i] + bushes[i+1 if n - 1 else 0]
    if bush_sum > bush_max:
        bush_max = bush_sum

print(bush_max)