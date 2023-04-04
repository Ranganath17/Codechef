# Alice, Bob, and Charlie participated in a 400-metre race.The time taken by Alice, Bob, and Charlie to complete the race was X,Y, and Z seconds respectively.
# Note that X,Y, and Z are distinct. Determine the person having the highest average speed in the race.





t= int(input())
for i in range (t):
    X,Y,Z=map(int,input().split())
    if min(X,Y,Z)==X:
        print("Alice")
    elif min(X,Y,Z)==Y:
        print("Bob")
    else:
        print("Charlie")
