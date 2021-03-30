import time
Strart_time = time.time()
N,M,K = map(int,input().split())
# N = 배열크기 , M = 숫자가 더해지는 횟수, K = 최대 더해질수있는 횟수

num_arr= list(map(int,input().split()))
# 배열 입력

num_arr.sort(reverse=True)
# 배열을 내림차순 정렬

output = 0
# 결과값으로 출력할수를 0 으로 초기화

first = num_arr[0]
second = num_arr[1]

while True:
    for i in range(K):
        if M == 0:
            break
        
        output += first
        M -= 1
    if M == 0:
        break
    output += second
    M -= 1
print(output)
    
