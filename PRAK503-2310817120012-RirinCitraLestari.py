def nilaiTerbesarTerkecil(bilangan):
    return max(bilangan), min(bilangan)

N = int(input())
bilangan = list(map(int, input().split()))
terbesar, terkecil = nilaiTerbesarTerkecil(bilangan)
print(terbesar, terkecil)
