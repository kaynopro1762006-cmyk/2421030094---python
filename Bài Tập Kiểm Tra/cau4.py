a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
tong = a + b
print("Tong =", tong)
max_cs = 0
m = tong
while m > 0:
    chu_so = m % 10
    if chu_so > max_cs:
        max_cs = chu_so
    m = m // 10
print("Chu so lon nhat =", max_cs)