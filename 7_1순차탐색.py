object_arr = list(map(str,input().split(' ')))
target = 'Dongbin'
idx = 0
for index in range(len(object_arr)):
    if target == object_arr[index]:
        idx = index

print(f'{target}의 순서는 {idx+1}입니다')
