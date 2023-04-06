# There are N children and Chef wants to give them 1 candy each. Chef already has X candies with him. To buy the rest, he visits a candy shop. In the shop,
# packets containing exactly 4 candies are available.Determine the minimum number of candy packets Chef must buy so that he is able to give 1 candy to each of 
# the N children.



import math
t=int(input())
for i in range (t):
    x,y=map(int,input().split())
    if x<=y:
        print('0')
    else:
        a=x-y
        print(math.ceil(a/4))
