# Chef has N empty bottles where each bottle has a capacity of X litres.There is a water tank in Chefland having K litres of water. Chef wants to fill the empty
# bottles using the water in the tank.Assuming that Chef does not spill any water while filling the bottles, find out the maximum number of bottles Chef can fill
# completely.


t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if z/y<=x:
        print(int(z/y))
    elif z/y>=x:
        print(x)
    else:
        print(0)
