a = input()

x = int(ord(a[0]) - ord('a'))+1
y = int(a[1])
# 문자 입력받으니까 아스키코드로 변환해서 하자

move = [(-2,1),(-2,-1),(2,-1),(2,1),(1,-2),(1,2),(-1,2),(-1,-2)]
# 이동할수있는경로


opt = 0
for i in move:
    dx = x + i[0]
    dy = y + i[1]
    if ((1 <= dx <= 8) and (1 <= dy <= 8)):
        opt += 1
        
print(opt)