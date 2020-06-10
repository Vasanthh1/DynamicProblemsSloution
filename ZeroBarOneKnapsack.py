def zeroBarOneKnapsack(n,c):#weight array,weightArrayLength,CapacityOfBag
    tab = [[0 for i in range(c+1)] for i in range(n+1)]   
    for i in range(1,n+1):
        for j in range(1,c+1):
            if weight[i-1] <= j:
                tab[i][j] = max(val[i-1]+tab[i-1][j-weight[i-1]],
                                tab[i-1][j])
            else:
                tab[i][j] = tab[i-1][j]
    return tab[n][c]

if __name__=='__main__':
    val = list(map(int,input().split()))
    weight = list(map(int,input().split()))
    c = int(input())
    print(zeroBarOneKnapsack(len(val),c))
