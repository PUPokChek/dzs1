n = int(input('Введите число '))
def plswork(n):
    if n == 0:
        return 1
    return plswork(n-1) * n
print(plswork(n))
