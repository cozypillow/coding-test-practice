T=int(input())
for i in range (T):
    L,S=input().split()
    L=int(L)
    print(S[:L-1]+S[L:])