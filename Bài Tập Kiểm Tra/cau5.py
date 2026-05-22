m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
tong = 0
m = n
while m > 0:
    chu_so = m % 10
    tong = tong + chu_so
    m = m // 10
print("Tong cac chu so cua n =", tong)
if m % tong == 0:
    print("m chia het cho tong cac chu so cua n")
else:
    print("m khong chia het cho tong cac chu so cua n")