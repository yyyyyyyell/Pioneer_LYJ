t = int(input())
for i in range(t):
    a,b=input().split()
    A = sorted(a)
    B = sorted(b)
    if A == B:
        print(a,'&', b,'are anagrams.')
    else: print(a, '&', b, 'are NOT anagrams.')

