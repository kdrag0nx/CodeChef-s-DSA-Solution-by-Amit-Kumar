'''

Author: Amit Kumar
Python Version: 3.5 and above

'''

tESTCASES=int(input())
while tESTCASES:
       tESTCASES -=1
       st =  input()
       ln= len(st)
       x=ln//2
       if ln%2==0:
              
             if sorted(st[:x])==sorted(st[x:]):
              print("YES")
             else:
              print("NO")
       else:
             if sorted(st[:x]) == sorted(st[x+1:]):
              print("YES")
             else:
              print("NO")