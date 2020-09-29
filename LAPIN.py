'''

Author: Amit Kumar
Python Version: 3.5 and above
Lapindrome is basically a string in which first n length of string from middle is equal to last n length of string from middle
for eg. xoxo so if you consider from middle then it will be xo in the 1st half and xoxo on another half 
so below is the code you can try in vs code or any python ide to pratice
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
