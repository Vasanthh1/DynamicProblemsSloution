def LongestRepSub(s):
    n = len(s)
    l = [[0 for j in range(n+1)] for i in range(n+1)]
    ind,res_len = 0,0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if s[i-1]==s[j-1] and (j-i > l[i-1][j-1]):
                l[i][j] = l[i-1][j-1]+1
                if l[i][j]> res_len:
                    res_len = l[i][j]
                    ind = max(i,ind)
            else:
                l[i][j] = 0
    return s[ind-res_len:ind]
if __name__=='__main__':
    print(LongestRepSub(input("Enter the String:")))
