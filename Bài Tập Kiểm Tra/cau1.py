n = int(input("Nhap n: "))
tong = 0
m = 0
for i in range(n):
    x = float(input("Nhap so thu " + str(i + 1) + ": "))
    if x > 0 and x < 1000:
        tong = tong + x
        m = m + 1
if m > 0:
    trung_binh_cong = tong / m
    print("Trung binh cong =", trung_binh_cong)
else:
    print("Khong co so hop le")