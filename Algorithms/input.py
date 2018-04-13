first,second,n=map(int,raw_input().split())
for i in range(2,n):
   third = second**2 + first
   first = second
   second = third
print(third)
