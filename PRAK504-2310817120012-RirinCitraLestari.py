def reverse(n):
    return int(str(n)[::-1])

A, B = map(int, input().split())
A_reversed = reverse(A)
B_reversed = reverse(B)
C = A_reversed + B_reversed
hasil = reverse(C)
print(hasil)
