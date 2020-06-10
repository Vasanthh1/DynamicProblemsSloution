#It takes O(n^2) time complexity

def LongestIncreasingSub(n,l):
    tab = [0 for i in range(n)]
    tab[n-1] = 1
    for i in range(n-1,-1,-1):
        j = i+1
        m = 0 
        while j<n and l[i]<l[j] and m<tab[j]:
            m = tab[j]
            j+=1
        tab[i] = m+1
    print(tab)
    return max(tab)
            
if __name__=='__main__':
    n = int(input())#Array length
    l = list(map(int,input().split()))#Array Elements
    print(LongestIncreasingSub(n,l))
