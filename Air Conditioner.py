# There are three people sitting in a room - Alice, Bob, and Charlie. They need to decide on the temperature to set on the air conditioner. Everyone has a demand each:
# Alice wants the temperature to be at leastA degrees.
# Bob wants the temperature to be at most B degrees.
# Charlie wants the temperature to be at least C degrees.
# Can they all agree on some temperature, or not?



t=int(input())
for i in range (t):
    x,y,z=map(int,input().split())
    if x<=y and z<=y:
        print("YES")
    else:
        print("NO")
