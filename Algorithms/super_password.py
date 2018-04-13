import sys
import re

def minimumNumber(n, password):
    count = 0
    if not re.search('[!@#$%^&*()\-+]', password):
        count+=1
    if not re.search('[a-z]',password):
        count+=1

    if not re.search('[A-Z]',password):
        count+=1
    if not re.search('[0-9]',password):
        count+=1
    if n + count < 6:
        count = count + (6 - (n + count))
    return count
if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
