if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    rup = 0

    for i in range (len(arr)-1):
        if(arr[i]<arr[i+1]):
            rup = arr[i]
            # print(rup)
        else:
            if(arr[i]>arr[i+1]):
                rup = arr[i+1]
                # print(rup)

    print(rup)
