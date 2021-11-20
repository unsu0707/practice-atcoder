N = int(input())

result = ['']
for i in range(N):
    new_result = []
    for j in range(len(result)):
        for kakko in ['(',')']:
            new_result.append(result[j] + kakko)
    result = new_result
for str in result:
    check = 0
    for c in str:
        if c == '(':
            check += 1
        elif c == ')':
            check -= 1
        if check < 0:
            break
    if check == 0 and N > 0:
        print(str)
