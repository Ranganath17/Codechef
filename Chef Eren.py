# Chef is a very big fan of Eren Yeager. In the last season of Attack on Titan, there were N episodes numbered from 1 to N. Each even indexed episode was A minutes 
# long and each odd indexed episode was B minutes long. Calculate the total duration (in minutes) of the last season.



t=int(input())
while t>0:
    n,a,b=map(int,input().split())
    if n%2==0:
        print((n//2)*a+(n//2)*b)
    else:
        print((n//2+1)*b+(n-(n//2+1))*a)
    t-=1
