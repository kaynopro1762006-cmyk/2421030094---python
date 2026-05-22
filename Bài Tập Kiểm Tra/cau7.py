import math
def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập n: "))
tong = 0
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    if so_nguyen_to(x):
        tong += x
print("Tổng các số nguyên tố =", tong)
if tong % 2 != 0 and tong > 50:
    print("Tổng là số lẻ và lớn hơn 50")
else:
    print("Tổng không thỏa điều kiện")