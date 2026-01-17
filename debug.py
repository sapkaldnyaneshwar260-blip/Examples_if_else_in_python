a = 54321
s = 0
while a!= 0:
    r = a%10
    if r%2 == 0:
        s = s*10+r
    a = a//10
print(s)   
rev =0

while s!=0:
   rem = s%10
   rev = rev*10+rem
   s = s//10
print(rev)  

   

