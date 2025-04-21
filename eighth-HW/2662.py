n = int(input())
arr = list(map(int, input().split()))

first_value = arr[0]
first_index = 0
count = 0

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    
    if i != min_index:
        if first_index == i:
            first_index = min_index
            count += 1
        elif first_index == min_index:
            first_index = i
            count += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]

print(count)
