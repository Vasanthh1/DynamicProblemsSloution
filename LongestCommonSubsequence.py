def lcs(a,b):
    n,m = len(a),len(b)
    tab = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                tab[i][j] = tab[i-1][j-1]+1
            else:
                tab[i][j] = max(tab[i-1][j],tab[i][j-1])
    return tab[n][m]


    
if __name__=='__main__':
    print(lcs(input(),input()))







    
