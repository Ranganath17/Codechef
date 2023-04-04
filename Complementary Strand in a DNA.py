You are given the sequence of Nucleotides of one strand of DNA through a string S of length N. S contains the character A,T,C and G only. Chef knows that:
A is complementary to T.
T is complementary to A.
C is complementary to G.
G is complementary to C.
Using the string S, determine the sequence of the complementary strand of the DNA.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

t= int(input())
for i in range (t):
    n=int(input())
    a=input()
    ans=''
    for i in a:
        if i=="A":
            ans+="T"
        elif i=="T":
            ans+="A"
        elif i=="C":
            ans+="G"
        else:
            ans+="C"
    print(ans)
    
