N=int(input())
if N==1:
    print("*")
elif N%2==0:
    for i in range (N//2):
        print('* '*(N-1)+'*')
        print(" *"*N)
elif N%2==1:
    for i in range (N):
        if i%2==0:
            print('* '*(N-1)+'*')
        else:
            print(" *"*N)