n = int(input("Nhap n: "))
tich = 1
m = n
while m > 0:
    chu_so = m % 10
    tich = tich * chu_so
    m = m // 10
print("Tich cac chu so =", tich)
if tich % 2 == 0 and tich > 20:
    print("Tich la so chan va lon hon 20")
else:
    print("Khong thoa man")