# Chef is playing a video game, and is now fighting the final boss. The boss has H health points. Each attack of Chef reduces the health of the boss by X. 
# Chef also has a special attack that can be used at most once, and will decrease the health of the boss by Y. Chef wins when the health of the boss is ≤ 0. What is the 
# minimum number of attacks needed by Chef to win?

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import math
for i in range(int(input())):
    h,x,y=map(int,input().split())
    if x>=y:
        print(math.ceil(h/x))
    else:
        print(math.ceil((h-y)/x)+1)
