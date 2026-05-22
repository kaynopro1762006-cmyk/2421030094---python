n = int(input("Nhap n: "))
tong = 0
m = n
while m > 0:
    chu_so = m % 10
    tong = tong + chu_so
    m = m // 10
if tong % 3 == 0:
    print("Tong chu so chia het cho 3")
else:
    print("Tong chu so khong chia het cho 3")