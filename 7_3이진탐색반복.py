input_arr = sorted(list(map(int,input("숫자입력 : ").split())))
target = int(input("찾으려는 숫자 입력 : "))
switch = True
idx = 0
def find_target(arr,target_int,first,last):
    
    mid = round((first + last)/2)

    while arr[mid] != target_int:
        if arr[mid] == target_int: 
            return mid

        elif arr[mid] < target_int:
            first = mid
            return first
        else:
            last = mid
            return last

    return None

last = len(input_arr)

idx = find_target(input_arr,target,0,last)  
print(input_arr)
print(f'{target}는 {idx + 1}번째 숫자입니다')