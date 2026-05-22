a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
tong = a + b + c
print("Tổng =", tong)
dem = 0
for ch in str(tong):
    if int(ch) % 2 == 0:
        dem += 1
print("Số chữ số chẵn trong tổng =", dem)
