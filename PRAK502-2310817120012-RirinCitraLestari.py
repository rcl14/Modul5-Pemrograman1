def mutlak(angka):
    return abs(angka)

def hitung(nilai1, nilai2):
    return abs(nilai1 - nilai2)

if __name__ == "__main__":
    a, c, b, d = map(int, input().split())
    hasil = hitung(a, b) + hitung(c, d)
    print(mutlak(hasil))
