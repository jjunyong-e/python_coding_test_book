n = int(input())
# 시간 입력 0 :00: 00 ~ n : 59 : 59까지 3 이들어가는 시간갯수


count = 0

# i시j분k초 = ijk로 나타내고 ijk에 3이있는경우 count에 1 추가 
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            hour = str(i) + str(j) + str(k)
            if('3' in hour):
                count +=1
print(count)