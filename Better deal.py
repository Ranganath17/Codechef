# There are 2 stores in Chefland and both sell the same product. The first store sells the product for 100 rupees whereas the second store sells it for 200 rupees.
# It is the holiday season and both stores have announced a special discount. The first store is providing a discount of A percent on its product and the second store
# is providing a discount of B percent on its product.Chef is wondering which store is selling the product at a cheaper price after the discount has been applied.
# Can you help him identify the better deal?Input Format The first line of input will contain a single integer T, denoting the number of test cases.Each test case
# consists of a single line of input containing two space-separated integers A and B denoting the discount provided by the first and second store respectively.



t= int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=100-(x)
    b=200-((y)*2)
    if a==b:
        print('BOTH')
    elif a>b:
        print('SECOND')
    else:
        print('FIRST')
