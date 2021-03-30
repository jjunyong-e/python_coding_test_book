n, k = map(int,input().split())

# n에서 1을 뺀다
# n을 k로나눈다
# 위의 규칙둘중하나를 이용하여 n을 1로만드는 최소횟수를 구한다


count = 0

while True:
    if n == 1:
        break
    else:
        if (n % k == 0):
            if n == 1:
                break
            n /= k
            count+=1
        else:
            if n== 1:
                break
            n -= 1
            count +=1
    
print(count)