n,m = map(int,input().split())
# n m 입력

card = list()
# 카드 저장될 리스트

min_num = list()
# 각행의 작은수들 저장할 리스트
for i in range(n):
    card.append(list(map(int,input().split())))

for i in range(n):
    min_num.append(min(card[i][:]))
# 각행에서 작은수들을 저장하고 그중 가장 큰수를 출력하면된다
print(max(min_num))


