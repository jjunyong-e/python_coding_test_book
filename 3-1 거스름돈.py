N = int(input())

change_arr = [500,100,50,10]
cnt =0

while N!= 0:
    for c in change_arr:
        cnt += N // c 
        N = N % c         
        


print(cnt)