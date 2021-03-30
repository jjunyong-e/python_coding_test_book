n = int(input())
# 최대 좌표는 n
arr = list(input().split())
# 방향을 저장

a,b = 1,1

# arr 에 있는것을 하나씩 꺼내서 각 방위에 따라 좌표 변경
# 각 좌표에서 불가능한경우 무시
for i in arr:
    if i == 'L':
    
        if b == 1:
            pass
        else:
            b -= 1
        
        
    elif i == 'R':
        
        if b == n:
            pass
        else:
            b += 1
        
    elif i == 'U':
        
        if a == 1:
            pass
        else:
            a -= 1
        
    else:

        if a == n:
            pass
        else:
            a += 1


print(a,b)        

