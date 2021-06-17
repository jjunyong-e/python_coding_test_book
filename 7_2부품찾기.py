N = int(input())
N_arr = sorted(list(map(int,input().split())))
M = int(input())
M_arr = list(map(int,input().split()))


for m in M_arr:
    if m in N_arr:
        print("yes")
    else:
        print("no")
    