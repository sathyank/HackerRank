def array_left_rotation(a, n, k):
    new_array = a.copy()
    for i in range(n):
        j = (i+k) % n
        new_array[i] = a[j]
    return new_array



n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
#print(*answer, sep=' ')
print(answer)
