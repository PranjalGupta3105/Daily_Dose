if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    f=s=-2147483648

    for i in range(len(arr)):
        if(arr[i]>f):
            s = f
            f= arr[i]
        elif (arr[i]>s and arr[i]!=f):
            s = arr[i]

    print(s)






