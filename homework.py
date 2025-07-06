n = int(input())
for i in range(n):
    n1 = int(input())
    operate = input()
    min = 1
    max = n1
    ans = []
    for j in reversed(operate):
        if j == '<':
            ans.append(min)
            min+=1
        else:
            ans.append(max)
            max-=1
    ans.append(max)
    for k in reversed(ans):
        print(k, end=' ')
    print()