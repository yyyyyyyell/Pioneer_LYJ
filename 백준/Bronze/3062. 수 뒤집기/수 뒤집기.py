T=int(input())
for i in range(T):
    a=input()
    b=a[::-1]
    sum=str(int(a)+int(b))
    if sum == sum[::-1]:
        print('YES')
    else: print('NO')
