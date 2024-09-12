n=int(input())
count=0
max=1

while n>max:
    count+=1
    max=max+6*count
print(count+1)