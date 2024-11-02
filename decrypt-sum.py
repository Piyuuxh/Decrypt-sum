def decrypt(code, k):
    res = []
    n = len(code)
    if k == 0:
        return [0] * n

    for i in range(n):
        total = 0
        if k > 0:
            for j in range(1, k + 1):
                total += code[(i + j) % n]

        elif k < 0:
            for j in range(1, -k + 1):
                total += code[(i - j) % n]

        res.append(total)

    return res

code = [3,7,2,5]
k = 3
print(decrypt(code, k))
            
