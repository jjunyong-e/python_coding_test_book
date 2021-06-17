N,M = map(int,input().split())
M_arr = sorted(list(map(int,input().split())))
H_arr = [i for i in range(min(M_arr), max(M_arr)+1)]

for h in H_arr:
    cutted_arr = list(map(lambda x: x - h,M_arr))
    cutted_arr = [c for c in cutted_arr if c >=0]
    if sum(cutted_arr) == M:
        print(h)
        