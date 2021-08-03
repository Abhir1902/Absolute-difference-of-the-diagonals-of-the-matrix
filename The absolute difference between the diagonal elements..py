#Absolute difference between the
print("Enter the order of the matrix")
n=int(input())
m=[]
for i in range(n):
    l=list(map(int,input().split()))
    m.append(l)
sum1=0
sum2=0
for i in range(n):
    for j in range(n):
        if(i==j):
            sum1+=m[i][j]
        elif(i+j==n-1):
            sum2+=m[i][j]
print("The absolute differnce between the diagonal elements is : ",abs(sum1-sum2))
