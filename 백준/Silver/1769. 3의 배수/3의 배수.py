n = input()
count = 0 

while len(n)>1: 
    count+=1 
    answer=0
    for i in n:
        answer+=int(i) 
    n =str(answer) 

print(count) 

if int(n)%3 ==0: 
      print("YES")
else:
       print("NO")