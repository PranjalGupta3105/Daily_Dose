# 6/5/20
# Its about List comprehension in python

# General mechanism used for traversing through the list is created a nested list
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    p = 0
    ar = []

    for i in range (x+1):
        for j in range(y+1):
            for k in range (z+1):
                if((i+j+k)!=n):
                    ar.append([])
                    ar[p] =[i,j,k]
                    p+=1

    print(ar)

# Best approach is : List comprehension
    ar = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if((i+j+k)!=n)]

    print(ar)
