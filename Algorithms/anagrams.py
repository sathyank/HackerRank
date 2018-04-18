def number_needed(a, b):
        hist = [0]*26
        sum = 0
        for i in range(len(a)):
            hist[a[i] - ord("a")] = hist[a[i] - ord("a")] + 1
        for i in range(len(b)):
            hist[b[i] - ord("a")] = hist[b[i] - ord("a")] - 1
        for i in range(26):
            if 0 < hist[i]:
                sum += hist[i]
            else:
                sum += -hist[i]
        return sum 

a = input().strip()
b = input().strip()

print(number_needed(a, b))
